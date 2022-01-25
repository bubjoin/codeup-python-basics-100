b = [[0 for i in range(10)] for j in range(10)]
for j in range(10):
    line = input().split()
    line = list(map(int,line))
    for i in range(10):
        b[j][i] = line[i]

rp = True
bp = True
gx = 1
gy = 1
b[gx][gy] = 9

while rp or bp:
    if (b[gy][gx+1]==0)or(b[gy][gx+1]==2):
        rp = True
    else:
        rp = False
        if (b[gy+1][gx]==0)or(b[gy+1][gx]==2):
            bp = True
        else:
            bp = False
    if rp == True:
        gx = gx+1 
    elif bp == True:
        gy = gy+1
    else:
        break
    if b[gy][gx]==2:
        b[gy][gx] = 9
        break
    b[gy][gx] = 9

for j in range(10):
    for i in range(10):
        print(b[j][i], end=' ')
    print()



