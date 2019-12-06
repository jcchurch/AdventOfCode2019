if __name__ == '__main__':
    low = 165432
    high = 707912

    i = low
    count = 0
    while i <= high:

        top = i % 10
        decreasing = i // 10
        isDecreasing = True
        while decreasing > 0 and decreasing % 10 <= top:
            top = decreasing % 10
            decreasing //= 10

        if decreasing > 0:
            isDecreasing = False

        asString = str(i)
        containsDouble = False
        if (asString[0] == asString[1] and asString[1] != asString[2]) or \
           (asString[0] != asString[1] and asString[1] == asString[2] and asString[2] != asString[3]) or \
           (asString[1] != asString[2] and asString[2] == asString[3] and asString[3] != asString[4]) or \
           (asString[2] != asString[3] and asString[3] == asString[4] and asString[4] != asString[5]) or \
           (asString[3] != asString[4] and asString[4] == asString[5]):
           containsDouble = True

        if isDecreasing and containsDouble:
            count += 1

        i += 1
    print(count)

