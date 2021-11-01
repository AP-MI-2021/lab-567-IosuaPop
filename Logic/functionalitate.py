from Domain.rezervare import getNume, creeazaRezervare, getId, getClasa, getPret, getCheckIn

def procentRedus(pret,procentaj):
    procentajPret=pret*procentaj/100
    return procentajPret

def reducerePret(procentaj, lista):
    """
    reduce pretul ale rezervarilor ale caror nume contin un string dat
    :param procentaj:  procentul ce se reduce din pret
    :param lista: lista de rezervari
    :return: lista in care rezervarile ale caror nume contin stringul dat s-au modificat
    """
    if procentaj < 0:
        raise ValueError("Procentajul ce se reduce din pret trebuie sa fie pozitiv!")
    if procentaj > 100:
        raise ValueError("Procentajul ce se reduce din pret trebuie sa fie mai mic sau egal cu 100!")
    listaNoua = []
    for rezervare in lista:
        if getCheckIn(rezervare) =="Da":
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                getClasa(rezervare),
                getPret(rezervare) - procentRedus(getPret(rezervare),procentaj),
                getCheckIn(rezervare)
            )
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua

def trecereRezervariPeUnNume(nume, lista):
    '''
    :param nume:
    :param lista:
    :return:
    '''
    listaNoua = []
    for rezervare in lista:
        if getNume(rezervare) != nume:
            rezervareNoua=(getId(rezervare), nume, getClasa(rezervare), getPret(rezervare), getPret(rezervare))
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua

def pretMaxperClasa(lista):
    '''
    :param lista:
    :return:
    '''
    rezultat = {'economy':0, 'economy plus':0, 'business':0}
    for rezervare in lista:
        pret = getPret(rezervare)
        clasa = getClasa(rezervare)
        if pret > rezultat[clasa]:
            rezultat[clasa] = pret
    return rezultat

def ordonareDupaPretDescrescator(lista):
    '''
    :param lista:
    :return:
    '''
    return sorted(lista, key=lambda rezervare: getPret(rezervare), reverse=True)

def sumaPreturiPerNume(lista):
    '''
    :param lista:
    :return:
    '''
    rezultat = {}
    for rezervare in lista:
        nume = getNume(rezervare)
        pret = getPret(rezervare)
        if nume in rezultat:
            rezultat[nume] = rezultat[nume] + pret
        else:
            rezultat[nume] = pret
    return rezultat
