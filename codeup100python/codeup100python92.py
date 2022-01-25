n = int(input())
calls = input().split()
for i in range(n):
    calls[i] = int(calls[i])
d = []
for k in range(24):
    d.append(0)
for c in calls :
    d[c] = d[c] + 1 
for j in range(1,24):
    print(d[j], end=" ")
