#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

class arrayLib:
    def __init__(lib, data):
        global array
        array = data['array']


    def myLenght(lib):
        # return len(array)

        lenght = 0
        for i in range(len(array)):
            lenght += 1
        return lenght

    def maxElement(lib):
        maxElement = None

        for i in range(len(array)):
            value = array[i]

            if (maxElement is None):
                maxElement = value
            elif (len(str(value)) > len(str(maxElement))):
                maxElement = str(value)

        return maxElement

    def minElement(lib):
        minElement = None

        for i in range(len(array)):
            value = array[i]

            if (minElement is None):
                minElement = value
            elif (len(str(value)) < len(str(minElement))):
                minElement = str(value)

        return minElement

    def uppercase(lib):
        for i in range(len(array)):
            array[i] = str(array[i]).upper()
        return array

    def lowercase(lib):
        for i in range(len(array)):
            array[i] = str(array[i]).lower()
        return array

    def inverted(lib):
        out = []

        for i in range(len(array)):
            array[i] = str(array[i])

            out.append([])
            chars = []

            for char in list(array[i]):
                if (isinstance(char, str) is False):
                    chars.append(str(char))
                elif (char.isupper()):
                    chars.append(char.lower())
                elif (char.islower()):
                    chars.append(char.upper())
                else:
                    chars.append(char)

            out[i] = ''.join(chars)

        return out

    def sum(lib):
        out = 0.0

        for item in array:
            if (isinstance(item, str)):
                out += str.__hash__(item)
            elif (isinstance(item, int) or isinstance(item, float)):
                out += item
            else:
                out += str.__hash__(str(item))


        return out

    def resetAll(lib):
        out = []

        for item in array:
            out.append([])

        return out

    def reset(lib, indexOut):
        out = []

        for index in range(len(array)):
            if index != indexOut:
                out.append(array[index])

        return out

    def search(lib, string):
        if (string in array):
            return True

        return None

    def sortASC(lib):
        return sorted(array)

    def sortDESC(lib):
        return list(reversed(sorted(array)))

    def modify(lib, indexOut, string):
        out = []

        for index in range(len(array)):
            if (index != indexOut):
                out.append(array[index])
            else:
                out.append(string)

        return out

    def addElement(lib, indexOut, string):
        out = []

        for index in range(len(array)):
            if index != indexOut:
                out.append(array[index])
            else:
                out.append(string)
                out.append(array[index])

        if string not in out:
            out.append(string)

        return out

    def realCopy(lib):
        return array

    def reverse(lib):
        return list(reversed(array))

    def commonElement(lib):
        counter = {}

        for value in array:
            if value in counter:
                counter[value] += 1
            else:
                counter[value] = 1

        maxCount = 0

        for count in counter:
            if counter[count] > maxCount:
                maxCount = counter[count]

        for count in counter:
            if counter[count] == maxCount:
                return {'value': count, 'count': maxCount}

    def leastElement(lib):
        counter = {}

        for value in array:
            if value in counter:
                counter[value] += 1
            else:
                counter[value] = 1

        minCount = 99

        for count in counter:
            if counter[count] < minCount:
                minCount = counter[count]

        for count in counter:
            if counter[count] == minCount:
                return {'value': count, 'count': minCount}

    def intToDouble(lib):
        out = []

        for value in array:
            if isinstance(value, int):
                out.append(float(value))
            else:
                out.append(value)

        return out

    def doubleToInt(lib):
        out = []

        for value in array:
            if isinstance(value, float):
                out.append(int(value))
            else:
                out.append(value)

        return out

    def unicode(lib, max = 150):
        out = []

        for i in range(0, max):
            out.append(unichr(i))

        return out

    def divide(lib, indexOut):
        outOne = []
        outTwo = []

        for index in range(len(array)):
            if (index <= indexOut):
                outOne.append(array[index])
            else:
                outTwo.append(array[index])

        return (outOne, outTwo)

    def test(lib, data):
        return None, data


array = [123, 'str', 123.0, 'STR']
print(arrayLib({
    'array': array
}).myLenght())

# print(input('Code: '))
