"""
Scrieți un program pentru gestionarea unei asociații de proprietari. Vor fi suportate operațiile:
1.1. Adăugare / ștergere / modificare cheltuială: se efectuează pe bază de număr de apartament.
    O cheltuială conține număr apartament, suma, data (DD.MM.YYYY) și tipul: întreținere, canal, alte cheltuieli.
1.2. Ștergerea tuturor cheltuielilor pentru un apartament dat.
1.3. Adunarea unei valori la toate cheltuielile dintr-o dată citită.
1.4. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.
1.5. Ordonarea cheltuielilor descrescător după sumă.
1.6. Afișarea sumelor lunare pentru fiecare apartament.
1.7. Undo.
"""
from Tests.test_all import test_all
from UI.console import run_menu
from UI.console_line_command import run_new_menu


def main():
    test_all()
    lista = []
    while True:
        print("1. Consola normala.")
        print("2. Console line command.")
        print("x. Iesire.")
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            run_menu(lista)
        elif optiune == "2":
            run_new_menu(lista)
        elif optiune.lower() == "x":
            break
        else:
            print("Optiune gresita ! Reincercati ")


if __name__ == "__main__":
    main()
