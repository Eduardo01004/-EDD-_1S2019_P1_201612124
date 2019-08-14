import os

class NodoDobleCircular:
     def __init__(self, nombre=None, siguiente=None, anterior=None):
        self.nombre=nombre
        self.siguiente=siguiente
        self.anterior=anterior

     def __str__(self):
        return "%s " %( self.nombre)



class ListaCircularDobleUsuarios:
    def __init__(self):
        self.primero=None
        self.ultimo=None


    def InsertarUsuario(self,nombre):
        nuevo=NodoDobleCircular(nombre)
        if self.primero==None:
            self.primero=nuevo
            self.ultimo=nuevo
            self.primero.siguiente=self.primero
            self.primero.anterior=self.ultimo
        else:
            self.ultimo.siguiente=nuevo
            nuevo.anterior=self.ultimo
            nuevo.siguiente=self.primero
            self.ultimo=nuevo
            self.primero.anterior=self.ultimo


    def Listar(self):
        validar=True
        temp=self.primero
        while(validar):
            print(temp)
            if temp==self.ultimo:
                validar=False
            else:
                temp=temp.siguiente

    def GraficarUsuarios(self):
        file = open("ListaDobleCircularUsuarios.dot", "w")
        file.write("digraph CircularList {rankdir=LR;\n\n")
        usuario=self.primero
        validar=True
        if self.primero!=None:
            while (validar):
                c=str(hash(usuario))
                ca=str(hash(usuario.siguiente))

                file.write(c +"[fillcolor=seashell2,label=\""+str(usuario.nombre) +"\"];\n")
                file.write(c + "->" + ca+"\n")
                file.write(ca + "->" + c+"\n")


                if usuario==self.ultimo:
                    validar=False
                else:
                    usuario=usuario.siguiente

        file.write("}")
        file.close()
        os.system("dot -Tpng ListaDobleCircularUsuarios.dot -o ListaDobleCircularUsuarios.png")
        os.system("ListaDobleCircularUsuarios.png")
