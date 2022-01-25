from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

def search(l1el, l2, len2, p):
    if l1el<l2[0]:
        return l2[0]
    if l1el>l2[len2-1]:
        return l2[len2-1]
    if l1el==l2[p]:
        return l2[p]
    if l2[p]< l1el <l2[p+1]:
        if (l2[p+1]-l1el) < (l1el-l2[p]):
            return l2[p+1]
        else: # It includes the case that if diff is same, return the smaller, l2[p]
            return l2[p]
    if l1el < l2[p]:
        p = int(p/2)
        return search(l1el, l2, len2, p)
    if l1el > l2[p]:
        p = p + int(p/2)
        return search(l1el, l2, len2, p)

t = int(stdin.readline())
r = [0] * t
for i in range(t):
    len1, len2 = map(int, stdin.readline().split())
    l1 = list(map(int,stdin.readline().split()))
    l2 = list(map(int,stdin.readline().split()))
    l3 = [0]*len1
    l2.sort()
    p = int(len2/2)
    for j in range(len1):
        gotit = search(l1[j], l2, len2, p)
        l3[j] = gotit
    r[i]=sum(l3)

for i in r:
    print(i)
