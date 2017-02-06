img = open("thing.ppm", "w")
img.write("P3 600 600 255")

for y in range(600):
    for x in range(600):
        n = str((x+10000)*(y+10000))
        red = int(n[-3:])
        red = red%256
        green = int(n[-6:-3])
        green = red%256
        blue = int(n[-9:-6])
        blue = red%256
        img.write(' ' + str(red) + ' ' + str(green) + ' ' + str(blue))
        
