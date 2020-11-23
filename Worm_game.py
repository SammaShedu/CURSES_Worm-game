#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import curses
import random
import pdb

def puntos(max_y,max_x,laberinto):
    p = []
    color_p = []
    i = 0

    for i in range(1,9):
        yx = [random.randrange(1,max_y - 2),random.randrange(1,max_x - 2)]

        if yx not in laberinto and yx not in p:
            p.append(yx)
        else:
            while yx in laberinto or yx in p:
                yx = [random.randrange(1,max_y - 2),
                    random.randrange(1,max_x - 2)]

            p.append(yx)

        # p.append(yx)
        c = random.randrange(1,239)
        if c not in color_p and c != 1:
            color_p.append(c)
        else:
            while c in color_p or c == 1:
                c = random.randrange(1,239)
            color_p.append(c)
        i += 1

    return p, color_p

def lab(laberinto,max_y):
    a = 5
    for i in range(1,30,a):
        laberinto.append([i,20])
    # for i in range(1,30,a):
    #     laberinto.append([i,40])
    for i in range(1,30,a):
        laberinto.append([i,60])
    # for i in range(1,30,a):
    #     laberinto.append([i,80])
    for i in range(1,30,a):
        laberinto.append([i,100])
    # for i in range(1,30,a):
    #     laberinto.append([i,120])
    for i in range(3,30,a):
        laberinto.append([max_y -i,30])
    # for i in range(3,30,a):
    #     laberinto.append([max_y -i,50])
    for i in range(3,30,a):
        laberinto.append([max_y -i,70])
    # for i in range(3,30,a):
    #     laberinto.append([max_y -i,90])
    for i in range(3,30,a):
        laberinto.append([max_y -i,110])
    return laberinto

def main(stdscr):
    # Calcula el tamaño de que tiene que tener el área de juego
    max_y , max_x = stdscr.getmaxyx()

    # Crea una subpantalla y pinta el borde
    scr = stdscr.subwin(max_y - 1, max_x,0,0)

    # Define los colores basicos
    if curses.has_colors():
        for i in range(1,239):
            curses.init_pair(i, 0, i)
        # curses.init_pair(1, 0, curses.COLOR_BLUE)
        # curses.init_pair(2, 0, curses.COLOR_CYAN)
        # curses.init_pair(3, 0, curses.COLOR_GREEN)
        # curses.init_pair(4, 0, curses.COLOR_MAGENTA)
        # curses.init_pair(5, 0, curses.COLOR_RED)
        # curses.init_pair(6, 0, curses.COLOR_YELLOW)
        # curses.init_pair(7, 0, curses.COLOR_WHITE)

    # curses.init_pair(1,0,10)
    # scr.attrset(curses.color_pair(random.randrange(1,7)))
    scr.border()

    # Escribe los comandos en la ventana principal
    stdscr.addstr(max_y - 1,0,'S)Comenzar / Parar  Q)Salir')
    stdscr.refresh()

    # Crear el listado de las posiciones del gusano
    i = 30
    gus = [[i,1],[i,2],[i,3],[i,4],[i,5],[i,6],[i,7],[i,8],[i,9],[i,10]]
    color_gus = random.randrange(1,239)
    dir = 'derecha'

    # Pinta el laberinto
    laberinto = list()
    laberinto = lab(laberinto,max_y)

    # laberinto = [[max_y -3,10],[max_y -4,10],[max_y -5,10],
    #              [max_y -6,10],[max_y -7,10],[max_y -8,10],[max_y -9,10],
    #              [max_y -10,10],[max_y -11,10],[max_y -12,10],[max_y -13,10]]
    for i in laberinto:
        scr.addstr(i[0],i[1],' ',curses.A_REVERSE)

    # Crea la primera posición del cuadrado que puede ser comido por el gusano
    # p = [random.randrange(1,max_y - 2),
    #     random.randrange(1,max_x - 2)]
    # color_p = random.randrange(1,7)
    # scr.addstr(p[0],p[1],' ',curses.color_pair(color_p))
    p, color_p = puntos(max_y,max_x,laberinto)
    for i in range(0,8):
        p_aux = p[i]
        scr.addstr(p_aux[0],p_aux[1],' ',curses.color_pair(color_p[i]))

    scr.refresh()

    # Quita la visibilidad al cursor
    curses.curs_set(0)
    reiniciar = False
    nivel = 0

    # Bucle principal. Espera a que se pulse una tecla
    while True:
        c = scr.getch()  # Recoge la tecla pulsada
        if 0 < c < 255:
            c = chr(c)
            if c in 'Ss':
                if reiniciar:
                    # Pinta de nuevo la pantalla
                    scr.clear()
                    scr.border()

                    # Crear el listado de las posiciones del gusano
                    i = 12
                    gus = [[i,1],[i,2],[i,3],[i,4],[i,5],[i,6],[i,7],[i,8],[i,9],[i,10]]
                    color_gus = random.randrange(1,239)
                    dir = 'derecha'

                    # Pinta el laberinto
                    # laberinto = [[20,50],[21,50],[22,50],[23,50],[24,50],[25,50],[26,50]]
                    laberinto = list()
                    laberinto = lab(laberinto,max_y)

                    for i in laberinto:
                        scr.addstr(i[0],i[1],' ',curses.A_REVERSE)

                    # Crea la primera posición del cuadrado que puede ser comido por el gusano
                    # p = [random.randrange(1,max_y - 2),
                    # random.randrange(1,max_x - 2)]
                    # color_p = random.randrange(1,7)
                    # scr.addstr(p[0],p[1],' ',curses.color_pair(color_p))
                    p, color_p = puntos(max_y,max_x,laberinto)
                    for i in range(0,8):
                        p_aux = p[i]
                        scr.addstr(p_aux[0],p_aux[1],' ',curses.color_pair(color_p[i]))

                    scr.refresh()

                for i in gus:
                    scr.addstr(i[0],i[1],' ')

                stdscr.nodelay(1)

                while True:
                    # Espera una señal del teclado
                    c = stdscr.getch()
                    if 0 < c < 255:
                        c = chr(c)
                        if c in 'SsQq':
                            break
                    elif c == curses.KEY_UP:
                        dir = 'arriba'
                    elif c == curses.KEY_DOWN:
                        dir = 'abajo'
                    elif c == curses.KEY_RIGHT:
                        dir = 'derecha'
                    elif c == curses.KEY_LEFT:
                        dir = 'izquierda'

                    # Borra el gusano
                    for i in gus:
                        scr.addstr(i[0],i[1],' ',curses.color_pair(0))

                    # Calcula las nuevas posiciones del gusano
                    aux = gus[-1]
                    if dir == 'arriba':
                        if i[0] <= 1:
                            gus.append([max_y - 3,aux[1]])
                        else:
                            gus.append([aux[0] - 1,aux[1]])
                    elif dir == 'abajo':
                        if i[0] >= max_y - 3:
                            gus.append([1,aux[1]])
                        else:
                            gus.append([aux[0] + 1,aux[1]])
                    elif dir == 'derecha':
                        if i[1] >= max_x - 2:
                            gus.append([aux[0],1])
                        else:
                            gus.append([aux[0],aux[1] + 1])
                    elif dir == 'izquierda':
                        if i[1] <= 1:
                            gus.append([aux[0],max_x - 2])
                        else:
                            gus.append([aux[0],aux[1] - 1])

                    gus.pop(0)  # Quita la cola del gusano

                    # Pinta el gusano
                    for i in gus:
                        scr.addstr(i[0],i[1],' ',curses.color_pair(color_gus))

                    # Si el gusano atrapa un cuadrado cambia a ese color
                    # if gus[-1] == p:
                    if gus[-1] in p:
                        color_gus = color_p[p.index(gus[-1])]
                        # Quita el punto del listado
                        del color_p[p.index(gus[-1])]
                        p.remove(gus[-1])

                        # Crea un nuevo cuadrado de color
                        # p = [random.randrange(1,max_y - 2),
                        #     random.randrange(1,max_x - 2)]
                        # Chapucilla para evitar que se solape con el laberinto
                        # if p in laberinto:
                        #     p = [random.randrange(1,max_y - 2),
                        #         random.randrange(1,max_x - 2)]
                        # color_p = random.randrange(1,7)

                        # Si ya no quedan más puntos termina la partida
                        if len(p) == 0:
                            py = max_y // 2 - 2
                            px = max_x // 2 - 10
                            scr.addstr(py,px,' ' * 21, curses.A_REVERSE)
                            scr.addstr(py,px,' ' * 21)
                            scr.addstr(py + 1,px,' ' * 21)
                            scr.addstr(py + 2,px,' ' * 21)
                            scr.addstr(py + 3,px,' ' * 21)
                            scr.addstr(py + 4,px,' ' * 21)
                            scr.addstr(py + 1,px + 1,' ' * 19,curses.A_REVERSE)
                            scr.addstr(py + 2,px + 1,' W E L L   D O N E ',curses.A_REVERSE)
                            scr.addstr(py + 3,px + 1,' ' * 19,curses.A_REVERSE)
                            curses.beep()
                            reiniciar = True
                            nivel += 20
                            break

                    elif gus[-1] in laberinto:
                        # Si choca con las paredes termina la partida
                        # py = int(max_y / 2) - 2
                        # px = int(max_x / 2) - 10
                        py = max_y // 2 - 2
                        px = max_x // 2 - 10
                        scr.addstr(py,px,' ' * 21, curses.A_REVERSE)
                        scr.addstr(py,px,' ' * 21)
                        scr.addstr(py + 1,px,' ' * 21)
                        scr.addstr(py + 2,px,' ' * 21)
                        scr.addstr(py + 3,px,' ' * 21)
                        scr.addstr(py + 4,px,' ' * 21)
                        scr.addstr(py + 1,px + 1,' ' * 19,curses.A_REVERSE)
                        scr.addstr(py + 2,px + 1,' G A M E   O V E R ',curses.A_REVERSE)
                        scr.addstr(py + 3,px + 1,' ' * 19,curses.A_REVERSE)
                        curses.beep()
                        reiniciar = True
                        break

                    scr.refresh()
                    curses.napms(100 - nivel)

            elif c in 'Qq':
                break

if __name__ == '__main__':
    curses.wrapper(main)
