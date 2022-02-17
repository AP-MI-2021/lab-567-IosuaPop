def creeaza_cheltuiala(id, numar_apartament, suma, data, tipul):
    """
    Creeaza o lista ce reprezinta o cheltuiala
    :param id: id-ul cheltuielii (int)
    :param numar_apartament: string
    :param suma: float
    :param data: date
    :param tipul: string
    :return: o lista ce contine o cheltuiala
    """
    return [("id", id), ("numar_apartament", numar_apartament), ("suma", suma),
            ("data", data), ("tipul", tipul)]


def get_id(cheltuiala):
    """
    Returneaza id-ul cheltuielii
    :param cheltuiala: cheltuiala careia vrem sa-i aflam id-ul
    :return: id-ul cheltuielii
    """
    return cheltuiala[0][1]


def get_numar_apartament(cheltuiala):
    """
    Returneaza numarul apartamentului unei cheltuieli
    :param cheltuiala: cheltuiala careia vrem sa-i aflam numarul de apartament
    :return: numarul apartamentului cheltuielii
    """
    return cheltuiala[1][1]


def get_suma(cheltuiala):
    """
    Returneaza suma cheltuielii
    :param cheltuiala: cheltuiala careia vrem sa-i aflam suma
    :return: suma cheltuielii
    """
    return float(cheltuiala[2][1])


def get_data(cheltuiala):
    """
    Returneaza data cheltuielii
    :param cheltuiala: cheltuiala careia vrem sa-i aflam data
    :return: data cheltuielii
    """
    return cheltuiala[3][1]


def get_tipul(cheltuiala):
    """
    Returneaza tipul cheltuielii
    :param cheltuiala: dcheltuiala careia vrem sa-i aflam tipul
    :return: tipul cheltuielii
    """
    return cheltuiala[4][1]


def to_string(cheltuiala):
    """
    Returneaza cheltuiala ca string
    :param cheltuiala: cheltuiala careia vrem sa-i aflam datele
    :return: cheltuiala ca string
    """
    return f"Id: {get_id(cheltuiala)}; Numar apartament: {get_numar_apartament(cheltuiala)}; " \
           f"Suma: {get_suma(cheltuiala)}; Data: {get_data(cheltuiala)}; Tipul: {get_tipul(cheltuiala)}"
