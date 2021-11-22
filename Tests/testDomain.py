from Domain.rezervare import creeazaRezervare, getId, getNume, getClasa, getPret, getCheckIn


def testRezervare():
    rezervare = creeazaRezervare("1", "Cluj", "economy", 80, "Da")

    assert getId(rezervare) == "1"
    assert getNume(rezervare) == "Cluj"
    assert getClasa(rezervare) == "economy"
    assert getPret(rezervare) == 80
    assert getCheckIn(rezervare) == "Da"