import os
from random import randint

class NodoPila:
    def __init__(self,coorx=None,coory=None,siguiente=None):
        self.coorx=coorx
        self.coory=coory
        self.siguiente=siguiente
        self.x = randint(1, 33)
        self.y = randint(1, 18)

    def __str__(self):
        return " %s %s" %(self.coorx,self.coory)
class NodoPila2:
    def __init__(self,coorx2=None,coory2=None,siguiente2=None):
        self.coorx2=coorx2
        self.coory2=coory2
        self.siguiente2=siguiente2
        self.x2 = randint(1, 33)
        self.y2 = randint(1, 18)



class PilaScore:
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.primero2=None
        self.ultimo2=None


    def InsertarScore(self, coorx, coory):
        nuevo=NodoPila(coorx,coory)

        if self.primero==None:
            self.primero=nuevo
            nuevo.siguiente=None
            self.ultimo=self.primero

        else:
            nuevo.siguiente=self.primero
            self.primero=nuevo

    def Pop(self):
        temporal=self.primero
        if self.primero==None:
            print("No hay datos en la pila")
        else:
            self.primero=temporal.siguiente
    #------------PILA2-------------------------------
    def InsertarScore2(self, coorx, coory):
        nuevo=NodoPila2(coorx,coory)
        if self.primero2==None:
            self.primero2=nuevo
            nuevo.siguiente2=None
            self.ultimo2=self.primero2

        else:
            nuevo.siguiente2=self.primero2
            self.primero2=nuevo

    def Pop2(self):
        temporal=self.primero2
        if self.primero2==None:
            print("No hay datos en la pila")
        else:
            self.primero2=temporal.siguiente2



    def Graficarpila(self):
        file = open("PilaScore.dot", "w")
        file.write("digraph G{ rankdir=LR;\n")
        file.write("node [shape= record, width=.1,height=.1];\n")
        file.write(" subgraph cluster1{\nlabel=\"PIlA NIVEL1\";\n")
        file.write("nodeTable [label = \" ")
        aux=self.primero
        if self.primero!=None:
            while (aux!=None):
                if aux.siguiente!=None:
                    file.write("|"+"("+str(aux.coorx)+","+str(aux.coory)+")")
                else:
                    c=str(hash(aux))
                    file.write("|"+"("+str(aux.coorx)+","+str(aux.coory)+")")
                aux=aux.siguiente
        file.write("\"];\n")
        file.write("}\n")

        #----------------------PILA 2++--------------------
        file.write(" subgraph cluster2{\nlabel=\"PIlA NIVEL2\";\n")
        file.write("nodeTable2 [label = \" ")
        aux2=self.primero2
        if self.primero2!=None:
            while (aux2!=None):
                if aux2.siguiente2!=None:
                    file.write("|"+"("+str(aux2.coorx2)+","+str(aux2.coory2)+")")

                else:
                    c2=str(hash(aux2))
                    file.write("|"+"("+str(aux2.coorx2)+","+str(aux2.coory2)+")")
                aux2=aux2.siguiente2
        file.write("\"];\n")
        file.write("}\n}\n")
        file.close()
        os.system("dot -Tpng PilaScore.dot -o PilaScore.png")
        os.system(" PilaScore.png")
