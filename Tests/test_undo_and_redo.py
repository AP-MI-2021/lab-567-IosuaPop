from Logic.CRUD import adauga_cheltuiala, get_by_id
from UI.console import ui_redo, ui_undo


def test_undo_and_redo():
    # lista goala
    lista = []
    undo_list = []
    redo_list = []

    # adaugam o cheltuiala
    lista = adauga_cheltuiala(1, 20, 200, "12.12.2021", "canal", lista, undo_list, redo_list)
    assert len(lista) == 1
    # adaugam o cheltuiala
    lista = adauga_cheltuiala(2, 34, 89.50, "08.05.2021", "intretinere", lista, undo_list, redo_list)
    assert len(lista) == 2
    # adaugam o cheltuiala
    lista = adauga_cheltuiala(3, 80, 56.78, "29.03.2021", "alte cheltuieli", lista, undo_list, redo_list)
    assert len(lista) == 3

    # undo
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(3, lista) is None
    assert get_by_id(2, lista) is not None
    assert get_by_id(1, lista) is not None

    # undo
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id(2, lista) is None
    assert get_by_id(1, lista) is not None

    # undo
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert get_by_id(1, lista) is None

    # undo
    assert len(lista) == 0

    # adaugam 3 cheltuieli
    lista = adauga_cheltuiala(1, 90, 100, "14.04.2021", "intretinere", lista, undo_list, redo_list)
    lista = adauga_cheltuiala(2, 45, 250, "20.03.2021", "canal", lista, undo_list, redo_list)
    lista = adauga_cheltuiala(3, 30, 345.66, "05.12.2021", "alte cheltuieli", lista, undo_list, redo_list)
    assert len(lista) == 3

    # redo
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is not None
    assert get_by_id(3, lista) is not None

    # undo undo
    lista = ui_undo(lista, undo_list, redo_list)
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id(2, lista) is None
    assert get_by_id(3, lista) is None
    assert get_by_id(1, lista) is not None

    # redo
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(3, lista) is None
    assert get_by_id(2, lista) is not None
    assert get_by_id(1, lista) is not None

    # redo
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is not None
    assert get_by_id(3, lista) is not None

    # undo undo
    lista = ui_undo(lista, undo_list, redo_list)
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id(3, lista) is None
    assert get_by_id(2, lista) is None
    assert get_by_id(1, lista) is not None

    # adaugam o cheltuiala
    lista = adauga_cheltuiala(4, 30, 400, "15.05.2021", "alte cheltuieli", lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is None
    assert get_by_id(3, lista) is None
    assert get_by_id(4, lista) is not None

    # redo
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is None
    assert get_by_id(3, lista) is None
    assert get_by_id(4, lista) is not None

    # undo
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id(1, lista) is not None
    assert get_by_id(4, lista) is None

    # undo
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert get_by_id(1, lista) is None

    # redo redo
    lista = ui_redo(lista, undo_list, redo_list)
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(1, lista) is not None
    assert get_by_id(4, lista) is not None

    # redo
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(1, lista) is not None
    assert get_by_id(4, lista) is not None
    assert get_by_id(2, lista) is None
    assert get_by_id(3, lista) is None
