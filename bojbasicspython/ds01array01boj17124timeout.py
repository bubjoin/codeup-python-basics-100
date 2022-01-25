t = int(input())
tl = []
for i in range(t):
    len1, len2 = input().split()
    len1, len2 = int(len1), int(len2)
    l1 = []
    l2 = []
    tmp = input().split()
    for j in range(len1):
        l1.append(int(tmp.pop(0)))
    tmp = input().split()
    for k in range(len2):
        l2.append(int(tmp.pop(0)))
    tl.append(l1)
    tl.append(l2)

for i in range(0,t*2,2):
    l1=tl[i]
    l2=tl[i+1]
    l3 = []
    m = l2[0]
    for j in range(len(l1)):
        for k in range(len(l2)-1):
            if abs(m-l1[j]) > abs(l2[k+1]-l1[j]):
                m = l2[k+1]
            elif abs(m-l1[j])==abs(l2[k+1]-l1[j]):
                m = min(m, l2[k+1])
            else:
                pass
        l3.append(m)
    print(sum(l3))