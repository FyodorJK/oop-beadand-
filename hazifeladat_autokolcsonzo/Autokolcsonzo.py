class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def autokHozzaadasa(self, auto):
        self.autok.append(auto)

    def berlesHozzaadasa(self, berles):
        self.berlesek.append(berles)
        print("Bérlés hozzáadva.")

    def berlesLemondasa(self, berles):
        self.berlesek.remove(berles)
        print("Bérlés lemondva.")

    def berlesekListazasa(self):
        if len(self.berlesek) == 0:
            print("Nincsenek bérlések.")
        else:
            for b in self.berlesek:
                print(b.berlesKiirasa())