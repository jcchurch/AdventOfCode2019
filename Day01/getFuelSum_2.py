def getFuel(x):
    fuel = x // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + getFuel(fuel)

if __name__ == '__main__':
    modules = []
    with open("modules.txt") as file:
        for line in file:
            modules.append(int(line))
    print(sum([getFuel(x) for x in modules]))
