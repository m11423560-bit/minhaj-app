const cacheName = 'minhaj-school-cache-v1';
const assets = [
  './',
  './index.html'
];

// فائلوں کو موبائل میں محفوظ کرنا
self.addEventListener('install', evt => {
  evt.waitUntil(
    caches.open(cacheName).then(cache => {
      console.log('فائلیں محفوظ ہو رہی ہیں...');
      cache.addAll(assets);
    })
  );
});

// بغیر انٹرنیٹ کے فائلیں دکھانا
self.addEventListener('fetch', evt => {
  evt.respondWith(
    caches.match(evt.request).then(cacheRes => {
      return cacheRes || fetch(evt.request);
    })
  );
});
