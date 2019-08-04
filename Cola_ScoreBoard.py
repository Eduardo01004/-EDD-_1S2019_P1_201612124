import os

class NodoCola:
    def __init__(self, nombre=None, punteo=None, siguiente=None):
        self.nombre=nombre
        self.punteo=punteo
        self.siguiente=siguiente
class ColaScore:
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def IngresarCola(self,nombre,punteo):
        tope=0
        nuevo=NodoCola(nombre,punteo)
        if self.primero==None:
            self.primero=nuevo
            self.primero.siguiente=None
            self.ultimo=self.primero
        else:
            self.ultimo.siguiente=nuevo
            nuevo.siguiente=None
            self.ultimo=nuevo

    def recorrerCola(self):
        aux=self.primero
        contador=0
        while(aux!=None):
            contador++

            aux=aux.siguiente
    



    def eliminar(self):
        aux=self.primero
        if aux==None:
            print("No hay datos en la cola")
        else:
            self.primero=aux.siguiente


    def GraficarCola(self):
        file = open("ColaScore.dot", "w")
        file.write("digraph G{ rankdir=LR;\n")
        aux=self.primero
        if self.primero!=None:
            while (aux!=None):
                c=str(hash(aux))
                ca=str(hash(aux.siguiente))
                if aux.siguiente!=None:
                    file.write(c +"[shape=record, style=filled, fillcolor=seashell2,label=\"("+aux.nombre+","+str(aux.punteo) + ")\"];\n")
                    file.write(c + "->" + ca+"\n")
                else:
                    c=str(hash(aux))
                    file.write(c +"[shape=record, style=filled, fillcolor=seashell2,label=\"("+aux.nombre+","+str(aux.punteo) + ")\"];\n")
                    file.write("null"+"[shape=record, style=filled, fillcolor=seashell2,label=\"NULL" + "\"];\n")
                    file.write(c + "->" + "null"+"[ color=\"blue\"]\n")

                aux=aux.siguiente
        file.write("}")
        file.close()
        os.system("dot -Tpng ColaScore.dot -o ColaScore.png")
        os.system(" ColaScore.png")
