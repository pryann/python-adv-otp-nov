### 1. Csak a pozitív számok 
**Cél:** Szűrés `filter` és egy rövid `lambda` segítségével.

**Feladat:** A `[-3, 0, 4, -1, 7, 2]` listából válogasd ki a nullánál nagyobb számokat `filter` használatával. A feltételt `lambda` függvénnyel add meg, az eredményt alakítsd listává. Próbáld ki a megoldást a `[-2, 0]` listán is.

**Ellenőrzés:** Az első eredmény `[4, 7, 2]`, a második `[]`. A nulla egyik eredménybe sem kerülhet be.

### 2. Naplózó dekorátor 

**Cél:** A dekorált függvény visszatérési értékének megőrzése.

**Feladat:** Írj `log_call` dekorátort, amely a becsomagolt függvény hívása előtt kiírja: `Hívás`. A wrapper továbbítsa a pozicionális és nevesített argumentumokat, majd adja vissza a függvény eredményét. Dekorálj vele egy `add(a, b)` összeadó függvényt, és írd ki az `add(2, b=3)` eredményét.

**Ellenőrzés:** Először `Hívás`, majd `5` jelenik meg. Az összeadás visszatérési értéke `5`, nem `None`.


### 3. Várd meg mindkét szálat

**Cél:** Szálak indítása és bevárása `join` segítségével.

**Feladat:** Írj `task(name)` függvényt, amely `0.1` másodperc várakozás után kiírja a nevét. Indíts két `Thread` példányt `"A"` és `"B"` névvel. Mindkettőt indítsd el, mielőtt várakozni kezdenél rájuk. A főprogram csak mindkét szál befejezése után írja ki: `Kész`.

**Ellenőrzés:** `A` és `B` egyaránt egyszer jelenik meg, tetszőleges sorrendben. A `Kész` mindig az utolsó sor.

### 4. Eredmények a szálkészletből

**Cél:** Egy `Future` eredményének lekérése.

**Feladat:** Készíts `square(number)` függvényt, amely visszaadja a szám négyzetét. Egy `ThreadPoolExecutor(max_workers=2)` segítségével, `submit` hívásokkal dolgozd fel a `[2, 3, 4]` számokat. A kapott Future objektumokat tárold listában, majd a beküldés sorrendjében kérd le a `result()` értékeiket.

**Ellenőrzés:** Az összegyűjtött lista `[4, 9, 16]`. Az eredmények sorrendjét a lekérés sorrendje biztosítja, a feladatok befejezési sorrendjétől függetlenül.


### 5. Két külön folyamat 

**Cél:** Folyamatok indítása és befejezésük megvárása.

**Feladat:** Írj `worker(name)` függvényt, amely kiírja: `<név> kész`. Hozz létre két `multiprocessing.Process` példányt `A` és `B` argumentummal. Előbb indítsd el mindkettőt, majd mindkettőn hívd meg a `join()` metódust. Ezután a főfolyamat írja ki: `Vége`.

**Ellenőrzés:** Az `A kész` és a `B kész` egyszer-egyszer jelenik meg, tetszőleges sorrendben. A `Vége` csak mindkét 


### 6. Négyzetek folyamattal 

**Cél:** Adatok feldolgozása a `multiprocessing.Pool.map()` segítségével.

**Feladat:** Írj `square(number)` függvényt. Egy két munkafolyamatot használó poollal számítsd ki az `[1, 2, 3, 4]` elemeinek négyzetét. A poolt `with` blokkban kezeld, az eredménylistát a főfolyamat írja ki.

**Ellenőrzés:** Az eredmény `[1, 4, 9, 16]`, az eredeti bemenet sorrendjében. Ennél a kis feladatnál a gyorsulás nem elvárás.