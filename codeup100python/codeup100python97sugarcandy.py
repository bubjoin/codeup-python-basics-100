h, w = input().split()
h, w = int(h), int(w)
n = int(input())
ldxy = []
for ni in range(n):  
    l, d, x, y = input().split()
    l, d, x, y = int(l), int(d), int(x), int(y)
    ldxy.append([l,d,x,y])

b = [[ 0 for i in range(w)] for j in range(h)]

for ni in range(n):
    for li in range(ldxy[ni][0]):
        if ldxy[ni][1] == 0:
            for yi in range(ldxy[ni][3]-1, (ldxy[ni][3]-1)+(ldxy[ni][0]-1)+1):
                b[ldxy[ni][2]-1][yi] = 1
        elif ldxy[ni][1] == 1:
            for xi in range(ldxy[ni][2]-1, (ldxy[ni][2]-1)+(ldxy[ni][0]-1)+1):
                b[xi][ldxy[ni][3]-1] = 1 

for i in range(h):
    for j in range(w):
        print(b[i][j], end=' ')
    print()
