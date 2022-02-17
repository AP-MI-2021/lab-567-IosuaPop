import datetime

from Domain.cheltuiala import to_string
from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala
from Logic.functionalitati import sterge_toate_cheltuielile_apartament, adauga_valoare_data, \
    cea_mai_mare_cheltuiala_dupa_tip, ordonare_descrescator_cheltuieli_dupa_suma, sume_lunare_apartament


def print_meniu():
    """
    Meniul de afisat
    """
    print("1. Adauga cheltuiala")
    print("2. Sterge cheltuiala")
    print("3. Modifica cheltuiala")
    print("4. Sterge toate cheltuielile pentru un apartament dat")
    print("5. Aduna o valoare la toate cheltuielile dintr-o dată citită")
    print("6. Determina cea mai mare cheltuiala pentru fiecare tip de cheltuială")
    print("7. Ordoneaza cheltuielile descrescător după sumă.")
    print("8. Afișarea sumelor lunare pentru fiecare apartament.")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare cheltuieli")
    print("x. Iesire")


def ui_adauga_cheltuiala(lista, undo_list, redo_list):
    """
    Adauga o cheltuiala noua la lista
    :param redo_list: lista pentru redo
    :param undo_list: lista pentru undo
    :param lista: lista de cheltuieli
    :return: lista de cheltuilei + cheltuiala nou introdusa
    """
    try:
        id = int(input("Dati id-ul cheltuielii: "))
        numar_apartament = int(input("Dati numarul apartamentului: "))
        suma = float(input("Dati suma: "))
        data = datetime.datetime.strptime(input("Dati data (DD.MM.YYYY): "), "%d.%m.%Y")
        data_string = datetime.datetime.strftime(data, "%d.%m.%Y")
        tipul = input("Dati tipul (intretinere, canal, alte cheltuieli): ")
        rezultat = adauga_cheltuiala(id, numar_apartament, suma, data_string, tipul, lista, undo_list, redo_list)
        return rezultat
    except ValueError as ve:
        print(f"Eroare : {ve}")
        return lista
    except TypeError as te:
        print(f"Eroare: {te}")


def ui_sterge_cheltuiala(lista, undo_list, redo_list):
    """
    Sterge o cheltuiala din lista de cheltuieli
    :param redo_list: lista pentru redo
    :param undo_list: lista pentru undo
    :param lista: lista de cheltuieli
    :return: lista de cheltuieli fara cheltuiala stearsa
    """
    try:
        id_de_sters = int(input("Dati id-ul cheltuielii de sters: "))
        rezultat = sterge_cheltuiala(id_de_sters, lista, undo_list, redo_list)
        return rezultat
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return lista


def ui_modifica_cheltuiala(lista, undo_list, redo_list):
    """
    Modifica o cheltuiala din lista
    :param redo_list: lista pentru redo
    :param undo_list: lista pentru undo
    :param lista: lista de cheltuieli
    :return: lista de cheltuieli cu modificarea aferenta a cheltuielii
    """
    try:
        id = int(input("Dati id-ul cheltuielii de modificat: "))
        numar_apartament = input("Dati noul numar de apartament: ")
        suma = float(input("Dati noua suma: "))
        data = datetime.datetime.strptime(input("Dati noua data (DD.MM.YYYY): "), "%d.%m.%Y")
        data_string = datetime.datetime.strftime(data, "%d.%m.%Y")
        tipul = input("Dati noul tip: ")
        rezultat = modifica_cheltuiala(id, numar_apartament, suma, data_string, tipul, lista, undo_list, redo_list)
        return rezultat
    except ValueError as ve:
        print(f"Eroare : {ve}")
        return lista


def show_all(lista):
    """
    Afiseaza cheltuielile din lista
    :param lista: lista de cheltuieli
    :return: cheltuielile din lista afisate ca string
    """
    for cheltuiala in lista:
        print(to_string(cheltuiala))


def ui_sterge_toate_cheltuielile_apartament(lista, undo_list, redo_list):
    """
    Sterge toate cheltuielile pentru un apartament dat
    :param redo_list: lista pentru redo
    :param undo_list: lista pentru undo
    :param lista: lista de cheltuieli
    :return: lista fara cheltuielile pentru apartamentul specificat
    """
    try:
        numar_apartament = int(input("Dati numarul apartamentului pentru care doriti sa stergeti toate cheltuielile: "))
        rezultat = sterge_toate_cheltuielile_apartament(numar_apartament, lista, undo_list, redo_list)
        return rezultat
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return lista


def ui_adauga_valoare_data(lista, undo_list, redo_list):
    """
    Adauga o valoare la o data specificata
    :param redo_list: lista pentru redo
    :param undo_list: lista pentru undo
    :param lista: lista de cheltuieli
    :return: lista de cheltuieli cu modificarile facute
    (s-a adaugat valoare introdusa la toate cheltuielile din data introdusa)
    """
    try:
        data = datetime.datetime.strptime(input("Introduceti data la care doriti sa adaugati valoarea: "), "%d.%m.%Y")
        data_string = datetime.datetime.strftime(data, "%d.%m.%Y")
        valoare = float(input("Introduceti valoarea pe care doriti sa o adaugati: "))
        rezultat = adauga_valoare_data(data_string, valoare, lista, undo_list, redo_list)
        return rezultat
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return lista


def ui_cea_mai_mare_cheltuiala_dupa_tip(lista):
    """
    Afiseaza cea mai mare suma pentru fiecare tip de cheltuiala
    :param lista: lista de cheltuieli
    :return: cea mai mare suma pentru fiecare tip de cheltuiala din lista
    """
    if not lista:
        print("Nu exista cheltuieli in lista !")
        return lista
    rezultat = cea_mai_mare_cheltuiala_dupa_tip(lista)
    for tip in rezultat:
        print(f"Tipul {tip} are cheltuiala cu valoarea maxima: {to_string(rezultat[tip])}")


def ui_ordonare_descrescator_cheltuieli_dupa_suma(lista, undo_list, redo_list):
    """
    Ordoneaza descrescator dupa suma cheltuielile din lista
    :param redo_list: lista pentru redo
    :param undo_list: lista pentru undo
    :param lista: lista de cheltuieli
    :return: lista ordonata descresctaor dupa suma
    """
    if not lista:
        print("Nu exista cheltuieli in lista !")
        return lista
    else:
        rezultat = ordonare_descrescator_cheltuieli_dupa_suma(lista, undo_list, redo_list)
        return rezultat


def ui_sume_lunare_apartament(lista):
    if not lista:
        print("Nu exista cheltuieli in lista!")
        return lista
    else:
        rezultat = sume_lunare_apartament(lista)
        for apartament in rezultat:
            for data in rezultat[apartament]:
                print(f"Apartamentul {apartament} are sumele lunare pentru {data} : {rezultat[apartament][data]} ")


def ui_undo(lista, undo_list, redo_list) -> list:
    """
    Face undo
    :param lista: lista careia vrem sa-i facem undo
    :param undo_list: lista pentru undo
    :param redo_list: lista pentru redo
    :return: undo la lista
    """
    if len(undo_list) > 0:
        redo_list.append(lista)
        return undo_list.pop()
    return lista


def ui_redo(lista, undo_list, redo_list) -> list:
    """
    Face redo
    :param lista: lista careia vrem sa-i facem redo
    :param undo_list: lista pentru undo
    :param redo_list: lista pentru redo
    :return: redo la lista
    """
    if len(redo_list) > 0:
        undo_list.append(lista)
        return redo_list.pop()
    return lista


def run_menu(lista):
    undo_list = []
    redo_list = []
    while True:
        print_meniu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = ui_adauga_cheltuiala(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = ui_sterge_cheltuiala(lista, undo_list, redo_list)
        elif optiune == "3":
            lista = ui_modifica_cheltuiala(lista, undo_list, redo_list)
        elif optiune == "4":
            lista = ui_sterge_toate_cheltuielile_apartament(lista, undo_list, redo_list)
        elif optiune == "5":
            lista = ui_adauga_valoare_data(lista, undo_list, redo_list)
        elif optiune == "6":
            ui_cea_mai_mare_cheltuiala_dupa_tip(lista)
        elif optiune == "7":
            lista = ui_ordonare_descrescator_cheltuieli_dupa_suma(lista, undo_list, redo_list)
        elif optiune == "8":
            ui_sume_lunare_apartament(lista)
        elif optiune.lower() == "u":
            if len(undo_list) == 0:
                print("Nu se poate face undo !")
            lista = ui_undo(lista, undo_list, redo_list)
        elif optiune.lower() == "r":
            if len(redo_list) == 0:
                print("Nu se poate face redo !")
            lista = ui_redo(lista, undo_list, redo_list)
        elif optiune.lower() == "a":
            if len(lista) > 0:
                show_all(lista)
            else:
                print("Nu exista cheltuieli in lista !")
        elif optiune.lower() == "x":
            break
        else:
            print("Optiune invalida ! Reincercati..")
