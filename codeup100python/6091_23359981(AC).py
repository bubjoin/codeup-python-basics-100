p1, p2, p3 = input().split()
p1, p2, p3 = int(p1), int(p2), int(p3)
d = 1
while True:
    if (d%p1==0) and (d%p2==0) and (d%p3==0):
        break
    d = d + 1 
    
print(d)

