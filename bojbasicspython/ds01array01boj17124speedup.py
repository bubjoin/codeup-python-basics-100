from sys import stdin

t = int(stdin.readline())
tl = [0]*t*3
for i in range(0, t*3, 3):
    len1, len2 = map(int, stdin.readline().split())
    l1 = list(map(int,stdin.readline().split()))
    l2 = list(map(int,stdin.readline().split()))
    tl[i]=(len1,len2)
    tl[i+1]=l1
    tl[i+2]=l2

for i in range(0,t*3,3):
    l1 = tl[i+1]
    l2 = tl[i+2]
    len1 = tl[i][0]
    len2 = tl[i][1]
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
    print(sum(l3))