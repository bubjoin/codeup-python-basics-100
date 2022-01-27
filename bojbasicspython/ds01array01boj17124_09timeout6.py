from sys import stdin

t = int(input())
sums = [0] * t
tlist = [[] for i in range(t)]
for i in range(t):
    len1, len2 = map(int,stdin.readline().split())
    list1 = tuple(map(int,stdin.readline().split()))
    list2 = tuple(map(int,stdin.readline().split()))
    tlist[i].append((len1,len2))
    tlist[i].append(list1)
    tlist[i].append(list2)

for i in range(t):
    len1, len2 = tlist[i][0]
    list1 = tlist[i][1]
    list2 = list(tlist[i][2])
    list2.sort()
    list3 = [0] * len1
    for j in range(len1):
        list2m = list2
        while True:
            if list1[j] <= list2m[0]:
                list3[j] = list2m[0]
                break
            if list1[j] >= list2m[len(list2m)-1]:
                list3[j] = list2m[len(list2m)-1]
                break
            pos = int(len(list2m)/2)
            if list1[j] == list2m[pos]:
                list3[j] = list2m[pos]
                break
            elif list1[j] > list2m[pos]:
                if list1[j] < list2m[pos+1]:
                    diff1 = list2m[pos+1] - list1[j]
                    diff2 = list1[j] - list2m[pos]
                    if diff1 < diff2:
                        list3[j] = list2m[pos+1]
                    else:
                        list3[j] = list2m[pos]
                    break
                list2m = list2m[pos+1:]
            else:
                if list1[j] > list2m[pos-1]:
                    diff1 = list2m[pos] - list1[j]
                    diff2 = list1[j] - list2m[pos-1]
                    if diff1 < diff2:
                        list3[j] = list2m[pos]
                    else:
                        list3[j] = list2m[pos-1]
                    break
                list2m = list2m[:pos]
    sums[i] = sum(list3)

for sum in sums:
    print(sum)