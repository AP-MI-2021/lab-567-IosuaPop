

from Domain.cheltuiala import get_numar_apartament, get_data, get_suma, creeaza_cheltuiala, get_id, get_tipul


def sterge_toate_cheltuielile_apartament(numar_aparatament, lista, undo_list=None, redo_list=None):
    """
    Ștergerea tuturor cheltuielilor pentru un apartament dat.
    :param redo_list: lista pentru redo care e resetata
    :param undo_list: lista pentru undo care salveaza lista inainte de modificare
    :param numar_aparatament: numarul de apartament pentru care dorim sa stergem toate cheltuielile
    :param lista: lista de cheltuieli
    :return: lista de cheltuieli fara cele pentru numarul de apartament specificat
    """
    if numar_aparatament < 0:
        raise ValueError("Numarul apartamentului nu poate fi negativ !")
    if undo_list is not None and redo_list is not None:
        undo_list.append(lista)
        redo_list.clear()
    rezultat = []
    for cheltuiala in lista:
        if get_numar_apartament(cheltuiala) != numar_aparatament:
            rezultat.append(cheltuiala)
    return rezultat


def adauga_valoare_data(data_string, valoare, lista, undo_list=None, redo_list=None):
    """
    Adunarea unei valori la toate cheltuielile dintr-o dată citită.
    :param redo_list: lista pentru redo care e resetata
    :param undo_list: lista pentru undo care salveaza lista inainte de modificare
    :param valoare: valoarea care se adauga sumei
    :param data_string: data pentru care se va adauga o valoare
    :param lista: lista de cheltuieli
    :return: lista in care cheltuielile cu data introdusa au valoarea adaugata sumei
    """
    if valoare < 0:
        raise ValueError("Nu se poate adauga o valoare negativa !")
    if undo_list is not None and redo_list is not None:
        undo_list.append(lista)
        redo_list.clear()
    rezultat = []
    for cheltuiala in lista:
        if get_data(cheltuiala) == data_string:
            cheltuiala_noua = creeaza_cheltuiala(get_id(cheltuiala), get_numar_apartament(cheltuiala),
                                                 float(get_suma(cheltuiala)) + valoare, get_data(cheltuiala),
                                                 get_tipul(cheltuiala))
            rezultat.append(cheltuiala_noua)
        else:
            rezultat.append(cheltuiala)
    return rezultat


def cea_mai_mare_cheltuiala_dupa_tip(lista):
    """
    Determina cea mai mare cheltuiala pentru fiecare tip de cheltuială
    :param lista: lista de chetuieli
    :return: cea mai mare chetuiala pentru fiecare tip de cheltuiala
    """
    rezultat = {}
    for cheltuiala in lista:
        tipul = get_tipul(cheltuiala)
        suma = get_suma(cheltuiala)
        if tipul in rezultat:
            if suma > get_suma(rezultat[tipul]):
                rezultat[tipul] = cheltuiala
        else:
            rezultat[tipul] = cheltuiala
    return rezultat


def ordonare_descrescator_cheltuieli_dupa_suma(lista, undo_list=None, redo_list=None):
    """
    Ordoneaza cheltuielile descrescător după sumă.
    :param redo_list: lista pentru redo care e resetata
    :param undo_list: lista pentru undo care salveaza lista inainte de modicare
    :param lista: lista de cheltuieli
    :return: lista de cheltuieli ordonata descrescator dupa suma
    """
    if undo_list is not None and redo_list is not None:
        undo_list.append(lista)
        redo_list.clear()
    return sorted(lista, key=lambda cheltuiala: get_suma(cheltuiala), reverse=True)


def get_luna_and_anul_from_data(data):
    """
    Determina luna (format MM.YYYY) din data ( format DD.MM.YYYY)
    :param data: data in format DD.MM.YYYY
    :return: luna si anul din data in format MM.YYYY
    """
    return data[3:]


def sume_lunare_apartament(lista):
    """
    Determina sumele lunare pentru fiecare apartament
    :param lista: lista de cheltuieli
    :return: un nested dictionary cu sumele lunare pentru fiecare apartament
    """
    apartament = {}
    for cheltuiala in lista:
        numar_apartament = get_numar_apartament(cheltuiala)
        luna = get_luna_and_anul_from_data(get_data(cheltuiala))
        suma = get_suma(cheltuiala)
        if numar_apartament in apartament:
            if luna in apartament[numar_apartament]:
                apartament[numar_apartament][luna] += suma
            else:
                apartament[numar_apartament][luna] = suma
        else:
            apartament[numar_apartament] = {}
            apartament[numar_apartament][luna] = suma
    return apartament
