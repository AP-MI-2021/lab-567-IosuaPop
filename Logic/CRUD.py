from Domain.cheltuiala import creeaza_cheltuiala, get_numar_apartament, get_id


def adauga_cheltuiala(id, numar_apartament, suma, data, tipul, lista, undo_list=None, redo_list=None):
    """
    Adauga o cheltuiala intr-o lista
    :param redo_list: lista pentru redo care e resetata
    :param undo_list: lista pentru undo care salveaza starea listei inainte de adaugare
    :param lista: lista de cheltuieli
    :param id: int
    :param numar_apartament: string
    :param suma: float
    :param data: string
    :param tipul: string
    :return: o lista continand atat elemente vechi, cat si noua cheltuiala
    """
    if get_by_id(id, lista) is not None:
        raise ValueError("Id-ul exista deja !")
    if tipul not in ["intretinere", "canal", "alte cheltuieli"]:
        raise ValueError("Tipul cheltuielii trebuie sa fie intretinere / canal / alte cheltuieli")
    if undo_list is not None and redo_list is not None:
        undo_list.append(lista)
        redo_list.clear()
    cheltuiala = creeaza_cheltuiala(id, numar_apartament, suma, data, tipul)
    return lista + [cheltuiala]


def get_by_id(id, lista):
    """
    Gaseste o cheltuiala cu id-ul dat intr-o lista
    :param id: id-ul cheltuielii
    :param lista: lista de cheltuieli
    :return: cheltuiala cu id-ul dat din lista, sau None daca aceasta nu exista
    """
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            return cheltuiala
    return None


def get_by_numar_apartament(numar_apartament, lista):
    """
    Gaseste o cheltuiala cu numarul de apartament dat intr-o lista
    :param numar_apartament: numarul de apartament al cheltuielii
    :param lista: lista de cheltuieli
    :return: cheltuiala cu numarul de apartament dat din lista, sau None in caz contrar
    """
    lista_noua = []
    for cheltuiala in lista:
        if get_numar_apartament(cheltuiala) == numar_apartament:
            lista_noua.append(cheltuiala)
    return lista_noua


def sterge_cheltuiala(id, lista, undo_list=None, redo_list=None):
    """
    Sterge un apartament cu id-ul dat
    :param redo_list: lista pentru redo care e resetata
    :param undo_list: lista pentru undo care salveaza starea listei inainte de stergere
    :param id: id-ul apartamentului care se va sterge
    :param lista: lista de cheltuieli
    :return: o lista de cheltuieli fara cheltuiala care are numarul apartamentului dat
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu id-ul dat !")
    if undo_list is not None and redo_list is not None:
        undo_list.append(lista)
        redo_list.clear()
    rezultat = []
    for cheltuiala in lista:
        if get_id(cheltuiala) != id:
            rezultat.append(cheltuiala)
    return rezultat


def modifica_cheltuiala(id, numar_apartament, suma, data, tipul, lista,  undo_list=None, redo_list=None):
    """
    Modifica o cheltuiala cu id-ul dat
    :param redo_list: lista pentru redo care e resetata
    :param undo_list: lista pentru undo care salveaza lista inainte de modificare
    :param id: id-ul cheltuielii
    :param numar_apartament: numarul de apartament al cheltuielii
    :param suma: suma cheltuielii
    :param data: data cheltuielii
    :param tipul: tipul cheltuielii
    :param lista: lista cu cheltuieli
    :return: lista modificata
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu id-ul dat !")
    if undo_list is not None and redo_list is not None:
        undo_list.append(lista)
        redo_list.clear()
    lista_noua = []
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            cheltuiala_noua = creeaza_cheltuiala(id, numar_apartament, suma, data, tipul)
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)
    return lista_noua
