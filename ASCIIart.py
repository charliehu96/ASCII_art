from PIL import Image
import numpy as np
import sys

max_size = (100,100)
mapping = list('`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$')

with Image.open("Eevee2.jpg") as im:
    im.thumbnail(max_size)
    pixels = np.array(im)
    print("Picture size: " + str(im.size))

print("Iterating through pixel contents")
print(len(pixels))
brightness = np.empty(im.size[::-1], dtype=int)

for x in range(len(pixels)):
    for y in range(len(pixels[x])):
        brightness[x][y] = int(np.round((0.21*pixels[x][y][0] + 0.72*pixels[x][y][1] + 0.07*pixels[x][y][2])/255*100/100*64))

print("Iterating through pixel brightness")

ascii_art = np.empty(im.size[::-1], dtype=str)

for x in range(len(brightness)):
    for y in range(len(brightness[x])):
        # print(int(brightness[x][y]))
        ascii_art[x][y] = mapping[int(brightness[x][y])]
        # print(ascii_art[x][y])

print("Printing ASCII-ART:")
for x in ascii_art:
    for i, y in enumerate(x):
        if not i:
            print()
        sys.stdout.write(y)
        sys.stdout.write(y)