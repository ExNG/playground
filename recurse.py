#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

def palindrom(data, start = None, end = None):
    if (isinstance(data, str)):
        data = list(data)

    if (start > len(data) - 1):
        return True

    if (start is None):
        start = 0
    if (end is None):
        end = len(data) - 1

    if (start >= end and len(data) % 2 == 1):
        return True

    bool = data[start] == data[end] and \
        palindrom(data, start + 1, end - 1)

    return bool

def addUp(base, first = None, second = None):
    if (first is None):
        first = base
    if (second is None):
        second = base

    if (second == 1):
        return 1

    return addUp(base, first + 1, second - 1) + addUp(base, first + 1, second - 1)

def checksum(number, index = None):
    if (isinstance(number, int)):
        number = list(str(number))
    if (index == None):
        index = 0
    if (index > len(number) - 1):
        return 0

    return int(number[index]) + int(checksum(number, index + 1))

def prime(limit = 1, number = None, out = []):
    def iterateNumbers(number, limit):
        if(number > limit):
            return

        def isPrime(number, i = 2):
            calc = number % i

            if (number == 2):
                return False

            if (i >= number):
                return True

            if ((number % i) == 0 or i == number):
                return False
            else:
                return isPrime(number, i + 1)

        if (isPrime(number)):
            out.append(number)
        return iterateNumbers(number + 1, limit)

    if (number is None):
        number = 1

    iterateNumbers(number, limit)
    return out


print(prime(100))
