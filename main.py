from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UserInterface.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugaRezervare("1", "Constanta", "economy", 50, "Nu", lista)
    lista = adaugaRezervare("2", "Timisoara", "economy", 30, "Da", lista)
    runMenu(lista)


main()
