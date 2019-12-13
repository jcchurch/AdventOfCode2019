import re
import sys
import math

def getMoonStr(moon):
    return "pos=<x={:2d}, y={:2d}, z={:2d}>, vel=<x={:2d}, y={:2d}, z={:2d}>".format(
        moon['pos']['x'],
        moon['pos']['y'],
        moon['pos']['z'],
        moon['vel']['x'],
        moon['vel']['y'],
        moon['vel']['z'])

def updateVelocityOnAxis(moonA, moonB, axis):
    if moonA['pos'][axis] > moonB['pos'][axis]:
        moonA['vel'][axis] -= 1
    if moonA['pos'][axis] < moonB['pos'][axis]:
        moonA['vel'][axis] += 1

def updatePositionOnAxis(moon, axis):
    moon['pos'][axis] += moon['vel'][axis]

def computeEnergyType(moon, axes, etype):
    return sum([math.fabs(moon[etype][axis]) for axis in axes])

def computeMoonEnergy(moon, axes):
    return computeEnergyType(moon, axes, 'pos') * computeEnergyType(moon, axes, 'vel')

def computeTotalEnergy(moons, axes):
    return sum([computeMoonEnergy(moon, axes) for moon in moons])

def getFactors(x):
    factors = []
    factor = 2
    num = x
    while num > 1:
        if num % factor == 0:
            factors.append(factor)
            num //= factor
        else:
            factor += 1
    return factors

if __name__ == '__main__':
    moons = []
    regex = "<x=(-?\d+), y=(-?\d+), z=(-?\d+)>"
    with open(sys.argv[1]) as file:
        for line in file:
            moon = {}
            moon['pos'] = {}
            moon['vel'] = {}
            matches = re.match(regex, line.strip())
            moon['pos']['x'] = int(matches.group(1))
            moon['pos']['y'] = int(matches.group(2))
            moon['pos']['z'] = int(matches.group(3))
            moon['vel']['x'] = 0
            moon['vel']['y'] = 0
            moon['vel']['z'] = 0
            moons.append(moon)

    steps = 1000
    axes = ['x', 'y', 'z']
    parts = ['pos'] # , 'vel']

    for step in range(steps):
        for i in range(len(moons)):
            for j in range(len(moons)):
                if i != j:
                    for axis in axes:
                        updateVelocityOnAxis(moons[i], moons[j], axis)

        for i in range(len(moons)):
            for axis in axes:
                updatePositionOnAxis(moons[i], axis)

    # This is going to be hacky, but what isn't these days?

    step = 0
    cycles_found = 0
    buffer_needed = 20
    buffer_index = 0
    cycles_needed = len(moons) * len(axes) * len(parts)

    cycles = []
    for moon in moons:
        cycle = {}
        for axis in axes:
            for part in parts:
                cycle[axis+part] = {}
                cycle[axis+part]['start'] = []
                cycle[axis+part]['end'] = []
                cycle[axis+part]['length'] = -1
        cycles.append(cycle)

    while cycles_found < cycles_needed:
        for i in range(len(moons)):
            for j in range(len(moons)):
                if i != j:
                    for axis in axes:
                        updateVelocityOnAxis(moons[i], moons[j], axis)

        for i in range(len(moons)):
            for axis in axes:
                updatePositionOnAxis(moons[i], axis)

        if buffer_index < buffer_needed:
            for i in range(len(moons)):
                for part in parts:
                    for axis in axes:
                        cycles[i][axis+part]['start'].append(moons[i][part][axis])

        for i in range(len(moons)):
            for part in parts:
                for axis in axes:
                    cycles[i][axis+part]['end'].append(moons[i][part][axis])

                    if len(cycles[i][axis+part]['end']) > buffer_needed:
                        cycles[i][axis+part]['end'].pop(0) # Probably slow

        found = ""
        if buffer_index > buffer_needed+1:
            for i in range(len(moons)):
                for part in parts:
                    for axis in axes:
                        if cycles[i][axis+part]['start'] == cycles[i][axis+part]['end'] and cycles[i][axis+part]['length'] == -1:
                            cycles[i][axis+part]['length'] = buffer_index + 1 - buffer_needed
                            cycles_found += 1
                            print(cycles[i][axis+part]['length'],":",str(i)+axis+part)

        """
        print(buffer_index, end=" ==>\t")
        for i in range(len(moons)):
            for axis in axes:
                for part in parts:
                    print(moons[i][part][axis], end="\t")
        print(computeTotalEnergy(moons, axes), end=" ")

        print(found)
        """

        buffer_index += 1

    print(buffer_index)

    factor_dictionary = {}
    for i in range(len(moons)):
        for part in parts:
            for axis in axes:
                factors = getFactors(cycles[i][axis+part]['length'])
                print(str(i)+axis+part, factors)
                these_factors = {}
                for factor in factors:
                    these_factors[factor] = these_factors.get(factor, 0) + 1

                    if factor_dictionary.get(factor, 0) < these_factors[factor]:
                        factor_dictionary[factor] = these_factors[factor]

    final = 1
    for key in factor_dictionary:
        final *= key ** factor_dictionary[key]

    print(factor_dictionary)
    print(final)

    for moon in moons:
        print(getMoonStr(moon))
