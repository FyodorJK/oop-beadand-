from Auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berletiDij):
            super().__init__(rendszam, tipus, berletiDij)
            self.extrak = "Teherbiras"

    def adatokKiirasa(self):
        return f"Teherautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérleti díj: {self.berletiDij}, {self.extrak}"
