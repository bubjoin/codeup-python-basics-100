r, g, b = input().split()
r, g, b = int(r), int(g), int(b)
n = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            n += 1 
print(n)
