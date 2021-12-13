from Domain.rezervare import toString
from Logic.CRUD import stergeRezervare, adaugaRezervare, modificaRezervare

def consola(lista):
    print("Operatiile vor fi a=add, sa=show all, d=delete, m=modifica, x=oprire/"
                  "fiecare operatie v-a fi separata prin ; iar valorile v-or/"
                  "fi separate prin ,/")
    print("exemplu: a;1,2,3,4,5;sa;d;1")
    comanda = input("Introduceti operatiile=")
    listaOperatii=(comanda.split(";"))
    for i in range(0,len(listaOperatii)):
        if listaOperatii[i]=='sa':
            showAll(lista)
        elif listaOperatii[i]=='a':
            if len(listaOperatii)>=i+1:
                listaAdaugare=listaOperatii[i+1].split(',')
                listaInt=[]
                for j in range(0,len(listaAdaugare)):
                    listaInt.append(int(listaAdaugare[j]))
                if len(listaInt) == 5:
                    id=listaInt[0]
                    nume=listaInt[1]
                    clasa=listaInt[2]
                    pret=float(listaInt[3])
                    checkIn=listaInt[4]
                    adaugaRezervare(id,nume,clasa,pret,checkIn,lista)
                else:
                    print("Nu se poate efectua operatia, nu sunt destule iteme de adaugat")
            else:
                print("Nu se poate efectua operatia, nu exista iteme de adaugat")
        elif listaOperatii[i] == 'd':
            if len(listaOperatii)>= i+1:
                stergeRezervare(int(listaOperatii[i+1]),lista)
            else:
                print("Nu se poate efectua operatia,nu exista id")
        elif listaOperatii[i] == 'm':
            if len(listaOperatii)>=i+1:
                listaModificare=listaOperatii[i+1].split(',')
                listaInt = []
                for j in range(0, len(listaModificare)):
                    listaInt[j] = int(listaModificare[j])
                if len(listaInt) == 5:
                    id=listaInt[0]
                    nume=listaInt[1]
                    clasa=listaInt[2]
                    pret=float(listaInt[3])
                    checkIn=listaInt[4]
                    modificaRezervare(id,nume,clasa,pret,checkIn,lista)
                else:
                    print("Nu se poate efectua operatia, nu exista destule iteme de modificat")
            else:
                print("Nu se poate efectua operatia, nu exista itemele de modificat")
        elif listaOperatii[i]== "x":
            break
        else:
            print("Operatie invalida!")
        i += 1
    return lista

def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))
lista=[]