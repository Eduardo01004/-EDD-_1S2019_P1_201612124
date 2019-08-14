from ListaDobleSnake import ListaDoble
from ListaCicularDoble_Usuarios import ListaCircularDobleUsuarios
from ScorePila import PilaScore
from Cola_ScoreBoard import ColaScore
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint
import time
import csv
listausuarios=ListaCircularDobleUsuarios()
cola=ColaScore()
WIDTH = 35 #ancho
HEIGHT = 20 # altura
username=""
#------------------------------MENU PRINCIPAL-----------------------------
def Menu_Principal(window):

    Titulo(window,'Main Menu')
    window.addstr(7,21, '1. Play')
    window.addstr(8,21, '2. Scoreboard')
    window.addstr(9,21, '3. User Selection')
    window.addstr(10,21, '4. Reports')
    window.addstr(11,21, '5. Bulk Loading')
    window.addstr(12,21, '6. Exit')
    window.timeout(-1)


def Titulo(window,var):
    window.clear()
    window.border()
    centro = round((60-len(var))/2)
    window.addstr(0,centro,var)

def TeclaESC(window):
    tecla=window.getch()
    while tecla!=27:
        tecla = window.getch()


def m(window):
    score=PilaScore()
    listasnake=ListaDoble()
    keystroke = -1
    while(keystroke==-1):
        keystroke = window.getch()
        if(keystroke==49):
            global username
            Titulo(window, ' PLAY ')
            if username == "":
                a = Crear_Usuario(window)
                username = "".join(map(chr, a))
                listasnake.Juego(window,listasnake,score,username,cola)
            else:
                listasnake.Juego(window,listasnake,score,username,cola)
            TeclaESC(window)
            Menu_Principal(window)
            keystroke=-1
        elif(keystroke==50):
            Titulo(window, ' SCOREBOARD ')
            Scoreboard(window)
            TeclaESC(window)
            Menu_Principal(window)
            keystroke=-1
        elif(keystroke==51):
            Titulo(window, ' USER SELECTION ')
            Menu_Usuarios(window,listasnake,score)
            TeclaESC(window)
            Menu_Principal(window)
            keystroke=-1
        elif(keystroke==52):
            Titulo(window,' Reports')
            Principal_Usuarios(window,listasnake,score)
            TeclaESC(window)
            Menu_Principal(window)
            keystroke=-1
        elif(keystroke==53):
            Titulo(window,' BULK LOADING ')
            LeerArchivo_Usuarios(window)
            TeclaESC(window)
            Menu_Principal(window)
            keystroke=-1
        elif(keystroke==54):
            pass
        else:
            keystroke=-1
#----------------------------------fin menu principal----------------------///

#------------------CARGA DE ARCHIVOS DE USUARIOS-------------------
def LeerArchivo_Usuarios(window):
    archivo=carga(window)
    try:
        with open(archivo) as file:
            reader = csv.reader(file)
            line_count = 0
            for row in reader:
                if line_count == 0:
                    line_count += 1
                else:
                    listausuarios.InsertarUsuario(row[0])#aqui se inserta el dato a la lista circular doble
                    line_count +=  1

            while True:
                window.clear()
                window.border(0)
                Titulo(window,' BULK LOADING ')
                msg="Carga Con exito"
                centro = round((60-len(msg))/2)
                window.addstr(10,centro,msg)
                sel = window.getch()
                if sel == 27:
                    break
    except:
        while True:
            window.clear()
            window.border(0)
            Titulo(window,' BULK LOADING ')
            texto2="Error al cargar el archivo"
            centro2 = round((60-len(texto2))/2)
            window.addstr(10,centro2,texto2)
            key2 = window.getch()
            if key2 is 27:
                carga(window)
                break

def carga(window):
    window.clear()
    window.border(0)
    Titulo(window,' BULK LOADING ')
    msg="Ingresa El nombre del archivo csv"
    centro = round((60-len(msg))/2)
    window.addstr(10,centro,msg)
    texto = ""
    while True:
        centro2 = round((60-len(texto))/2)
        window.addstr(15,centro,texto)
        key = window.getch()
        if key is 10:
            break
        elif key > 0:
            texto += str(chr(key))
    return texto

def print_Users(window, name):
    window.clear()
    Titulo(window,' USERS ')
    height, width = window.getmaxyx()
    text="<-    "+ name +"    -> "
    centro = round((60-len(text))/2)
    window.addstr(10, centro , text)
    window.refresh()

def Menu_Usuarios(window,listasnake,score):

    temp=listausuarios.primero
    temp2=listausuarios.ultimo
    validar=True
    global username
    if temp != None:
        name = temp.nombre
        print_Users(window, name)
        while(validar):
            key = window.getch()
            if key == curses.KEY_RIGHT:
                temp = temp.siguiente
                name = temp.nombre
            elif key == curses.KEY_LEFT:
                temp = temp.anterior
                name = temp.nombre
            elif key == 10:
                username =name
                listasnake.Juego(window,listasnake,score,username,cola)
                break
            elif key == 27:
                break
            print_Users(window, name)
    else:
        print_Users(window, "Vacio")
#-----------------------------MENU DE REPORTES ------------------------------
def Menu_Reportes(window):
    Titulo(window,'Reportes')
    window.addstr(7,21, '1. Snake Report(Lista Doble)')
    window.addstr(8,21, '2. ScoreReport(Pila)')
    window.addstr(9,21, '3. Scoreboard Report(Cola)')
    window.addstr(10,21, '4. Users Report(Lista Circular Doble)')
    window.addstr(11,21, '5. Main Menu')
    window.addstr(12,21, '6. Exit')
    window.timeout(-1)

def Principal_Usuarios(window,listasnake,score):
    window.clear()
    Menu_Reportes(window)
    keystroke = -1
    while(keystroke==-1):
        keystroke = window.getch()
        if(keystroke==49): #1
            listasnake.GraficarDobleSnake()
            keystroke=-1
        elif(keystroke==50):
            score.Graficarpila()
            keystroke=-1
        elif(keystroke==51):
            cola.GraficarCola()
            keystroke=-1
        elif(keystroke==52):
            listausuarios.GraficarUsuarios()
            keystroke=-1
        elif(keystroke==53):
            TeclaESC(window)
            Menu_Principal(window)
            m(window)
            keystroke=-1
        elif(keystroke==54):
            pass
        else:
            keystroke=-1
    window.refresh()
#-----------------------------OPCION DEL SCOREBOARD DE LA COLA ----------------
def Scoreboard(screen):

    Cola()
    screen.clear()
    Titulo(screen, ' SCOREBOARD ')
    temp=cola.primero
    max_row = 10 #max number of rows
    contador=0
    if temp != None:
        screen.addstr( 4, 25, "NAME" )
        screen.addstr( 4, 40, "SCORE" )
        while temp is not None and contador < max_row + 1:
            name=temp.nombre
            score=temp.punteo
            screen.addstr( 15-contador, 25, str(name) )
            screen.addstr( 15-contador, 40, str(score))
            temp = temp.siguiente
            contador += 1
            screen.refresh()
    else:
        screen.addstr( 10, 25, "Vacio" )
#--------------------------Crear nuevo usuario-------------------
def Crear_Usuario(screen):
    curses.echo()
    curses.curs_set(True)
    screen.addstr(5, 5, "No ha cargado usuario: ")
    screen.addstr(10, 5, "Ingrese nombre usuario")
    global username
    jugador = screen.getstr()
    username = "".join(map(chr, jugador))
    listausuarios.InsertarUsuario(username)
    curses.curs_set(False)
    screen.clear()
    return jugador

#Verificar que la cola tiene tope de 10-------
def Cola():
    temp=cola.primero
    contador=0
    while temp !=None:
        if contador > 9:
            cola.eliminar()
        contador +=1
        temp = temp.siguiente
#------------------------INICIO DEL PROGRAMA----------------------------
curses.initscr()
window = curses.newwin(20,60,0,0)
curses.start_color()
window.keypad(True)
curses.noecho()
curses.curs_set(0)
window.border(0)

Menu_Principal(window)
m(window)


curses.endwin()
