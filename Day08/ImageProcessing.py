import sys

if __name__ == '__main__':
    data = ""
    with open(sys.argv[1]) as file:
        for line in file:
            data += line.strip()

    colors = [' ', '#']
    width = 25
    height = 6
    bytes = height * width
    image = [0] * height
    for h in range(height):
        image[h] = [2] * width

    i = 0
    best = bytes
    onesTimesTwos = 0
    while i < len(data):
        layer = data[i:i+bytes]
        zeros = layer.count("0")
        ones = layer.count("1")
        twos = layer.count("2")

        for h in range(height):
            for w in range(width):
                pixel = int(layer[h * width + w])
                if pixel != 2 and image[h][w] == 2:
                    image[h][w] = colors[pixel]

        if zeros < best:
            best = zeros
            onesTimesTwos = ones * twos
        i += bytes

    print("First:", onesTimesTwos)
    print("Second:")
    for h in range(height):
        print("".join(image[h]))

