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


def uiAdaugaRezervare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele rezervarii: ")
        clasa = input("Dati clasa rezervarii: ")
        pret = float(input('Dati pretul: '))
        checkIn = input("Checkin(Da/Nu): ")
        rezultat = adaugaRezervare(id, nume, clasa, pret, checkIn, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeRezervare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul rezervarii de sters: ")
        rezultat = stergeRezervare(id, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaRezervare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul rezervarii de modificat: ")
        nume = input("Dati noul nume: ")
        clasa = input("Alegeti noua clasa de zbor: ")
        pret = float(input('Dati noul pret: '))
        checkIn = int(input("Alegeti varianta noua de checkin: "))
        rezultat = modificaRezervare(id, nume, clasa, pret, checkIn, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def uiReducerePret(lista, undoList, redoList):
    try:
        procent = int(input("Dati procentele pe care vreti sa le reduceti din pret: "))
        rezultat = reducerePret(procent, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiTrecereRezervariPeUnNume(lista, undoList, redoList):
    try:
        nume = int(input("Dati numele: "))
        rezultat = trecereRezervariPeUnNume(nume, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiPretMaxperClasa(lista, undoList, redoList):
    rezultat = pretMaxperClasa(lista)
    for pret in rezultat:
        print("Clasa {} are pretul maxim {}".format(pret, rezultat[pret]))


def uiOrdonareDupaPretDescrescator(lista, undoList, redoList):
    rezultat = ordonareDupaPretDescrescator(lista)
    undoList.append(lista)
    redoList.clear()
    return rezultat


def uiSumaPreturiPerNume(lista, undoList, redoList):
    rezultat = sumaPreturiPerNume(lista)
    for nume in rezultat:
        print("Numele {} are suma preturilor {}".format(nume, rezultat[nume]))


def runMenu(lista):
    undoList = []
    redoList = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaRezervare(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergeRezervare(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificaRezervare(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiReducerePret(lista, undoList, redoList)
        elif optiune == "5":
            uiTrecereRezervariPeUnNume(lista, undoList, redoList)
        elif optiune == "6":
            uiPretMaxperClasa(lista, undoList, redoList)
        elif optiune == "7":
            uiOrdonareDupaPretDescrescator(lista, undoList, redoList)
        elif optiune == "8":
            uiSumaPreturiPerNume(lista, undoList, redoList)
        elif optiune == "a":
            showAll(lista)
        elif optiune == 'u':
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face Undo!")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face Redo.")
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")