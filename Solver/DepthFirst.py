'''
Created on 11.02.2021

__updated__="2021-02-13"

@author: jung
'''

# Spielfeld
Seerosen01 = [[0, 1, 1, 0],
              [1, 0, 1, 1],
              [1, 0, 1, 0],
              [0, 1, 0, 0]]
x01 = 3
y01 = 1

Seerosen02 = [[1, 1, 1, 0],
              [0, 1, 1, 1],
              [0, 1, 1, 1],
              [0, 0, 0, 1]]
x02 = 0
y02 = 0

Seerosen03 = [[0, 1, 1, 1, 0],
              [0, 1, 0, 1, 0],
              [0, 1, 0, 1, 1],
              [1, 1, 1, 1, 0]]
x03 = 0
y03 = 3

Seerosen04 = [[0, 0, 0, 0, 1, 1],
              [0, 1, 1, 0, 0, 1],
              [0, 0, 1, 1, 1, 1],
              [0, 1, 0, 0, 1, 0],
              [1, 1, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 1]]
x04 = 0
y04 = 4

Seerosen05 = [[0, 0, 1, 0, 0],
              [0, 1, 1, 0, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 0, 1, 1],
              [0, 0, 0, 1, 0]]
x05 = 2
y05 = 0

Seerosen06 = [[0, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 1, 0],
              [0, 1, 1, 1, 0, 0],
              [0, 1, 1, 0, 1, 1],
              [1, 1, 0, 1, 0, 1],
              [0, 0, 0, 0, 1, 1]]
x06 = 0
y06 = 4

# Spielfeld
Seerosen = Seerosen06

# Start
x = x06
y = y06

# Initialisierung
import copy

assert len(Seerosen) > 0

x_Dimension = len(Seerosen[0])
y_Dimension = len(Seerosen)

assert x < x_Dimension
assert y < y_Dimension

print("Dimension: {}, {}".format(x_Dimension, y_Dimension))

Richtung = {'N': (0, -1),
            'S': (0, 1),
            'O': (1, 0),
            'W': (-1, 0)}

Gegenrichtung = {'N': 'S',
                 'S': 'N',
                 'O': 'W',
                 'W': 'O'}

Weg = []

# Funktionen


# Gehe, wenn möglich, von der Position (x, y) in eine bestimmte Richtung r
def gehe_nach(r, x, y):
    global Seerosen

    # Losgehen
    while True:
        x += Richtung[r][0]
        y += Richtung[r][1]

        # Außerhalb vom Spielfeld? Diese Richtung war nichts
        if x not in range(x_Dimension):
            return (False, 0, 0)
        if y not in range(y_Dimension):
            return (False, 0, 0)

        # Auf eine 1 gestoßen? Gut! Erfolg melden und neue Koordinaten zurückgeben.
        if Seerosen[y][x]:
            return (True, x, y)

    # In dieser Richtung nichts gefunden! Misserfolg melden und einfach 0 als Koordinaten zurückgeben.
    return (False, 0, 0)


# Suche alle möglichen Wege von der Position (x, y) aus. Dabei darf man nicht zurück!
def suche(woher, x, y):
    global Seerosen, Weg

    # Das jetztige Feld löschen
    Seerosen[y][x] = 0

    # Debugging --------------------------
    # Seerosen_tmp = copy.deepcopy(Seerosen)
    # Seerosen_tmp[y][x] = 8
    # for Zeile in Seerosen_tmp:
    #    print(Zeile)
    # ------------------------------------

    # Gewonnen?
    Einser = False
    for Zeile in Seerosen:
        if 1 in Zeile:
            Einser = True
            break
    if not Einser:
        print("Lösung gefunden!")
        print(*Weg, sep="-")

        Seerosen[y][x] = 8
        for Zeile in Seerosen:
            print(Zeile)

        return True

    # Man darf nicht einfach zurücklaufen!
    verboten = Gegenrichtung[woher]

    # Suche in allen anderen Richtungen
    for r in Richtung:
        if r is verboten:
            continue
        Weg.append(r)
        # Debugging -------------------------------
        # print(*Weg, sep='-')
        # -----------------------------------------
        # Ist der Zug möglich?
        (Erfolg, x_neu, y_neu) = gehe_nach(r, x, y)
        if Erfolg:
            # Ja, der Zug ist möglich! Suche vom neuen Feld aus.
            if suche(r, x_neu, y_neu):
                # Erfolg! Setze den Weg zusammen und melde die Lösung
                Weg.insert(0, r)
                return True
        Weg.pop()

    # Hier ging nichts! Löschung rückgängig machen, Misserfolg melden.
    Seerosen[y][x] = 1
    return False


def löse(x, y):
    global Seerosen, Weg

    Seerosen[y][x] = 0

    # Debugging --------------------------
    Seerosen_tmp = copy.deepcopy(Seerosen)
    Seerosen_tmp[y][x] = 8
    for Zeile in Seerosen_tmp:
        print(Zeile)
    # ------------------------------------

    # Gewonnen?
    Einser = False
    for Zeile in Seerosen:
        if 1 in Zeile:
            Einser = True
            break
    if not Einser:
        print("Lösung gefunden!")
        print(*Weg, sep="-")

        Seerosen[y][x] = '*'
        for Zeile in Seerosen:
            print(Zeile)

        return True

    # Suche.
    for r in Richtung:
        Weg.append(r)
        # Debugging -------------------------------
        # print(*Weg, sep="-")
        # -----------------------------------------
        (Erfolg, x_neu, y_neu) = gehe_nach(r, x, y)
        if Erfolg:
            if suche(r, x_neu, y_neu):
                Weg.insert(0, r)
                return True
        Weg.pop()

    Seerosen[y][x] = 1
    return False


if löse(x, y):
    print("Fertig!")
else:
    print("Keine Lösung gefunden")

print()
