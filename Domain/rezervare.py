def creeazaRezervare(id, nume, clasa, pret, checkIn):
    '''
    creaza un dictiionar ce reprezinta o rezervare
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkIn: string
    :return: un dictionar ce contine o rezervare
    '''
    return {
        "id": id,
        "nume": nume,
        "descriere": clasa,
        "pret": pret,
        "checkIn": checkIn,
    }

def getId(rezervare):
    '''
    da id-ul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: id-ul rezervarii
    '''
    return rezervare["id"]

def getNume(rezervare):
    return rezervare["nume"]

def getClasa(rezervare):
    return rezervare["clasa"]

def getPret(rezervare):
    return rezervare["pret"]

def getCheckIn(rezervare):
    return rezervare["checkIn"]

def toString(rezervare):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, CheckIn: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckIn(rezervare)
    )