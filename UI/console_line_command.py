from Domain.cheltuiala import to_string
from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala


def print_meniu():
    print("Comenzile introduse trebuie separate prin ;, acestea putand fi: \n"
          "Adaugare: add,id,numar apartament,suma,data,tipul \n"
          "Stergere: delete,id-ul cheltuielii de sters \n"
          "Afisare: showall \n"
          "Atentie !!! Comenzile trebuie introduse exact ca in modelul de mai sus !")


def run_new_menu(lista):
    while True:
        print_meniu()
        comenzi = input("Introduceti comenzile: ").split(";")
        for i in range(len(comenzi)):
            com = comenzi[i].split(",")
            if com[0] == "add":
                try:
                    lista = adauga_cheltuiala(com[1], com[2], com[3], com[4], com[5], lista)
                except Exception as e:
                    print(f"Eroare: {e}")
            elif com[0] == "delete":
                try:
                    lista = sterge_cheltuiala(com[1], lista)
                except ValueError as ve:
                    print(f"Eroare: {ve}")
            elif com[0] == "showall":
                for cheltuiala in lista:
                    print(to_string(cheltuiala))
            else:
                print("Reincerti ! Comenzi introduse gresit")
