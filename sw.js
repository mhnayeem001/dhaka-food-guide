// Dhaka Menu Hub - Service Worker for Offline Resilience & PWA
const CACHE_NAME = 'dhaka-menu-hub-v505';
const STATIC_ASSETS = [
  './',
  './index.html',
  './data/restaurants.json',
  './data/restaurants_data.js',
  './manifest.json'
];

self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(STATIC_ASSETS))
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.filter(k => k !== CACHE_NAME).map(k => {
        console.log('[SW] Purging stale cache:', k);
        return caches.delete(k);
      })
    )).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  // Network first for data files and index.html, cache fallback
  if (event.request.url.includes('/data/') || event.request.mode === 'navigate') {
    event.respondWith(
      fetch(event.request, { cache: 'no-cache' }).catch(() => caches.match(event.request))
    );
    return;
  }
  // Stale-while-revalidate for static shell assets
  event.respondWith(
    caches.match(event.request).then(cached => {
      const networked = fetch(event.request).then(res => {
        const resClone = res.clone();
        caches.open(CACHE_NAME).then(cache => cache.put(event.request, resClone));
        return res;
      }).catch(() => cached);
      return cached || networked;
    })
  );
});
