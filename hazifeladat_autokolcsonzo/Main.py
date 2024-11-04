from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from Autokolcsonzo import Autokolcsonzo
from Berles import Berles

kolcsonzo = Autokolcsonzo("Budapesti Autókölcsönző")
auto1 = Szemelyauto("AAAA-153", "Toyota Corolla", 10000)
auto2 = Szemelyauto("SHZ-446", "Ford Focus", 15000)
auto3 = Teherauto("POI-769", "Mercedes Sprinter", 25000)
kolcsonzo.autokHozzaadasa(auto1)
kolcsonzo.autokHozzaadasa(auto2)
kolcsonzo.autokHozzaadasa(auto3)
kolcsonzo.berlesHozzaadasa(Berles(auto1, "2024.11.01"))
kolcsonzo.berlesHozzaadasa(Berles(auto2, "2024.11.02"))
kolcsonzo.berlesHozzaadasa(Berles(auto3, "2024.11.03"))
kolcsonzo.berlesHozzaadasa(Berles(auto1, "2024.11.04"))

print("\t")

while True:
    print("1. Autó bérlése")
    print("2. Bérlés lemondása")
    print("3. Bérlések listázása")
    print("4. Kilépés")
    valasz = input("Válassz egy számot(1-4): ")

    if valasz == "autoHozzaadas":
        titkosertek = input("Szemelyauto vagy Teherauto: ")
        if titkosertek == "Szemelyauto":
            rendszam = input("Add meg az autó rendszámát: ")
            tipus = input("Add meg az autó tipusát: ")
            berletiDij = input("Add meg az autó bérleti díjat: ")
            kolcsonzo.autokHozzaadasa(Szemelyauto(rendszam, tipus, berletiDij))
        if titkosertek == "Teherauto":
            rendszam = input("Add meg az autó rendszámát: ")
            tipus = input("Add meg az autó tipusát: ")
            berletiDij = input("Add meg az autó bérleti díjat: ")
            kolcsonzo.autokHozzaadasa(Teherauto(rendszam, tipus, berletiDij))
    elif valasz == "autokKiirasa":
        print("\t")
        for a in kolcsonzo.autok:
            print(a.adatokKiirasa())
        print("\t")
    elif valasz == "1":
        rendszam = input("Add meg az autó rendszámát: ")
        datum = input("Add meg a bérlés dátumát (YYYY.MM.DD): ")
        auto = None
        for a in kolcsonzo.autok:
            if a.rendszam == rendszam:
                foglalt = False
                for berles in kolcsonzo.berlesek:
                    if berles.auto.rendszam == rendszam and berles.datum == datum:
                        foglalt = True
                        break
                if not foglalt:
                    auto = a
                    break
        if auto is None:
            print("Az autó nem elérhető vagy nem létezik a megadott dátumra.")
        else:
            kolcsonzo.berlesHozzaadasa(Berles(auto, datum))
            print(f"Bérlés hozzáadva, Ár: {auto.berletiDij}")

    elif valasz == "2":
        rendszam = input("Add meg a lemondani kívánt bérlés rendszámát: ")
        datum = input("Add meg a bérlés dátumát (YYYY.MM.DD): ")
        nincs = False
        for b in kolcsonzo.berlesek:
            if b.auto.rendszam == rendszam and b.datum == datum:
                kolcsonzo.berlesLemondasa(b)
                nincs = True
                break
        if not nincs:
            print("Nincs ilyen bérlés.")

    elif valasz == "3":
        kolcsonzo.berlesekListazasa()

    elif valasz == "4":
        break
    else:
        print("Érvénytelen választás, próbálja újra.")