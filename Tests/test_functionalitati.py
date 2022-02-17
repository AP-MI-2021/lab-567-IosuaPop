from Domain.cheltuiala import get_suma, get_data, get_tipul, get_id
from Logic.CRUD import adauga_cheltuiala, get_by_id, get_by_numar_apartament
from Logic.functionalitati import sterge_toate_cheltuielile_apartament, adauga_valoare_data, \
    cea_mai_mare_cheltuiala_dupa_tip, ordonare_descrescator_cheltuieli_dupa_suma, sume_lunare_apartament, \
    get_luna_and_anul_from_data


def test_sterge_toate_cheltuielile_apartament():
    lista = []
    lista = adauga_cheltuiala(1, 13, 150, "06.10.2021", "canal", lista)
    lista = adauga_cheltuiala(2, 45, 200, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(3, 45, 89.45, "12.03.2021", "canal", lista)

    lista = sterge_toate_cheltuielile_apartament(45, lista)
    assert len(lista) == 1
    assert get_by_numar_apartament(45, lista) == []
    assert get_by_numar_apartament(13, lista) == [[("id", 1), ("numar_apartament", 13), ("suma", 150),
                                                   ("data", "06.10.2021"), ("tipul", "canal")]]


def test_adauga_valoare_data():
    lista = []
    lista = adauga_cheltuiala(1, 13, 150, "12.03.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(2, 45, 200, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(3, 45, 89.45, "12.03.2021", "canal", lista)

    lista = adauga_valoare_data("12.03.2021", 45.50, lista)
    assert len(lista) == 3
    cheltuiala_modificata_1 = get_by_id(1, lista)
    assert get_suma(cheltuiala_modificata_1) == 195.50
    assert get_data(cheltuiala_modificata_1) == "12.03.2021"
    assert get_tipul(cheltuiala_modificata_1) == "alte cheltuieli"
    cheltuiala_modificata_2 = get_by_id(3, lista)
    assert get_suma(cheltuiala_modificata_2) == 134.95
    assert get_data(cheltuiala_modificata_2) == "12.03.2021"
    cheltuiala_nemodificata = get_by_id(2, lista)
    assert get_suma(cheltuiala_nemodificata) == 200
    assert get_data(cheltuiala_nemodificata) == "23.10.2021"


def test_cea_mai_mare_cheltuiala_dupa_tip():
    lista = []
    lista = adauga_cheltuiala(1, 13, 150, "12.03.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(2, 90, 200, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(3, 45, 89.45, "04.10.2021", "canal", lista)
    lista = adauga_cheltuiala(4, 87, 78.90, "07.12.2021", "canal", lista)
    lista = adauga_cheltuiala(5, 56, 567.78, "14.01.2020", "intretinere", lista)
    lista = adauga_cheltuiala(6, 17, 70, "31.12.2020", "alte cheltuieli", lista)

    rezultat = cea_mai_mare_cheltuiala_dupa_tip(lista)

    assert len(rezultat) == 3
    assert get_id(rezultat["canal"]) == 3
    assert get_id(rezultat["intretinere"]) == 5
    assert get_id(rezultat["alte cheltuieli"]) == 1


def test_ordonare_descrescator_cheltuieli_dupa_suma():
    lista = []
    lista = adauga_cheltuiala(1, 13, 150, "12.03.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(2, 90, 200, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(3, 45, 89.45, "04.10.2021", "canal", lista)

    lista = ordonare_descrescator_cheltuieli_dupa_suma(lista)
    assert lista[0] == [("id", 2), ("numar_apartament", 90), ("suma", 200),
                        ("data", "23.10.2021"), ("tipul", "intretinere")]
    assert lista[1] == [("id", 1), ("numar_apartament", 13), ("suma", 150),
                        ("data", "12.03.2021"), ("tipul", "alte cheltuieli")]
    assert lista[2] == [("id", 3), ("numar_apartament", 45), ("suma", 89.45),
                        ("data", "04.10.2021"), ("tipul", "canal")]


def test_get_luna_and_anul_from_data():
    assert get_luna_and_anul_from_data("12.03.2021") == "03.2021"
    assert get_luna_and_anul_from_data("04.10.2021") == "10.2021"


def test_sume_lunare_apartament():
    lista = []
    lista = adauga_cheltuiala(1, 13, 150, "12.03.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(2, 45, 200, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(3, 45, 89.45, "04.10.2021", "canal", lista)
    lista = adauga_cheltuiala(4, 45, 50, "04.03.2021", "canal", lista)

    rezultat = sume_lunare_apartament(lista)
    assert len(rezultat) == 2
    assert rezultat[13] == {"03.2021": 150}
    assert rezultat[45] == {"10.2021": 289.45, "03.2021": 50}
