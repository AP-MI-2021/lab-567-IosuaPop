from Domain.cheltuiala import get_numar_apartament, get_suma, get_data, get_tipul, get_id
from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala, get_by_id, get_by_numar_apartament


def test_adauga_cheltuiala():
    lista = []
    lista = adauga_cheltuiala(1, 23, 230, "04.09.2021", "intretinere", lista)

    assert len(lista) == 1
    assert get_id(get_by_id(1, lista)) == 1
    assert get_numar_apartament(get_by_id(1, lista)) == 23
    assert get_suma(get_by_id(1, lista)) == 230
    assert get_data(get_by_id(1, lista)) == "04.09.2021"
    assert get_tipul(get_by_id(1, lista)) == "intretinere"


def test_sterge_cheltuiala():
    lista = []
    lista = adauga_cheltuiala(1, 13, 150, "06.10.2021", "canal", lista)
    lista = adauga_cheltuiala(2, 45, 200, "23.10.2021", "intretinere", lista)

    lista = sterge_cheltuiala(1, lista)

    assert len(lista) == 1
    assert get_by_id(1, lista) is None
    assert get_by_id(2, lista) is not None


def test_modifica_cheltuiala():
    lista = []
    lista = adauga_cheltuiala(1, "1", 234, "12.02.2021", "canal", lista)
    lista = adauga_cheltuiala(2, "23", 120, "23.10.2021", "alte cheltuieli", lista)

    lista = modifica_cheltuiala(2, "23", 230, "04.10.2021", "intretinere", lista)

    assert len(lista) == 2
    cheltuiala_modificata = get_by_id(2, lista)
    assert get_suma(cheltuiala_modificata) == 230
    assert get_data(cheltuiala_modificata) == "04.10.2021"
    assert get_tipul(cheltuiala_modificata) == "intretinere"
    cheltuiala_nemodificata = get_by_id(1, lista)
    assert get_suma(cheltuiala_nemodificata) == 234
    assert get_data(cheltuiala_nemodificata) == "12.02.2021"
    assert get_tipul(cheltuiala_nemodificata) == "canal"


def test_get_by_id():
    lista = []
    lista = adauga_cheltuiala(1, 13, 150, "06.10.2021", "canal", lista)
    lista = adauga_cheltuiala(2, 45, 200, "23.10.2021", "intretinere", lista)

    assert get_by_id(1, lista) == [("id", 1), ("numar_apartament", 13), ("suma", 150), ("data", "06.10.2021"),
                                   ("tipul", "canal")]
    assert get_by_id(2, lista) == [("id", 2), ("numar_apartament", 45), ("suma", 200), ("data", "23.10.2021"),
                                   ("tipul", "intretinere")]
    assert get_by_id(5, lista) is None


def test_get_by_numar_apartament():
    lista = []
    lista = adauga_cheltuiala(1, 13, 150, "06.10.2021", "canal", lista)
    lista = adauga_cheltuiala(2, 45, 200, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(3, 45, 89.45, "12.03.2021", "canal", lista)

    assert get_by_numar_apartament(45, lista) == [[("id", 2), ("numar_apartament", 45), ("suma", 200),
                                                   ("data", "23.10.2021"),  ("tipul", "intretinere")], [("id", 3),
                                                  ("numar_apartament", 45), ("suma", 89.45), ("data", "12.03.2021"),
                                                  ("tipul", "canal")]]
    assert get_by_numar_apartament(13, lista) == [[("id", 1), ("numar_apartament", 13), ("suma", 150),
                                                   ("data", "06.10.2021"), ("tipul", "canal")]]
    assert get_by_numar_apartament(4, lista) == []
