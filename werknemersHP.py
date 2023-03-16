from werknemers_klasses import *

def toon_menu():
    print("1: toon alle medewerkers")
    print("2: toon alle arbeiders/bediendes")
    print("3: voeg medewerker toe")
    print("4: verwijder een werknemer")
    print("5: sorteer op naam")
    print("a: geef het aantal werknemers")

def toon_alle_medewerkers():
    print("------------------------------------")
    for medewerker in lijst_werknemers:
        print(medewerker)
        print("------------------------------------")

def toon_arbeiders_bediendes():
    keuze = input("a of b")
    if keuze.upper() == "A":
        for werknemer in lijst_werknemers:
            if isinstance(werknemer,Arbeider):
                print(werknemer)
    else:
            for werknemer in lijst_werknemers:
                if isinstance(werknemer,Bediende):
                    print(werknemer)

def voeg_medewerker_toe():
    keuze = input("Arbeider of bediende")
    if keuze.upper() == "ARBEIDER":
        naam = input("geef de naam in")
        geslacht = input("geef het geslacht in")
        uurloon = int(input("geef het uurloon"))
        urenperweek = int(input("geef het aantal uur per week"))
        w = Arbeider(naam,geslacht,uurloon,urenperweek)
        lijst_werknemers.append(w)
    elif keuze.upper() == "BEDIENDE":
        naam = input("geef de naam in")
        geslacht = input("geef het geslacht in")
        maandloon = int(input("geef het maandloon"))
        functie = input("geef de functie")
        w = Bediende(naam,geslacht,maandloon,functie)
        lijst_werknemers.append(w)
    else:
        print("Werknemer kan niet aangemaakt worden, enkel Arbeiders of Bediendes")

def verwijder_een_medewerker():
    toon_alle_medewerkers()
    verwijder_id = input("geef het id in")
    for werknemer, o in enumerate(lijst_werknemers):
            if o.id == verwijder_id:
                del lijst_werknemers[werknemer]
                break
    o.aantalwn += -1
def sorteer_op_naam():
    lijst_werknemers.sort(key=lambda x:x.naam)
    for wn in lijst_werknemers:
        print(wn)




w1 = Bediende("Bob","M",2000,"Programmeur")
w2 = Bediende("Marcel","M",3000,"Manager")
w3 = Arbeider("Frank","M",14,38)
w4 = Arbeider("Nancy","V",15,30)
w5 = Bediende("An","V",5000,"CEO")

lijst_werknemers = [w1,w2,w3,w4,w5]

################################################
#------------Hoofdprogramma--------------------#
################################################
toon_menu()
opdracht = input("geef opdracht")
while not opdracht == "stop":
    if opdracht == "1":
        toon_alle_medewerkers()
    elif opdracht == "2":
        toon_arbeiders_bediendes()
    elif opdracht == "3":
        voeg_medewerker_toe()
    elif opdracht == "4":
        verwijder_een_medewerker()
    elif opdracht == "5":
        sorteer_op_naam()
    elif opdracht == "a":
        w1.print_aantal_wn()
    else:
        print("foutieve input")
    toon_menu()
    opdracht = input()
