#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

days = [
    12,
    14,
    9,
    12,
    15,
    16,
    15,
    15,
    11,
    8,
    13,
    13,
    15,
    12
]

def zweiWochen(woche = 1):
    i = woche * 7 - 7
    sum = 0

    while (i < 14):
        sum += days[i]
        i += 1

    print(round(sum / i))


def maxAndMin():
    minTemp = days[0]
    maxTemp = days[0]

    for temp in days:
        if (temp < minTemp):
            minTemp = temp

        if (temp > maxTemp):
            maxTemp = temp

    print('Höchste Temperatur: ' + str(maxTemp) + ' Minimale Temperatur: ' + str(minTemp))


def highestDifference():
    i = 1
    first = days[0]
    second = days[1]
    difference = abs(first - second)

    while (i < len(days) - 1):
        if (abs(days[i] - days[i + 1]) > difference):
            first = i
            second = i + 1
            difference = abs(days[i] - days[i + 1])

        i += 1

    print('Day ' + str(first) + '(' + str(days[first]) + '°C) and ' + str(second) + '(' + str(days[second]) + '°C) had a ' + str(difference) + '°C difference')


def printTable():
    print('Day Temperatur')
    print('--------------')
    for index, day in enumerate(days):
        whitespaces = ' ' * int(4 - len( str(index))) + '      '

        if (len(str(day)) == 1 and len(str(int(index + 1))) <= 1):
            whitespaces += ' '

        print(str(index + 1) + whitespaces + str(day) + '°C')


def aufgabe6(array):
    """ LAZY WAY: """
    # print(str(array[-1]))

    print(str(array[len(array) - 1]))


def aufgabe9(array, term):
    for index, value in enumerate(array):
        if (value is term):
            print(str(value) + ' is at ' + str(index - 1))


def aufgabe12(input):
    # print(input)

    out = []
    for ar in input:
        out.extend(ar)

    runs = len(input) * len(out)
    run = 0

    while (run < runs):
        i = 0
        while (i < len(out) - 1):
            if (out[i] > out[i + 1]):
                # print(out[i] > out[i + 1], out[i], out[i + 1])
                out[i], out[i + 1] = out[i + 1], out[i]
            i += 1
        run += 1
    print(' '.join(out))


def aufgabe14():
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 4, 5]

    if (a == b):
        print(True)
    else:
        print(False)


def aufgabe15(N):
    import numpy as np

    # N  = 5
    magic_square = np.zeros((N,N), dtype=int)

    n = 1
    x, y = 0, N//2

    while n <= N**2:
        magic_square[x, y] = n
        n += 1
        new_x, new_y = (x-1) % N, (y+1)% N
        if magic_square[new_x, new_y]:
            x += 1
        else:
            x, y = new_x, new_y

    print(magic_square)


def aufgabe16():
    array = [
        [3, 3],
        [5, -3],
        [1, 3],
        [0, -2],
        [5, -2]
    ]

    newArray = []
    # Für jede Spalte eine neue Zeile
    for x in range(0, len(array[0])):
        newArray.append([])
        # alte Spalten in neue Zeilen
        for y in range(0, len(array)):
            # x => y; y => x
            newArray[x].append(array[y][x])

    print(array)
    """ [[3, 3],
        [5, -3],
        [1, 3],
        [0, -2],
        [5, -2]]"""

    print(newArray)
    """[[3, 5, 1, 0, 5],
       [3, -3, 3, -2, -2]]"""


def aufgabe17():
    """ eZ way:
        import numpy as np

        print(np.array([1, 2]) + np.array([2, 1])) # [3, 3]

        The wanted way:
    """

    x = [
        [1, 200, 100],
        [1, 2, 100]
    ]
    y = [
        [1, 200, 100],
        [1, 2, 100]
    ]

    if (len(x) is len(y)):
        if (len(x[0]) >= 1 and len(y[0]) >= 1):
            matrix_rows = (len(x) + len(y)) / 2

            x_lenghts = 0
            for array in x:
                x_lenghts += len(array)
            x_lenghts = (x_lenghts / matrix_rows)

            y_lenghts = 0
            for array in y:
                y_lenghts += len(array)
            y_lenghts = (y_lenghts / matrix_rows)

            condition = bool(
                x_lenghts is y_lenghts and
                (x_lenghts % 2 is not 0.5 and matrix_rows % 2 is not 0.5)
            )

            if (condition):

                newArray = []

                for row_index, x_row in enumerate(x):
                    newArray.append([])
                    for value_index, x_value in enumerate(x_row):
                        newArray[row_index].append(
                            int(x[row_index][value_index]) + int(y[row_index][value_index])
                        )

                print(newArray)

            else:
                print('Did not work')


def aufgabe18():

    """   DOES NOT WORK   """

    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    b = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    if (len(a[0]) is len(b)):
        newArray = []
        for row_index, a_row in enumerate(a):

            newRow = []

            for index, muliplicator in enumerate(a_row):
                newRow.append(int(
                    a[row_index][index] * muliplicators[index]
                ))


            print(newRow)
            newArray.append(newRow)

        print(newArray)


def aufgabe19():
    root = []
    antworten = {
        'gruppe': 2,
        'proband': 5,
        'fragebogen': 7,
        'frage': 4,
        'antworten': [
            'Ja',
            'Nein',
            'Ja'
        ]
    }

    # Gruppen
    for gruppe in range(3):
        root.append([])

        # Probanden
        for proband in range(15):
            root[gruppe].append([])

            # Fragebögen
            for fragebogen in range(10):
                root[gruppe][proband].append([])

                # Fragen
                for frage in range(12):
                    root[gruppe][proband][fragebogen].append([])

                    # Antworten
                    root[gruppe][proband][fragebogen][frage] = [
                        'Bitte speichern',
                        'sie die antworten',
                        'des Probanden'
                    ]

                    root[gruppe][proband][fragebogen][frage] = ' '.join(root[gruppe][proband][fragebogen][frage])

    root[2][5][7][4] = [
        'Ja',
        'Nein',
        'Ja'
    ]

    print(root[2][5][7][4])


def aufgabe20():
    height = 5
    depth = 5
    triangle = []

    for a in range(height):
        triangle.append([])

        i = 0

        while (i < a):

            if (i == 0):
                triangle[a].append([1])
            else:
                print ('a: ' + str(a))
                print ('i: ' + str(i))
                before = triangle[a - 1][i - 2]
                print(before)

                # triangle[a].append([
                #     triangle[a - 2][i - 2] + triangle[a - 1][i - 1]
                # ])

            i += 1

    print(triangle)


from random import *
def aufgabe21():

    i = 0
    numbers = []

    while (i < 6):
        number = randint(1, 49)

        if (number not in numbers):
            numbers.append(number)
            i += 1

    print(sorted(numbers))


def aufgabe22():
    originalWord = 'lageregal'
    reversedWord = ''.join(
        reversed(
            list(originalWord)
        )
    )

    if (originalWord == reversedWord):
        print('It`s a Palindrom')
    else:
        print('It`s not')









# from graphics import *
# def main():
#     win = GraphWin("Pause", 100, 1000)
#     win.getMouse() # pause for click in window
#     win.close()
# main()





aufgabe22()
# aufgabe12([
#     ['c', 's', 'M'],
#     ['h', 'A', 'R'],
#     ['d', 'F', 'r'],
#     ['D', 'H', 'z'],
#     ['L', 'H', 'k']
# ])
