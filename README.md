Service Worker — README 
- Service Worker je JavaScriptový skript, ktorý beží na pozadí prehliadača nezávisle od otvorenej stránky a interceptuje sieťové požiadavky. Používa sa na cachovanie zdrojov, zlepšenie rýchlosti, a umožnenie offline režimu.

 PREČO POUŽIŤ

- Rýchlejšie načítanie (cache statických assetov).

- Offline podpora a degradované správanie pri strate siete.

- Možnosť spracovať push notifikácie a pozadí synchronizáciu.

HLAVNÉ LIFECYCLE UDALOSTÍ

- install — inicializácia; typicky sa pred-cache-ujú základné súbory.

- activate — aktivácia; miesto na čistenie starých cache a migráciu.

- fetch — zachytáva požiadavky; rozhoduje medzi cache a sieťou (politikou).

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
