class Persoon:

    def __init__(self, voornaam,achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam

    def __str__(self):
        return f"{self.voornaam} {self.achternaam}"



if __name__ == "__main__":
    p1 = Persoon("Ben","Bensen")
    p2 = Persoon("Jan","Jansen")
    p3 = Persoon("Frans","Fransen")

    lijst_personen = [p1,p2,p3]
    for persoon in lijst_personen:
        print(persoon)
