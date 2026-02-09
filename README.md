---SERVICE WORKER---
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

---APP SHELL MODEL---

 ZÁKLADNÁ KOSTRA APLIKÁCIE
- App shell precachuje základné súbory ako index.html, CSS a skripty pri inštalácii Service Workera

 RÝCHLEJŠIE NAČÍTAVANIE OFFLINE 
- App shell umožnuje okamžité načítanie aplikácie pri slabom alebo žiadnom internetovom pripojení

 DYNAMICKÉ NAČÍTANIE DÁT
- Dynamické dáta sa načítavajú počas behu aplikácie, oddelene od statickej kostry

 VÝHODY PRE ŠKOLSKÉ PROJEKTY 
- Model App Shell pomáha žiakom pochopiť offline režim a rpzdeliť projekt na statickú a dynamickú časť

---MINIMÁLNA ŠTRUKTÚRA PWA PROJEKTU---
  POVINNÉ SÚBORY PWA
- Klúčové súbory ako index.html, style.css, sw.js, offline.html a manifest.webmanifest tvoria základ PWA projektu a jeho funkcionality

  ŠTRUKTÚRA PRIEČINKOV
- Priečinok icons obsahuje ikony vo veľkostiach 192x192px a 512x512px pre PWA, zabezpečuje vizuálnu identitu aplikácie

 BRYTHON ŠPECIFIKÁCIA 
- Brython projekty vyžadujú app.py, brython.min a brython_stdlib.js na zabezpečenie lokálnej funkčnosti aj bez internetu

 ODDELENIE STATICKÝCH A DYNAMICKÝCH SÚBOROV 
- Správne usporiadanie súborov oddeľuje statické od dynamických, čo zlepšuje cache a uľahčuje údržbu aplikácie

 ---REGISTRÁCIA SERVICE WORKERA V INDEX.HTML---
  ZÁKLADNÝ KROK PWA
- Registrácia Service Workera je kľúčová pre správnu implementáciu progresívnych webových aplikácií

  UMIESTNENIE V INDEX.HTML
- Kód registrácie sa vkladá pred koniec body, aby sa nezdržovalo načítanie stránky

   BEZPEČNOSTNÉ OBMEDZENIA
- Registrácia funguje len na HTTPS alebo localhost kvôl bezpečnosti prehliadačov

   PROFESIONALITA A LADENIE
- Po registrácii možno sledovať stav v konzole, čo podporuje profesioálnu webovú prax

---SW.JS - PROFESIONÁLNY ZÁKLAD---
 CACHE VERZOVANIE A AKTUALIZÁCIE 
- CACHE_VERSION sa manuálne mení, aby sa zabránilo uchovávaniu zastaraných súborov v cache

 PRECACHE A APP SHELL
- PRECACHE_ASSETS obsahuje kľúćové súbory ako index.html, štýly, skripty a ikony pre rýchly štart aplikácie

 FETCH A OFFLINE CALLBACK
- Pri navigačných požiadavkách sa obsah načítava zo siete, inak sa zobrazí offline stránka offline.html

 RUNTIME CACHING A SELEKTÍVNA OBSLUHA
- Runtine caching umožňuje dynamické dopĺňanie cache a selektívnu obsluhu podľa typu požiadavky 

