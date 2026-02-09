**SERVICE WORKER**
- Service Worker je JavaScriptový skript, ktorý beží na pozadí prehliadača nezávisle od otvorenej stránky a interceptuje sieťové požiadavky. Používa sa na cachovanie zdrojov, zlepšenie rýchlosti, a umožnenie offline režimu.

 PREČO POUŽIŤ
- Rýchlejšie načítanie (cache statických assetov).

- Offline podpora a degradované správanie pri strate siete.

- Možnosť spracovať push notifikácie a pozadí synchronizáciu.

 HLAVNÉ LIFECYCLE UDALOSTÍ
- install — spúšťa precache dôležitých statických súborov pri registrácií alebo novej verzii Service workera 

- activate — čistí staré cache verzie, zabezpečujúc aktuálnosť a konzistenciu cache dát

- fetch — rozhoduje, či vybaviť požiadavku zo siete alebo cache podľa nastavených cahce stratégií

- Riešenie waiting stavu — Nový SW môže zostať v stave waiting, kým použivateľ nezavrie staré karty; skipWaiting urýchluje tento proces

 BEŽNÉ CACHE STRATÉGIE
- Cache-first — pre statické assety (CSS, JS, obrázky). Rýchle, dobré pre offline.

- Network-first — pre dynamické / autentifikačné dáta; fallback na cache pri strate siete.

- Stale-while-revalidate — rýchla odpoveď z cache + pozadie aktualizuje cache zo siete.

 DEFINÍCIA A VÝZNAM
- Beží na pozadí a spravuje sieťové požiadavky

 VÝHODY CACHE A OFFLINE REŽIMU 
-SW umožnuje rýchlejšie načítavanie a fungovanie aplikácie aj bez internetového pripojenia

 PODPORA PWA FUNKCIÍ
- SW umožnuje webovej aplikácii správať sa ako natívna s inštaláciou a ikonou na zariadení

OBMEDZENIA A BEZPEČNOSŤ
- SW funguje iba nna HTTPS alebo localhost a vyžaduje rovnaký pôvod ako webová stránka

**APP SHELL MODEL**

 ZÁKLADNÁ KOSTRA APLIKÁCIE
- App shell precachuje základné súbory ako index.html, CSS a skripty pri inštalácii Service Workera

 RÝCHLEJŠIE NAČÍTAVANIE OFFLINE 
- App shell umožnuje okamžité načítanie aplikácie pri slabom alebo žiadnom internetovom pripojení

 DYNAMICKÉ NAČÍTANIE DÁT
- Dynamické dáta sa načítavajú počas behu aplikácie, oddelene od statickej kostry

 VÝHODY PRE ŠKOLSKÉ PROJEKTY 
- Model App Shell pomáha žiakom pochopiť offline režim a rpzdeliť projekt na statickú a dynamickú časť 
