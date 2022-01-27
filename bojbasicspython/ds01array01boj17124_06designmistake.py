from sys import stdin

t = int(input())
sums = [0] * t
for i in range(t):
    len1, len2 = map(int,stdin.readline().split())
    list1 = list(map(int,stdin.readline().split()))
    list2 = list(map(int,stdin.readline().split()))
    list2.sort()
    list3 = [0] * len1
    for j in range(len1):
        if list1[j] <= list2[0]:
            list3[j] = list2[0]
        elif list1[j] >= list2[len2-1]:
            list3[j] = list2[len2-1]
        else:
            pos = int(len2/2)
            while True:
                if list1[j] == list2[pos]:
                    list3[j] = list2[pos]
                    break
                elif list1[j] > list2[pos]:
                    if list1[j] < list2[pos+1]:
                        diff1 = list2[pos+1] - list1[j]
                        diff2 = list1[j] - list2[pos]
                        if diff1 < diff2:
                            list3[j] = list2[pos+1]
                        else:
                            list3[j] = list2[pos]
                        break
                    pos = pos + int(pos/2)
                else:
                    if list1[j] > list2[pos-1]:
                        diff1 = list2[pos] - list1[j]
                        diff2 = list1[j] - list2[pos-1]
                        if diff1 < diff2:
                            list3[j] = list2[pos]
                        else:
                            list3[j] = list2[pos-1]
                        break
                    pos = int(pos/2)
    sums[i] = sum(list3)

for sum in sums:
    print(sum)