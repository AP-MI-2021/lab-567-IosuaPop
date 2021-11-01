from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckIn
from Logic.CRUD import adaugaRezervare, getById, stergeRezervare, modificaRezervare


def testAdaugaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Londra", "economy", 100, "Da", lista)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getNume(getById("1", lista)) == "Londra"
    assert getClasa(getById("1", lista)) == "economy"
    assert getPret(getById("1", lista)) == 100
    assert getCheckIn(getById("1", lista)) == "Da"

def testStergeRezervare():
    lista = []
    lista = adaugaRezervare("1", "Londra", "economy", 105, "Nu", lista)
    lista = adaugaRezervare("2", "New York", "economy plus", 92, "Da", lista)

    lista = stergeRezervare("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

    try:
        lista = stergeRezervare("3", lista)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert getById("2", lista) is not None
    except Exception:
        assert False

def testModificaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Bucuresti", "business", 160, "Nu", lista)
    lista = adaugaRezervare("2", "Amsterdam", "economy plus", 200, "Nu", lista)

    lista = modificaRezervare("1", "Bucuresti", "economy plus", 140, "Nu", lista)

    rezervareUpdatata = getById("1", lista)
    assert getId(rezervareUpdatata) == "1"
    assert getNume(rezervareUpdatata) == "Bucuresti"
    assert getClasa(rezervareUpdatata) == "economy plus"
    assert getPret(rezervareUpdatata) == 140
    assert getCheckIn(rezervareUpdatata) == "Nu"

    rezervareNeupdatata = getById("2", lista)
    assert getId(rezervareNeupdatata) == "2"
    assert getNume(rezervareNeupdatata) == "Amsterdam"
    assert getClasa(rezervareNeupdatata) == "economy plus"
    assert getPret(rezervareNeupdatata) == 200
    assert getCheckIn(rezervareNeupdatata) == "Nu"

    lista = []
    lista = adaugaRezervare("1", "Canada", "business", 230, "Da", lista)

    try:
        lista = modificaRezervare("3", "Kiev", "economy", 290, "Nu", lista)
    except ValueError:
        rezervareNeupdatata = getById("1", lista)
        assert getId(rezervareNeupdatata) == "1"
        assert getNume(rezervareNeupdatata) == "Bucuresti"
        assert getClasa(rezervareNeupdatata) == "business"
        assert getPret(rezervareNeupdatata) == 160
        assert getCheckIn(rezervareNeupdatata) == "Nu"
    except Exception:
        assert False