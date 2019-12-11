import sys
import math

def abs(x):
    if x < 0:
        return -x
    return x

def sign(x):
    if x < 0:
        return -1
    return 1

if __name__ == '__main__':
    data = []
    with open(sys.argv[1]) as file:
        for line in file:
            data.append(line.strip())

    width = len(data[0])
    height = len(data)
    amap = [0] * height
    mymap = [0] * height
    for h in range(height):
        mymap[h] = [0] * width
        amap[h] = list(data[h])

    astroids = []

    for h in range(height):
        for w in range(width):
            if data[h][w] == '#':
                astroids.append((w,h))

    bx = -1
    by = -1
    best_seen = 0
    for (x,y) in astroids:
        for (p,q) in astroids:
            if x != p or y != q:
                vx = p - x
                vy = q - y

                avx = abs(vx)
                avy = abs(vy)

                factor = 2
                best_factor = 1
                while factor <= avx and factor <= avy:
                    if avx % factor == 0 and avy % factor == 0:
                        best_factor = factor
                    factor += 1

                if avx == 0:
                    dx = 0
                    dy = sign(vy)
                elif avy == 0:
                    dx = sign(vx)
                    dy = 0
                else:
                    dx = vx // best_factor
                    dy = vy // best_factor

                rayx = x + dx
                rayy = y + dy
                while data[rayy][rayx] != '#':
                    rayx += dx
                    rayy += dy

                if rayx == p and rayy == q:
                    mymap[y][x] += 1

                    if mymap[y][x] > best_seen:
                        best_seen = mymap[y][x]
                        bx = x
                        by = y

    print("First:", best_seen)

    to_bomb = []
    for (x,y) in astroids:
        degree = 10000
        if x != bx or y != by:
            vx = x - bx
            vy = y - by

            dist = (vx * vx + vy * vy) ** 0.5
            ux = vx / dist 
            uy = vy / dist
            theta = math.pi + math.atan2(-ux,uy)
            to_bomb.append((x, y, ux, uy, dist, theta))

    vaporized = 0
    lastx = -1
    lasty = -1
    last_theta = -0.001

    while len(to_bomb) > 0 and vaporized < 200:
        best = -1
        nearest = 10000
        smallest_theta = 10000
        for b in range(len(to_bomb)):
            (x, y, ux, uy, dist, theta) = to_bomb[b]

            # Find smallest_theta that is still greater than last theta
            if theta < smallest_theta and theta > last_theta:
                smallest_theta = theta
                nearest = dist
                best = b

            elif theta == smallest_theta:
                if dist < nearest:
                    nearest = dist
                    best = b

        if best >= 0:
            (x, y, ux, uy, dist, theta) = to_bomb[best]
            lastx = x
            lasty = y
            last_theta = theta
            to_bomb.pop(best)
            vaporized += 1
        else:
            last_theta = -0.001
            

    print("Second:", lastx * 100 + lasty)
