from sys import stdin

t = int(stdin.readline())
r = [0] * t
for i in range(t):
    len1, len2 = map(int, stdin.readline().split())
    l1 = list(map(int,stdin.readline().split()))
    l2 = list(map(int,stdin.readline().split()))
    l3 = [0]*len1
    m = l2[0]
    for j in range(len1):
        for k in range(len2-1):
            if abs(m-l1[j]) > abs(l2[k+1]-l1[j]):
                m = l2[k+1]
            elif abs(m-l1[j])==abs(l2[k+1]-l1[j]):
                m = min(m, l2[k+1])
            else:
                pass
        l3[j] = m
    r[i]=sum(l3)

for i in r:
    print(i)