class Werknemer:
    aantalwn = 0

    def __init__(self, naam, geslacht):
        self.id = "id" + str(Werknemer.aantalwn + 1)
        self.naam = naam
        self.geslacht = geslacht

    def __str__(self):
        return f"ID:\t{self.id}\nNaam:\t{self.naam}\nGeslacht:\t{self.geslacht}"

    def print_aantal_wn(self):
        print("Het bedrijf telt:",Werknemer.aantalwn,"Werknemers")


class Bediende(Werknemer):

    def __init__(self, naam, geslacht, maandloon, functie):
        super().__init__(naam, geslacht)
        self.maandloon = maandloon
        self.functie = functie
        Werknemer.aantalwn += 1

    def __str__(self):
        super().__str__()
        return f"Functie:\t{self.functie}\nMaandloon:\t{self.maandloon}"

    def toon_jaar_loon(self):
        return self.maandloon * 12


class Arbeider(Werknemer):

    def __init__(self, naam, geslacht, uurloon, uurperweek):
        super().__init__(naam, geslacht)
        self.uurloon = uurloon
        self.uurperweek = uurperweek
        Werknemer.aantalwn += 1

    def __str__(self):
        super().__str__()
        return f"Uurloon:\t{self.uurloon}\nAantal uur per week:\t{self.uurperweek}"

    def toon_jaar_loon(self):
        return self.uurloon * self.uurperweek * 4 * 13


a1 = Arbeider("Bob", "M", 13, 38)
a1.print_aantal_wn()
