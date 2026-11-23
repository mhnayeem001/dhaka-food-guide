import http.server
import socketserver
import webbrowser
import os
import json

PORT = 5000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(DIRECTORY, "data", "restaurants.json")
JS_DATA_FILE = os.path.join(DIRECTORY, "data", "restaurants_data.js")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Prevent browser from aggressively caching data files
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_POST(self):
        if self.path == "/api/view":
            self.handle_record_view()
        elif self.path == "/api/rate":
            self.handle_submit_rating()
        else:
            self.send_error(404, "Endpoint not found")

    def handle_record_view(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            payload = json.loads(body)
            rest_id = payload.get("restaurant_id")

            if not rest_id:
                self.send_error(400, "Missing restaurant_id")
                return

            with open(DATA_FILE, "r", encoding="utf-8") as f:
                restaurants = json.load(f)

            new_views = 0
            found = False
            for r in restaurants:
                if r.get("id") == rest_id:
                    r["view_count"] = r.get("view_count", 0) + 1
                    new_views = r["view_count"]
                    found = True
                    break

            if found:
                with open(DATA_FILE, "w", encoding="utf-8") as f:
                    json.dump(restaurants, f, ensure_ascii=False, indent=2)
                with open(JS_DATA_FILE, "w", encoding="utf-8") as f:
                    f.write("window.RESTAURANTS_DATA = " + json.dumps(restaurants, ensure_ascii=False, indent=2) + ";\n")

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "new_view_count": new_views}).encode('utf-8'))
        except Exception as e:
            self.send_error(500, f"Error recording view: {str(e)}")

    def handle_submit_rating(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            payload = json.loads(body)
            rest_id = payload.get("restaurant_id")
            stars = float(payload.get("rating", 5))

            if not rest_id or stars < 1 or stars > 5:
                self.send_error(400, "Invalid payload")
                return

            with open(DATA_FILE, "r", encoding="utf-8") as f:
                restaurants = json.load(f)

            new_rating = 0.0
            new_reviews = 0
            found = False
            for r in restaurants:
                if r.get("id") == rest_id:
                    old_rating = float(r.get("rating", 4.5))
                    raw_rev = str(r.get("review_count", 0)).replace(',', '').replace('+', '')
                    try:
                        old_reviews = int(raw_rev)
                    except:
                        old_reviews = 100

                    new_reviews = old_reviews + 1
                    # Bayesian weighted incremental average
                    new_rating = round(((old_rating * old_reviews) + stars) / new_reviews, 1)
                    r["rating"] = new_rating
                    r["review_count"] = new_reviews
                    found = True
                    break

            if found:
                with open(DATA_FILE, "w", encoding="utf-8") as f:
                    json.dump(restaurants, f, ensure_ascii=False, indent=2)
                with open(JS_DATA_FILE, "w", encoding="utf-8") as f:
                    f.write("window.RESTAURANTS_DATA = " + json.dumps(restaurants, ensure_ascii=False, indent=2) + ";\n")

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "new_rating": new_rating, "new_review_count": new_reviews}).encode('utf-8'))
        except Exception as e:
            self.send_error(500, f"Error saving rating: {str(e)}")

if __name__ == "__main__":
    print("=" * 60)
    print(f"🚀 Dhaka Menu Hub Live API Server: http://localhost:{PORT}")
    print("   Endpoints: GET /, POST /api/view, POST /api/rate")
    print("=" * 60)
    print("Press Ctrl+C to stop the server.")
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
