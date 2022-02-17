from Domain.cheltuiala import creeaza_cheltuiala, get_numar_apartament, get_suma, get_data, get_tipul, get_id


def test_cheltuiala():
    cheltuiala = creeaza_cheltuiala(1, "23", 200, "12.03.2021", "canal")
    assert get_id(cheltuiala) == 1
    assert get_numar_apartament(cheltuiala) == "23"
    assert get_suma(cheltuiala) == 200.0
    assert get_data(cheltuiala) == "12.03.2021"
    assert get_tipul(cheltuiala) == "canal"
