# https://www.acmicpc.net/problem/17124

t = int(input())
sums = [0] * t
for i in range(t):
    len1, len2 = map(int,input().split())
    list1 = tuple(map(int,input().split()))
    list2 = list(map(int,input().split()))
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