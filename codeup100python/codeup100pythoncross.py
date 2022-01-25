d = [[0 for j in range(20)] for k in range(20)]

for j in range(1,20):
        l = input().split()
        l = list(map(int,l))
    for k in range(1,20):
        d[j][k] = l[k-1]

n = int(input())
for i in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    for j in range(1,20):
        if d[j][y] == 0:
            d[j][y] = 1 
        else:
            d[j][y] = 0 
    for k in range(1,20):
        if d[x][k] == 0:
            d[x][k] = 1 
        else:
            d[x][k] = 0 

for j in range(1, 20):
    for k in range(1, 20):
        print(d[j][k], end=' ')
    print()
