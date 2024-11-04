from Auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berletiDij):
        super().__init__(rendszam, tipus, berletiDij)
        self.extrak = "Utasszam"

    def adatokKiirasa(self):
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérleti díj: {self.berletiDij}, {self.extrak}"