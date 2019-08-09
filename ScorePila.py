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



class PilaScore:
    def __init__(self):
        self.primero=None
        self.ultimo=None

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

    def render(self,window):
        temp=self.primero
        prob=randint(1, 4)

        while temp != None:
            window.addstr(x, y, '*')
            temp=temp.siguiente




    def Graficarpila(self):
        file = open("PilaScore.dot", "w")
        file.write("digraph G{ rankdir=LR;\n")
        file.write("node [shape= record, width=.1,height=.1];\n")
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
        file.write("}")
        file.close()
        os.system("dot -Tpng PilaScore.dot -o PilaScore.png")
        os.system(" PilaScore.png")
