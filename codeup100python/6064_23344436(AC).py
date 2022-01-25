a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
min = a if a < b else b
min = min if min < c else c 
print(min)
