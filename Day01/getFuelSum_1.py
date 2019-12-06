if __name__ == '__main__':
    modules = []
    with open("modules.txt") as file:
        for line in file:
            modules.append(int(line))
    print(sum([x // 3 - 2 for x in modules]))
