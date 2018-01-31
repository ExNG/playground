#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

functioName = None

# Aufgabe: 7

# def aufgabe7():
#     print('Quadratzahlanzahl: ')
#     zahl = int(input())
#
#     i = 0
#
#     while (i < zahl):
#         print i*i
#         i += 1
#
# # Aufgabe: 8
#
# def aufgabe8():
#     zahl = 0
#     i = 0
#
#     while (zahl < 441):
#         zahl = i * i
#         print zahl
#         i += 1
#
# # Aufgabe: 9
#
# def aufgabe9():
#     zahl = 0
#     i = 0
#
#     while (zahl <= 123456):
#         zahl = i * i
#         i += 1
#
#     print i
#
# # Aufgabe: 10
#
# def aufgabe10():
#     summe = 0
#     pos = 42
#     i = 0
#
#     while (summe < pos):
#         if (i%2):
#             summe += 1
#             print 'Zahl: ' + str(i) + ' POS: ' + str(summe)
#         i += 1
#
# # Aufgabe: 11
#
# def aufgabe11():
#     jahre = 10
#     zins = 3.0
#     kapital = 100.0
#     i = 0
#
#     while (i < jahre):
#         kapital = kapital * (zins / 100  + 1)
#         i += 1
#
#     kapital = round(kapital, 2)
#     print 'Kontostand: ' + str(kapital) + ' Zins: ' + str(zins / 100  + 1)
#
# # Aufgabe: 12
#
# def aufgabe12():
#     print 'zähler wird nicht incrementiert'
#
# # Aufgabe: 13
#
# def aufgabe13():
#     vorgaenger = 1
#     vorgaenger2 = 0
#     nummer = 0
#     schritte = 50
#     i = 0
#
#     while (i < schritte):
#         print 'Schritt: ' + str(i + 1) + ' Nummer: ' + str(int(nummer))
#
#         vorgaenger2 = vorgaenger
#         vorgaenger = nummer
#
#         nummer = vorgaenger + vorgaenger2
#
#         i += 1
#
# # Aufgabe: 14
#
# def aufgabe14():
#     print 'Zahl eingeben: '
#     zahl = input()
#     i = 2
#
#     # for i in range(2,zahl):
#     #    if (zahl % i) == 0:
#     #        print zahl,"is not a prime number"
#     #        print i,"times",zahl//i,"is",zahl
#     #        break
#     #    else:
#     #        print zahl, "is a prime number"
#     #
#     # print ((zahl % i) == 0)
#     # while (bool(true)):
#     #     if
#
#     while (i < zahl):
#         if ((zahl % i) == 0):
#             print str(zahl) + ' ist keine Primzahl'
#             break
#         else:
#             print str(zahl) + ' ist eine Primzahl'
#             break
#         i += 1
#
# # 1000 Primzahlen
#
# def isPrime(zahl):
#     i = 2
#
#     while (i < zahl):
#
#         print 'HIER: ' + str(zahl % i)
#
#         if ((zahl % i) == 0):
#             # return False
#             break
#         else:
#             print str(zahl) + ' ist eine Primzahl'
#             return True
#             break
#         i += 1
#
# # def prim1000():
# #     for (nummer in range(2, 1000)):
# #         print str(nummer)
#
# def testPrime():
#     i = 2
#     nummer = 2
#
#     while (i < 10):
#         testOutput = isPrime(nummer)
#
#         if (testOutput is True):
#             i += 1
#
#         nummer += 1
#
#         # print str(i)
#
#
# def weih1():
#     stufen = 3
#     hoehe = 8
#
#     currentStufe = 0
#
#     while (currentStufe < stufen):
#         currentHoehe = 0
#
#         i = 0
#
#         while (currentHoehe < hoehe):
#
#             sternchen = '**' * i
#             print '*' + sternchen
#
#             i += 1
#             currentHoehe += 1
#
#         currentStufe += 1
#
#
# def weih2():
#     hoehe = 25
#     i = 0
#
#     while (i < hoehe):
#         leftWhitespaces = ' ' * (hoehe - i - 1)
#
#         print leftWhitespaces + '*' + ('**' * i)
#
#         i += 1
#
#     whitespaces = ' ' * (hoehe - 1)
#     print whitespaces + 'I'
#
#
#
#
#
#
#
#
# from random import *
#
# red = '\033[91m'
# end = '\033[0m'
#
# def getRandomRow(lenght):
#     i = 0
#     out = ''
#     whitespaces = ''
#
#     difference = (2 * randint(-2, 0))
#
#     oldLenght = lenght
#
#     if (oldLenght >= 10):
#         lenght += difference
#         if (difference <= -1):
#             whitespaces = ' ' * (-difference * 2)
#
#     while (i < lenght + 1):
#         if (randint(0, 100) <= 10):
#             out = out + '°'
#         else:
#             out = out + '*'
#         i += 1
#
#     if (lenght % 3 is 2):
#         out = '|' + out + '|'
#
#     return whitespaces + out
#
# def weih3():
#     hoehe = 15
#     i = 0
#
#     while (i < hoehe):
#         whitespaces = ' ' * ((hoehe + (1 * hoehe)) / 2 - i - 1)
#         if ((2 * i) % 3 is 2):
#             whitespaces = ' ' * ((hoehe + (1 * hoehe)) / 2 - i - 2)
#         # print whitespaces + getRandomRow(i + (1 * i))
#         out = getRandomRow(2 * i)
#         whitespaces = int(hoehe - len(out))
#         print str(' ' * whitespaces) + out
#
#         i += 1
#
#         # if (i % 3 is 1):
#         #     ii = i - 1
#         # print red + str(len(getRandomRow(2 * int(i)))) + end
#         # else:
#         #     ii = i
#
#     i = 0
#     whitespaces = ' ' * (hoehe - 2)
#
#     while (i < 3):
#         print whitespaces + '###'
#         i += 1


def aufgabe1():
    zahl = 0
    summe = 0

    while(zahl <= 7):
        summe += zahl
        zahl += 1

    print(str(summe))


def aufgabe2():
    summe = 0
    zahl = 1

    while (zahl <= 7):
        summe += zahl
        zahl += 1

    print(str(summe))


def aufgabe3():
    fac = 1

    zahl = int(input('Zahl: '))

    for number in range(1, zahl + 1):
        fac *= number

    print(str(fac))


def aufgabe5():
    # x = int(input('x: '))
    # y = int(input('y: '))

    x = 1337
    y = 1337

    while (x != y):
        if (x < y):
            y = y - x
        else:
            x = x - y
    else:
        print(str(x))


def aufgabe6():
    # basis = int(input('Zahl (Basis): '))
    # exponent = int(input('Zahl (Exponent): '))

    basis = 12
    exponent = 12

    out = int(basis)

    for i in range(exponent - 1):
        out = out * basis

    # out = basis ** exponent

    print(out)

def aufgabe7():
    zahlen = 20

    out = []

    for nummer in range(1, zahlen):
        quadrat = int(nummer ** 2)
        out.append(str(quadrat))

    print(out)


def aufgabe8():
    maximum = 441

    i = 1
    out = []

    while True:
        quadrat = int(i ** 2)

        if (quadrat <= maximum):
            out.append(str(quadrat))
        else:
            break

        i += 1

    print(out)


def aufgabe9():
    maximum = 123201

    i = 1
    out = []

    while True:
        quadrat = int(i ** 2)

        if (quadrat <= maximum):
            out.append(str(quadrat))
        else:
            break

        i += 1

    print(len(out))


def aufgabe10():
    zahlen = []
    i = 1

    while len(zahlen) < 42:
        if (i % 2 != 0):
            zahlen.append(i)
        i += 1

    out = 0

    for zahl in zahlen:
        out += zahl

    print(out)

    return


def aufgabe11():
    kapital = 100.00
    laufzeit = 10 #Jahre
    zinsen = 4 #%

    out = float(kapital)
    zinsen = float(zinsen) / 100 + 1

    for jahr in range(laufzeit):
        out = out * zinsen

    out = round(out, 2)

    print(out)

    return


# Aufgabe 12: "Bitte nicht nachmachen!" wird in die console gespammt


def aufgabe13():
    numbers = [0, 1]
    i = 0

    childs = 50

    for r in range(1, childs):
        child = int(numbers[i] + numbers[i + 1])
        numbers.append(child)
        i += 1

    for index, value in enumerate(numbers):
        print(index, value)

    return

def aufgabe14():
    number = int(input('Beliebige zahl (größer als 1): '))

    if number <= 1:
        print('zu klein')

    for i in range(2, number):
        if (number % i) == 0:
            print('no prime')
            break
    else:
        print('prime')

    return


def aufgabe15():
    nummer = str(int(input('zahl: ')))

    nummern = list(nummer)
    out = 0

    for nummer in nummern:
        out += int(nummer)

    print(out)

    return

def aufgabe16():
    def quersumme(nummer):
        nummern = list(str(nummer))
        out = 0

        for nummer in nummern:
            out += int(nummer)
        return out

    def primezahl(zahl):
        if zahl <= 1:
            return False

        for i in range(2, zahl):
            if (zahl % i) == 0:
                return False
                break
        else:
            return True
        return 'error'

    out = []
    i  = 0

    while len(out) < 1000:
        if (primezahl(i)):
            if (quersumme(i) > 10):
                out.append(str(i))
        i += 1

    print(list(enumerate(out)))

    return


def aufgabe17():
    """ The eZ way """
    # print(str(bin(int(input('Zahl: ')))))

    # number = int(input('Zahl: '))
    number = 99999999999999999999999
    out = {}
    print('Number: ' + str(number))

    i = 0

    while ((2 ** i) < number):
        i += 1

    dividers = []

    for i in range(i + 1):
        dividers.append(2 ** i)

    for divider in reversed(dividers):
        if (divider <= number):
            number = int(number - divider)
            out[divider] = 1
        else:
            out[divider] = 0

    if (list(out.values())[0] == 0):
        out.pop(list(out.keys())[0], None)

    print(list(out.values()))

    return


def aufgabe18():
    number1 = int(input('Zahl 1: '))
    number2 = int(input('Zahl 2: '))

    def divisors(number):
        number = int(number)
        out = []

        i = 1

        while (i < number):
            if (number % i == 0):
                out.append(i)
            i += 1

        return out

    sumNumber1 = 0

    for divisor in divisors(number1):
        sumNumber1 += divisor

    sumNumber2 = 0

    for divisor in divisors(number2):
        sumNumber2 += divisor

    if (number2 == sumNumber1 and number1 == sumNumber2):
        print(str(number1) + ' und ' + str(number2) + ' sind befreundet')
    else:
        print(str(number1) + ' und ' + str(number2) + ' sind nicht befreundet')

        print(sumNumber1)
        print(sumNumber2)

    return



def aufgabe19():
    def checkFriends(number1, number2):
        def divisors(number):
            number = int(number)
            out = []

            i = 1

            while (i < number):
                if (number % i == 0):
                    out.append(i)
                i += 1

            return out

        sumNumber1 = 0

        for divisor in divisors(number1):
            sumNumber1 += divisor

        sumNumber2 = 0

        for divisor in divisors(number2):
            sumNumber2 += divisor

        if (number2 == sumNumber1 and number1 == sumNumber2):
            return True
        else:
            return False

    maxNumber = 10000000
    step = 2
    out = []
    numbers = []
    # out = [(284, 220), (1210, 1184), (2924, 2620)]
    # numbers = [284, 220, 1210, 1184, 2924, 2620]

    def sortOutOdds(range):
        out = []

        for number in range:
            if (number % 2 == 0):
                out.append(number)

        return out

    for number1 in sortOutOdds(range(0, maxNumber, step)):
        if (len(out) >= 3):
            break

        for number2 in sortOutOdds(range(0, number1, step)):
            # debugOut = str(number1) + ' : ' + str(number2)
            # print(debugOut, end="\r")

            if (len(out) >= 3):
                break

            if (number2 != number1 and number1 not in numbers):

                if checkFriends(number1, number2):
                    out.append((number1, number2))
                    numbers.append(number1)
                    numbers.append(number2)

                    print(out)
                    # print(numbers)

    print('\nFinished, Results:')
    print(out)

    return


def passwort():
    from random import randint, shuffle
    from string import digits, punctuation, ascii_letters

    parameter = {
        'numbers': 2,
        'chars': 2,
        'letters': 4
    }

    password = []
    for i in range(0, int(parameter['numbers'])):
        password.extend(
            str(
                list(digits)[randint(0,
                                     len(list(digits)) - 1
                )]
            )
        )

    for i in range(0, int(parameter['chars'])):
        password.extend(str(list(punctuation)[randint(0, len(list(punctuation)) - 1)]))

    for i in range(0, int(parameter['letters'])):
        password.extend(str(list(ascii_letters)[randint(0, len(list(ascii_letters)) - 1)]))

    shuffle(password)
    print(''.join(password))

    return










functioName = 'passwort'

if (functioName is None):
    functioName = str(input('function name: '))
else:
    functioName += '()'

exec(functioName)
