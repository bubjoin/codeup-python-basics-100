n = int(input())
calls = input().split()
for i in range(n):
    calls[i] = int(calls[i])
for j in range(n-1, -1, -1):
    print(calls[j], end=' ')
    
