# 07. Iterátorok és generátorok – gyakorló feladatok

Három rövid feladat a modul gyakorlásához.

### 1. Egy iterátor elfogyasztása 

**Cél:** Az iterátor állapotának és kimerülésének megfigyelése.

**Feladat:** Készíts iterátort az `["piros", "zöld", "kék"]` listából az `iter()` segítségével. Két `next()` hívással írd ki az első két elemet, majd egy `for` ciklussal a maradékot. Ezután hívd meg a `next(iterator, "elfogyott")` kifejezést, és írd ki az eredményt.

**Ellenőrzés:** A kimenet sorrendben `piros`, `zöld`, `kék`, `elfogyott`. A ciklus nem kezdi újra a listát.

### 2. Páros számok generátora 

**Cél:** Értékek előállítása egyenként a `yield` használatával.

**Feladat:** Írj `even_numbers(limit)` generátorfüggvényt, amely 0-tól a megadott határig, a határt is beleértve, előállítja a páros számokat. Ne készíts benne listát. Vizsgáld meg a `list(even_numbers(6))` és a `list(even_numbers(5))` eredményét.

**Ellenőrzés:** Az eredmények `[0, 2, 4, 6]` és `[0, 2, 4]`. Egy `even_numbers(6)` példányon két egymást követő `next()` hívás `0`-t, majd `2`-t ad.

### 3. Változatok párosítása 

**Cél:** Kombinációk előállítása az `itertools.product()` használatával.

**Feladat:** Adott két lista: `colors = ["piros", "kék"]` és `sizes = ["S", "M"]`. A `product()` segítségével állítsd elő az összes szín–méret párt, majd alakítsd listává az eredményt. A szín legyen a párok első eleme.

**Ellenőrzés:** Az eredmény `[("piros", "S"), ("piros", "M"), ("kék", "S"), ("kék", "M")]`. Mind a négy lehetséges párosítás szerepel benne.
