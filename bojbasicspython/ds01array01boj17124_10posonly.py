# https://www.acmicpc.net/problem/17124

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
        pos0 = 0
        pos2 = len2-1
        pos1 = int(len2/2)
        while True:
            if list1[j] <= list2[pos0]:
                list3[j] = list2[pos0]
                break
            elif list1[j] >= list2[pos2]:
                list3[j] = list2[pos2]
                break
            if list1[j] == list2[pos1]:
                list3[j] = list2[pos1]
                break
            elif list1[j] > list2[pos1]:
                if list1[j] < list2[pos1+1]:
                    if (list2[pos1+1]-list1[j]) < (list1[j]-list2[pos1]):
                        list3[j] = list2[pos1+1]
                    else:
                        list3[j] = list2[pos1]
                    break
                else:
                    pos0 = pos1+1
                    pos1 = int((pos2 - pos0)/2)
            else:
                if list1[j] > list2[pos1-1]:
                    if (list2[pos1]-list1[j]) < (list1[j]-list2[pos1-1]):
                        list3[j] = list2[pos1]
                    else:
                        list3[j] = list2[pos1-1]
                    break
                else:    
                    pos2 = pos1-1
                    pos1 = int((pos2 - pos0)/2)
    sums[i] = sum(list3)

for sum in sums:
    print(sum)