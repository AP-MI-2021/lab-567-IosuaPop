from Domain.rezervare import toString
from Logic.CRUD import stergeRezervare, adaugaRezervare, modificaRezervare

def consola(lista):
    print("Operatiile vor fi a=add, sa=show all, d=delete, m=modifica/"
                  "fiecare operatie v-a fi separata printr-o ; iar valorile v-or/"
                  "fi separate prin virgule/")
    comanda = input("Introduceti operatiile=")
    listaOperatii=(comanda.split(";"))
    i=1
    for i in range(len(listaOperatii)):
        if listaOperatii[i]=='sa':
            showAll(lista)
        elif listaOperatii[i]=='a':
            if len(listaOperatii)>=i+2:
                listaAdaugare=listaOperatii[i+1].split(',')
                if len(listaOperatii) >= i+6:
                    id=listaAdaugare[1]
                    nume=listaAdaugare[2]
                    clasa=listaAdaugare[3]
                    pret=float(listaAdaugare[4])
                    checkIn=listaAdaugare[5]
                    adaugaRezervare(id,nume,clasa,pret,checkIn,lista)
                else:
                    print("Nu se poate efectua operatia")
            else:
                print("Nu se poate efectua operatia")
            i += 1
        elif listaOperatii[i] == 'd':
            if len(listaOperatii)>= i+2:
                stergeRezervare(listaOperatii[i+1],lista)
            else:
                print("Nu se poate efectua operatia")
            i+=1
        elif listaOperatii[i] == 'm':
            if len(listaOperatii)>=i+2:
                listaModificare=listaOperatii[i+1].split(',')
                if len(listaOperatii) >= i+6:
                    id=listaModificare[1]
                    nume=listaModificare[2]
                    clasa=listaModificare[3]
                    pret=float(listaModificare[4])
                    checkIn=listaModificare[5]
                    modificaRezervare(id,nume,clasa,pret,checkIn,lista)
                else:
                    print("Nu se poate efectua operatia")
            else:
                print("Nu se poate efectua operatia")
            i+=1
        else:
            print("Operatie invalida")
    return lista

def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))