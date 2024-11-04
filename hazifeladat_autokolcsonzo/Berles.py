class Berles:
    def __init__(self, auto, datum):
        self.auto = auto
        self.datum = datum

    def berlesKiirasa(self):
        return f"Bérlés - Autó: {self.auto.rendszam}, Dátum: {self.datum}, Ár: {self.auto.berletiDij} Ft"