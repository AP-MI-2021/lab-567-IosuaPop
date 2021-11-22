from Domain.rezervare import creeazaRezervare, getId


def adaugaRezervare(id, nume, clasa, pret, checkIn, lista):
    '''
    adauga o rezervare intr-o lista
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkIn: string
    :param lista: lista de rezervari
    :return: o lista continand atat elementele vechi, cat si noua rezervare
    '''
    ec = "economy"
    ecp = "economy plus"
    bs = "business"
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    if clasa != ec or clasa != ecp or clasa != bs:
        raise ValueError("Clasa de zbor poate fi doar: economy, economy plus sau business!")
    if checkIn !="da" or checkIn != "nu":
        raise ValueError("Checkin-ul poate fi doar Da sau Nu")
    rezervare = creeazaRezervare(id, nume, clasa, pret, checkIn)
    return lista + [rezervare]

def getById(id, lista):
    '''
    gaseste o rezervare cu id-ul dat intr-o lista
    :param id: string
    :param lista: lista de rezervari
    :return: rezervarea cu id-ul dat din lista sau None, daca aceasta nu exista
    '''
    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None

def stergeRezervare(id, lista):
    """
    sterge o rezervare cu id-ul dat din lista
    :param id: id-ul rezervarii care se va sterge
    :param lista: lista de rezervari
    :return: o lista de rezervari fara elementul cu id-ul dat
    """
    if getById(id, lista) is None:
        raise ValueError("Nu exista o rezervare cu id-ul dat!")
    return [rezervare for rezervare in lista if getId(rezervare) != id]

def modificaRezervare(id, nume, clasa, pret, checkIn, lista):
    """
    modifica a rezervare cu id-ul dat
    :param id: id-ul rezervarii
    :param nume: numele rezervarii
    :param clasa: clasa rezervarii
    :param pret: pretul rezervarii
    :param checkIn: da/nu(daca s-a facut)
    :param lista: O lista de rezervari.
    :return: lista modificata.
    """
    if getById(id, lista) is None:
        raise ValueError("Nu exista o rezervare cu id-ul dat!")
    listaNoua = []
    for rezervare in lista:
        if getId(rezervare) == id:
            rezervareNoua = creeazaRezervare(id, nume, clasa, pret, checkIn)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua