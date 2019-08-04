from ListaDobleSnake import ListaDoble
from ListaCicularDoble_Usuarios import ListaCircularDobleUsuarios
from ScorePila import PilaScore
from Cola_ScoreBoard import ColaScore
import curses
from curses import textpad
import time
#-----------------------------------------MENU DE OPCIONES---------------------------------
opciones_menu=['1. Play','2. ScoreBoard', '3. User selection','4. Reportes','5.Carga de usuarios','6. Salir']

def Menu(stdscr,selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx,row in enumerate(opciones_menu):
        x = w//2 - len(row)//2
        y = h//2 - len(opciones_menu)//2 +idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y,x,row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y,x,row)

    stdscr.refresh()



def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row_idx=0

    Menu(stdscr,current_row_idx)
    stdscr.refresh()
    stdscr.getch()

    while 1:
        key = stdscr.getch()
        stdscr.clear()
        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(opciones_menu)-1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10,13]:
            stdscr.addstr(0,0,"opcion {}".format(opciones_menu[current_row_idx]))

            if current_row_idx == len(opciones_menu)-1:#boton salir
                break
            elif current_row_idx == len(opciones_menu)-6:
                curses.wrapper(mainSnake)


        Menu(stdscr,current_row_idx)
        stdscr.refresh()

#----------------------------------------JUEGO DE SNAKE------------------------
def mainSnake(stdscr):
    curses.curs_set(0)
    sh,sw = stdscr.getmaxyx()
    box =[[3,3],[sh-3,sw-3]]
    textpad.rectangle(stdscr,box[0][0],box[0][1],box[1][0],box[1][1])
    snake=[[sh//2,sw//2+1],[sh//2,sw//2],[sh//2,sw//2-1]]
    direccion=curses.KEY_RIGHT

    for y,x in snake:
        stdscr.addstr(y,x,'#')
    stdscr.refresh()
    stdscr.getch()





if __name__=="__main__":

    curses.wrapper(main)
    listadoble=ListaDoble()
    listadoble.Insertar(5,4)
    listadoble.Insertar(5,3)
    listadoble.Insertar(5,2)
    listadoble.Listar()
    listadoble.GraficarDobleSnake()

    usuarios=ListaCircularDobleUsuarios()
    usuarios.InsertarUsuario("Eduardo")
    usuarios.InsertarUsuario("Saul")
    usuarios.InsertarUsuario("Tun")
    usuarios.InsertarUsuario("Aguilar")
    usuarios.Listar()
    usuarios.GraficarUsuarios()

    score=PilaScore()
    score.InsertarScore(4,1)
    score.InsertarScore(3,2)
    score.InsertarScore(2,3)
    score.InsertarScore(1,4)
    score.Pop()
    score.Graficarpila()

    cola=ColaScore()
    cola.IngresarCola("Eduardo",1)
    cola.IngresarCola("Saul",2)
    cola.IngresarCola("Tun",3)
    cola.GraficarCola()
