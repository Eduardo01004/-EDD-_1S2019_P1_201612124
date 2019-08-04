import os

class NodoDoble:

    def __init__(self, coorx=None, coory=None, siguiente=None, atras=None):
        self.coorx=coorx
        self.coory=coory
        self.siguiente=siguiente
        self.atras=atras

    def __str__(self):
        return "%s %s" %(self.coorx, self.coory)


class ListaDoble:
    def __init__(self):
        self.primero=None
        self.ultimo=None


    def Insertar(self,coorx,coory):
        nuevo=NodoDoble(coorx,coory)
        if self.primero==None:
            self.primero=nuevo
            self.primero.siguiente=None
            self.primero.atras=None
            self.ultimo=nuevo
        else:
            self.ultimo.siguiente=nuevo
            nuevo.siguiente=None
            nuevo.atras=self.ultimo
            self.ultimo=nuevo

    def Listar(self):
        actual=self.primero
        while actual != None:
            print("********")
            print(actual)
            actual=actual.siguiente


    def GraficarDobleSnake(self):
        file = open("ListaDobleSnake.dot", "w")

        file.write("digraph G {rankdir = \"LR\"; \n subgraph cluster3{\nlabel=\"Snake\";\n")
        snake=self.primero
        aux=snake.atras
        if self.primero!=None:
            d=str(hash(aux))
            c=str(hash(snake))
            file.write(d +"[shape=record, style=filled, fillcolor=seashell2,label=\"NULL" + "\"];\n")
            file.write(c +"[shape=record, style=filled, fillcolor=seashell2,label=\"("+str(snake.coorx)+","+str(snake.coory) + ")\"];\n")
            file.write(d + "->" + c+"[dir=back color=\"blue\"]\n")

            while(snake!=None):
                aux2=snake.siguiente
                if snake!=self.ultimo:
                    c=str(hash(snake))
                    ca=str(hash(aux2))
                    file.write(c +"[shape=record, style=filled, fillcolor=seashell2,label=\"("+str(snake.coorx)+","+str(snake.coory) + ")\"];\n")
                    file.write(c + "->" + ca+"\n")
                    file.write(ca + "->" + c+"\n")

                elif snake==self.primero or snake==self.ultimo :
                    c=str(hash(snake))
                    file.write(c +"[shape=record, style=filled, fillcolor=seashell2,label=\"("+str(snake.coorx)+","+str(snake.coory) + ")\"];\n")
                    file.write("null"+"[shape=record, style=filled, fillcolor=seashell2,label=\"NULL" + "\"];\n")
                    file.write(c + "->" + "null"+"[ color=\"blue\"]\n")


                snake=snake.siguiente
        file.write("}\n}\n")
        file.close()
        os.system("dot -Tpng ListaDobleSnake.dot -o ListaDobleSnake.png")
        os.system(" ListaDobleSnake.png")
