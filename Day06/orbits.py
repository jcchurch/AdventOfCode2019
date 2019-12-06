def getParents(orbits, planet):
    parents = []
    while planet in orbits:
        planet = orbits[planet]
        parents.append(planet)
    return parents
 
if __name__ == '__main__':
    orbits = {}
    planets = []
    count = 0
    with open("orbits.txt") as file:
        for line in file:
            (a, b) = line.strip().split(")")
            orbits[b] = a
            planets.append(b)

    count = 0
    for p in planets:
        while p in orbits:
            count += 1
            p = orbits[p]

    santa_list = getParents(orbits, "SAN")
    you_list = getParents(orbits, "YOU")
     
    while santa_list[-1] == you_list[-1]:
          santa_list.pop()
          you_list.pop()

    print("Part 1:", count)
    print("Part 2:", len(santa_list)+len(you_list))
