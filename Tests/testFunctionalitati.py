from Domain.rezervare import getId, getPret
from Logic.CRUD import adaugaRezervare, getById
from Logic.functionalitate import reducerePret, trecereRezervariPeUnNume, pretMaxperClasa, ordonareDupaPretDescrescator, \
    sumaPreturiPerNume


def testReducerePret():
    lista = []
    lista = adaugaRezervare("1", "Constanta", "economy", 50, "Nu", lista)
    lista = adaugaRezervare("2", "Timisoara", "economy", 30, "Da", lista)
    lista = adaugaRezervare("3","Oradea","economy", 40,"Da", lista)

    lista = reducerePret(10,lista)

    assert getPret(getById("1", lista)) == 50
    assert getPret(getById("2", lista)) == 27
    assert getPret(getById("3", lista)) == 36

def testTrecereRezervariPeUnNume():
    lista = []
    lista = adaugaRezervare("1", "Suceava", "economy", 20, "Da", lista)
    lista = adaugaRezervare("2", "Satu Mare", "economy", 25, "Nu", lista)

    rezultat = trecereRezervariPeUnNume("Suceava", lista)

    assert len(rezultat) == 2
    assert getById("2", lista) is not None

    rezultat = trecereRezervariPeUnNume("Baia Mare", lista)

    assert len(rezultat) == 2

def testPretMaxperClasa():
    lista = []
    lista = adaugaRezervare("1", "Bacau", "economy", 150, "Da", lista)
    lista = adaugaRezervare("2", "Olt", "business", 180, "Nu", lista)
    lista = adaugaRezervare("3", "Iasi", "economy", 100, "Nu", lista)

    rezultat = pretMaxperClasa(lista)

    assert len(rezultat) == 2
    assert rezultat["business"] == 180
    assert rezultat["economy"] == 150

def testOrdonareDupaPretDescrescator():
    lista = []
    lista = adaugaRezervare("1", "Vaslui", "economy plus", 150, "Da", lista)
    lista = adaugaRezervare("2", "Mehedinti", "business", 130, "Nu", lista)
    lista = adaugaRezervare("3", "Targu Mures", "economy", 140, "Nu", lista)

    rezultat = ordonareDupaPretDescrescator(lista)

    assert getId(rezultat[0]) == "1"
    assert getId(rezultat[1]) == "3"
    assert getId(rezultat[2]) == "2"

def testSumaPreturiPerNume():
    lista = []
    lista = adaugaRezervare("1", "Bistrita", "economy plus", 150, "Da", lista)
    lista = adaugaRezervare("2", "Dej", "business", 130, "Nu", lista)
    lista = adaugaRezervare("3", "Dej", "economy", 140, "Nu", lista)

    rezultat = sumaPreturiPerNume(lista)

    assert len(rezultat) == 2
    assert rezultat["Bistrita"] == 150
    assert rezultat["Dej"] == 270
