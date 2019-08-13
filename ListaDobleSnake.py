import os
import curses
from ScorePila import PilaScore
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
import random
WIDTH = 35
HEIGHT = 20
MAX_X = WIDTH - 2
MAX_Y = HEIGHT - 2
TIMEOUT = 100
movimiento=""
class NodoDoble:

    def __init__(self, coorx, coory):
        self.coorx=coorx
        self.coory=coory
        self.siguiente=None
        self.atras=None

    def __str__(self):
        return "%s %s" %(self.coorx, self.coory)

class comida:
    def __init__(self, window):
        self.window = window

    def generar_comida(self, score):
        self.poscomidax = randint(1, 98)
        self.poscomiday = randint(1, 33)
        if score == 0:
            self.tipocomida = 10
        else:
            self.tipocomida = randint(1, 100)

    def pintar_comida(self):
        if self.tipocomida < 80:
            self.window.addstr(self.poscomiday, self.poscomidax, "+")
        else:
            self.window.addstr(self.poscomiday, self.poscomidax, "*")

    def coordenadacomidax(self):
        return self.poscomidax

    def coordenadacomiday(self):
        return self.poscomiday

    def obtenertipocomida(self):
        return self.tipocomida

class Food(object):
    def __init__(self, window,char='+'):
        self.x = random.randint(1, MAX_X)
        self.y = random.randint(1, MAX_Y)
        self.window = window
        self.char=char
        tipo=random.randint(0,40)
        if tipo <=25 :
            self.type_food = 0 #0 == bad food (*)
        else:
            self.type_food = 1 #1 == good food (+)

    def render(self):
        self.window.addstr(self.y, self.x, self.char)

    def reset(self):
        self.x = random.randint(1, MAX_X)
        self.y = random.randint(1, MAX_Y)


class ListaDoble:
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.punteo=0
        self.tiempo=TIMEOUT
        self.nivel=1
        self.x = random.randint(1, MAX_X)
        self.y = random.randint(1, MAX_Y)
        self.RETURN = ord("\n")
        self.SPACE  = ord(" ")
        self.KEY_M  = ord("m")
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
            if contador==0:
                window.addstr(temp.coory, temp.coorx, '0')
            else:

                window.addstr(temp.coory, temp.coorx, '#')
            contador+=1
            temp=temp.siguiente

    def Comer(self,x,y,s,window):
        a=True
        s.reiniciar()
        window.clear()
        if self.type_food == 1:
            window.addstr(self.y, self.x, '+')
            s.Insertar_Inicio(x,y)
            print("sale mas")
            self.punteo += 1
            a=True
        else:
            window.addstr(self.y, self.x, '*')
            s.Eliminar_Ultimo(x,y)
            print("sale menos")
            self.punteo -= 1
            a=False

        if self.punteo <= 15:
            p.InsertarScore(x,y)
        else:
            self.tiempo -= 5
            self.nivel = 2
            window.timeout(self.tiempo)
            p.InsertarScore2(x,y)
        return a

    def reiniciar(self):
        self.x = random.randint(1, MAX_X)
        self.y = random.randint(1, MAX_Y)

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
    def GameOver(sefl,window):
        window.clear()
        msg = "Game Over!"
        centro = round((60-len(msg))/2)
        window.addstr(0,centro,msg)

        window.addstr(7,21, '1. Play')
        window.addstr(8,21, '2. Scoreboard')
        window.addstr(9,21, '3. User Selection')
        window.addstr(10,21, '4. Reports')
        window.addstr(11,21, '5. Bulk Loading')
        window.addstr(12,21, '6. Exit')
        window.timeout(-1)
        q = None
        while q not in (ord("\n"), ord("m"), ord("q")):
            q = window.getch()
            if q == ord("q"):
                option = "quit"
            elif q == ord("\n"):
                option = "play again"
            elif q == ord("m"):
                option = "menu"
        window.clear()
        return option
    def Juego(self,window,s,p):
        window.clear()
        window.timeout(100)
        window.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        window.nodelay(1)
        window.border(0)
        s.Insertar_Inicio(3,5)
        s.Insertar_Inicio(4,5)
        s.Insertar_Inicio(5,5)
        prev_button_direction = 1
        button_direction = 1
        tipocomida=False
        food=Food(window,"+")
        direction = curses.KEY_RIGHT

        while True:
            window.clear()
            window.border(0)
            aux=s.primero
            x=aux.coorx
            y=aux.coory
            auxx=s.x
            auxy=s.y
            s.Listar(window)
            food.render()
            window.addstr(0, 5, s.score)
            window.addstr(0, 20, s.Nivel)

    #--------------------------DIRECCION DE LAS TECLAS SNAKE------------
            key = window.getch()
            prevKey = direction
            if key == 27:
                break

            direction = direction if key == -1 else key

            if direction == ord(' '):                                                             # empty space == '32' which is ASCII for 'space bar'. If the keystroke is spacebar, key is assigned to 32 and gets stuck in this if statement. Then key is reassigned to -1.
                direction = -1
                while direction != ord(' '):                                                      # Tried to explain the loop but it takes too much text. Figure it out :D
                    direction = window.getch()
                    curses.beep()                                                           # Added a beep so you can hear when it repeats the loop. Just delete if it's annoying.

                direction = prevKey
                continue

            if key == -1:
                direction = direction
            else:
                direction = key


            if direction == curses.KEY_LEFT and prev_button_direction != 1:
                button_direction = 0 #Izquierda
            elif direction == curses.KEY_RIGHT and prev_button_direction != 0:
                button_direction = 1 #Derecha
            elif direction == curses.KEY_UP and prev_button_direction != 2:
                button_direction = 3 #Arriba
            elif direction == curses.KEY_DOWN and prev_button_direction != 3:
                button_direction = 2 #Abajo
            else:
                pass

            prev_button_direction = button_direction
            if button_direction == 1:# Derecha
                x+=1
                if x > MAX_X:
                    x = 1
            elif button_direction == 0: #Izquierda
                x-=1
                if x < 1:
                    x = MAX_X
            elif button_direction == 2:#Abajo
                y+=1
                if y > MAX_Y:
                    y = 1

            elif button_direction == 3:#Arriba
                y-=1
                if y < 1:
                    y = MAX_Y
    #--------------------------FIN DIRECCION DE LA SNAKE-----------

            #---------------SERPIERENTE COME*******************

            if x == food.x and y == food.y:
                if tipocomida is True:
                    s.punteo -= 1
                    s.Eliminar_Ultimo()
                    p.Pop()
                elif tipocomida is False:
                    s.punteo += 1
                    s.Insertar_Inicio(x,y)
                    p.InsertarScore(auxx,auxy)
                    window.refresh()
        #--------------------FABRICAR DOS TIPOS DE COMIDA ----
                if random.random() > 0.85:
                    food = Food(window, '*')
                    food.render()
                    tipocomida = True
                    print("malo")
                else:
                    food=Food(window,"+")
                    food.render()
                    tipocomida = False
                    print("bueno")
                s.reiniciar()# REINICIA COORDENADAS

            #SERPIENTE CHOCA CON ELLA MISMA-----------------
            if s.Colision(x,y)==True:
                while True:
                    opt=s.GameOver(window)
                    if opt == "quit":
                         curses.endwin()
                         break
                    elif opt == "play again":
                        continue
                    elif opt == "menu":
                        break
                #s.GraficarDobleSnake()
                #p.Graficarpila()
            s.Insertar_Inicio(x,y)
            s.Eliminar_Ultimo()
