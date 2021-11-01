from Domain.rezervare import toString
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare
from Logic.functionalitate import reducerePret, trecereRezervariPeUnNume, sumaPreturiPerNume, ordonareDupaPretDescrescator, \
    pretMaxperClasa


def printMenu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("4. Reducere pret cu un procentaj dat")
    print("5. Trecerea tuturor rezervarilor introduse pe un nume dat")
    print("6. Determinarea rezervarii cu cel mai mare pret din fiecare clasa")
    print("7. Ordonarea rezervarilor descrescator după preț")
    print("8. Afișarea sumelor prețurilor pentru fiecare nume")
    print("a. Afisare prajituri")
    print("x. Iesire")


def uiAdaugaRezervare(lista):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        print("Variantele de clase: /"
              "1 Economy/"
              "2 Economy plus/"
              "3 Business")
        clasaImput = input("Alegeti clasa prin numarul din dreptul clasei: ")
        if clasaImput==1:
            clasa="economy"
        elif clasaImput==2:
            clasa="economy plus"
        elif clasaImput==3:
            clasa="business"
            '''
            eroare
            '''
        pret = float(input('Dati pretul: '))
        print("Daca s-a facut checkin-ul apasati tasta 1 , /"
              " in caz contrar apasati tasta 0")
        checkInInput = int(input("Alegeti varianta de checkin: "))
        if checkInInput==1:
            checkIn="Da"
        elif checkInInput==0:
            checkIn="Nu"
            '''
            eroare
            '''
        return adaugaRezervare(id, nume, clasa, pret, checkIn, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeRezervare(lista):
    try:
        id = input("Dati id-ul rezervarii de sters: ")
        return stergeRezervare(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaRezervare(lista):
    try:
        id = input("Dati id-ul rezervarii de modificat: ")
        nume = input("Dati noul nume: ")
        print("Variantele de clase: /"
              "1 Economy/"
              "2 Economy plus/"
              "3 Business")
        clasaImput = input("Alegeti noua clasa prin numarul din dreptul clasei dorite: ")
        if clasaImput == 1:
            clasa = "economy"
        elif clasaImput == 2:
            clasa = "economy plus"
        elif clasaImput == 3:
            clasa = "business"
            '''
            eroare
            '''
        pret = float(input('Dati noul pret: '))
        print("Daca s-a facut checkin-ul apasati tasta 1 , /"
              " in caz contrar apasati tasta 0")
        checkInInput = int(input("Alegeti varianta noua de checkin: "))
        if checkInInput == 1:
            checkIn = "Da"
        elif checkInInput == 0:
            checkIn = "Nu"
            '''
            eroare
            '''
        return modificaRezervare(id, nume, clasa, pret, checkIn, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def uiReducerePret(lista):
    try:
        procent = int(input("Dati procentele pe care vreti sa le reduceti din pret: "))
        return reducerePret(procent, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiTrecereRezervariPeUnNume(lista):
    try:
        nume = int(input("Dati numele: "))
        showAll(trecereRezervariPeUnNume(nume, lista))
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiPretMaxperClasa(lista):
    rezultat = pretMaxperClasa(lista)
    for an in rezultat:
        print("Clasa {} are pretul maxim {}".format(an, rezultat[an]))


def uiOrdonareDupaPretDescrescator(lista):
    showAll(ordonareDupaPretDescrescator(lista))


def uiSumaPreturiPerNume(lista):
    rezultat = sumaPreturiPerNume(lista)
    for nume in rezultat:
        print("Numele {} are suma preturilor {}".format(nume, rezultat[nume]))


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaRezervare(lista)
        elif optiune == "2":
            lista = uiStergeRezervare(lista)
        elif optiune == "3":
            lista = uiModificaRezervare(lista)
        elif optiune == "4":
            lista = uiReducerePret(lista)
        elif optiune == "5":
            uiTrecereRezervariPeUnNume(lista)
        elif optiune == "6":
            uiPretMaxperClasa(lista)
        elif optiune == "7":
            uiOrdonareDupaPretDescrescator(lista)
        elif optiune == "8":
            uiSumaPreturiPerNume(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")