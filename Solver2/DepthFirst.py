'''
Created on 13.02.2021

__updated__='2021-02-13'

@author: jung
'''

import copy
from Solver2 import Spielfelder

Richtung = {'N': (0, -1),
            'S': (0, 1),
            'O': (1, 0),
            'W': (-1, 0)}

Gegenrichtung = {'N': 'S',
                 'S': 'N',
                 'O': 'W',
                 'W': 'O'}


def zeige(Feld, x=-1, y=-1):
    for j in range(len(Feld)):
        for i in range(len(Feld[0])):
            if (i, j) == (x, y):
                print('#', end=' ')
            elif Feld[j][i]:
                print('O', end=' ')
            else:
                print('·', end=' ')
        print()
    print()


def fertig(Feld):
    for Zeile in Feld:
        if 1 in Zeile:
            return False
    return True


def gehe_nach(Feld, x, y, r):

    x_Dimension = len(Feld[0])
    y_Dimension = len(Feld)

    while True:
        x += Richtung[r][0]
        y += Richtung[r][1]

        if x not in range(x_Dimension):
            return (False, 0, 0)
        if y not in range(y_Dimension):
            return (False, 0, 0)

        if Feld[y][x]:
            return (True, x, y)


def suche(Feld, Weg, x, y):
    Feld[y][x] = 0

    if fertig(Feld):
        return True

    if len(Weg) == 0:
        verboten = 'X'
    else:
        verboten = Gegenrichtung[Weg[-1]]

    for r in Richtung:
        if r is verboten:
            continue

        Weg.append(r)
        (Erfolg, x_neu, y_neu) = gehe_nach(Feld, x, y, r)
        if Erfolg:
            if suche(Feld, Weg, x_neu, y_neu):
                return True
        Weg.pop()

    Feld[y][x] = 1
    return False


def spiele(Feld, Weg, x, y):
    zeige(Feld, x, y)
    for r in Weg:
        Feld[y][x] = 0
        (_, x, y) = gehe_nach(Feld, x, y, r)
        zeige(Feld, x, y)


if __name__ == '__main__':

    Feld = copy.deepcopy(Spielfelder.Seerosen06)
    x, y = Spielfelder.x06, Spielfelder.y06

    zeige(Feld, x, y)

    print('Suche...')

    Weg = []

    if suche(Feld, Weg, x, y):
        print('Lösung gefunden: ', end='')
        print(*Weg, sep='-')
        print()
    else:
        print('Keine Lösung gefunden!')

    spiele(Spielfelder.Seerosen06, Weg, x, y)
