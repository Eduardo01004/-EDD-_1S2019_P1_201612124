import os
import curses
from ScorePila import PilaScore
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint
WIDTH = 35
HEIGHT = 20
MAX_X = WIDTH - 2
MAX_Y = HEIGHT - 2
TIMEOUT = 100
p=PilaScore()
class NodoDoble:

    def __init__(self, coorx, coory):
        self.coorx=coorx
        self.coory=coory
        self.siguiente=None
        self.atras=None

    def __str__(self):
        return "%s %s" %(self.coorx, self.coory)


class ListaDoble:
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.punteo=0
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)
        self.x2 = randint(1, MAX_X)
        self.y2 = randint(1, MAX_Y)
        self.tiempo=TIMEOUT
        self.nivel=1

    @property
    def score(self):
        return 'Score : {}'.format(self.punteo)
    @property
    def Nivel(self):
        return 'Nivel : {}'.format(self.nivel)

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

    def Eliminar_Ultimo(self):
        if self.primero==None:
            print("lista Vacia")
        else:
            aux=self.primero
            aux=self.ultimo.atras
            aux.siguiente=None
            self.ultimo=aux

    def Insertar_Inicio(self,x,y):
        nuevo=NodoDoble(x,y)
        if self.primero==None:
            self.primero=nuevo
            self.ultimo=nuevo
        else:
            self.primero.atras=nuevo
            nuevo.siguiente=self.primero
            self.primero=nuevo

    def Listar(self,window):
        temp=self.primero
        contador=0
        while temp != None:
            coorx=temp.coorx
            coory=temp.coory
            if contador==0:
                window.addstr(coory, coorx, '0')
            else:
                window.addstr(coory, coorx, '#')
            contador+=1

            temp=temp.siguiente

    def render(self,window):
        temp=self.primero
        prob=randint(1, 4)
        while temp != None:
            window.addstr(self.y, self.x, '+')
            temp=temp.siguiente

    def render2(self,window):
        temp=self.primero
        prob=randint(1, 4)
        while temp != None:
            window.addstr(self.y2, self.x2, '*')
            temp=temp.siguiente

    def Comer(self,x,y,s,window):
        s.reiniciar()
        s.Insertar_Inicio(x,y)
        self.punteo += 1
        if self.punteo <= 6:
            p.InsertarScore(x,y)
        else:
            self.tiempo -= 5
            self.nivel = 2
            window.timeout(self.tiempo)
            p.InsertarScore2(x,y)

    def reiniciar(self):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)

    def Colision(self,x,y):
        temp=self.primero
        aux=temp.siguiente
        bandera=True
        while aux!=None:
            coorx=aux.coorx
            coory=aux.coory
            if coorx==x and coory==y:
                bandera=True
                break
            else:
                bandera=False
            aux=aux.siguiente
        return bandera


    def GraficarDobleSnake(self):
        file = open("ListaDobleSnake.dot", "w")
        file.write("digraph G {rankdir = \"LR\"; \n subgraph cluster3{\nlabel=\"Snake\";\n")
        snake=self.primero
        if self.primero!=None:
            c=str(hash(snake))
            file.write("h" +"[shape=record, style=filled, fillcolor=seashell2,label=\"NULL" + "\"];\n")
            file.write(c +"[shape=record, style=filled, fillcolor=seashell2,label=\"("+str(snake.coorx)+","+str(snake.coory) + ")\"];\n")
            file.write("h" + "->" + c+"[dir=back color=\"blue\"]\n")

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
if __name__ == '__main__':
    curses.initscr()
    curses.beep()
    curses.beep()
    window = curses.newwin(HEIGHT, WIDTH, 0, 0)
    window.timeout(TIMEOUT)
    window.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    window.border()
    s=ListaDoble()

    s.Insertar_Inicio(3,5)
    s.Insertar_Inicio(4,5)
    s.Insertar_Inicio(5,5)
    movimiento=""
    direction = curses.KEY_RIGHT

    while True:
        window.clear()
        window.border(0)
        aux=s.primero
        auxx=s.x
        auxy=s.y
        x=aux.coorx
        y=aux.coory
        s.render(window)
        s.render2(window)
        s.Listar(window)

        window.addstr(0, 5, s.score)
        window.addstr(0, 20, s.Nivel)
        key = window.getch()
        if key == 27:
            break
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP]:
            direction = key
        if direction == curses.KEY_RIGHT:
            movimiento="Derecha"
            x+=1
            if x > MAX_X:
                x = 1
        elif direction == curses.KEY_LEFT:
            movimiento="Izquierda"
            x-=1
            if x < 1:
                x = MAX_X
        elif direction == curses.KEY_DOWN:
            movimiento="Abajo"
            y+=1
            if y > MAX_Y:
                y = 1
        elif direction == curses.KEY_UP:
            movimiento="Arriba"
            y-=1
            if y < 1:
                y = MAX_Y
        if x==auxx and y==auxy:
            s.Comer(x,y,s,window)
        if s.Colision(x,y)==True:
            window.clear()
            msg = "Game Over!"
            centro = round((60-len(msg))/2)
            window.addstr(0,centro,msg)
            print("perdio")
            curses.beep()
            window.nodelay(0)
            window.getch()
            window.refresh()
            curses.echo()
            s.GraficarDobleSnake()
            p.Graficarpila()
        s.Eliminar_Ultimo()
        s.Insertar_Inicio(x,y)

    curses.endwin()
