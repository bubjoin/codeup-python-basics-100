n = int(input())
calls = input().split()

for i in range(n):
    calls[i] = int(calls[i])

min = calls[0]

for i in range(n):
    if calls[i] < min :
        min = calls[i]
        
print(min)
