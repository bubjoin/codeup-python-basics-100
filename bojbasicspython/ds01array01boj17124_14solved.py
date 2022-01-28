# https://www.acmicpc.net/problem/17124
from sys import stdin

t = int(stdin.readline())
sums = [0] * t
for i in range(t):
    len1, len2 = map(int,stdin.readline().split())
    list1 = tuple(map(int,stdin.readline().split()))
    list2 = list(map(int,stdin.readline().split()))
    list2.sort()
    list3 = [0] * len1
    for j in range(len1):
        pos0 = 0
        pos2 = len2-1
        pos1 = int(len2/2)
        while True:
            if (pos2-pos0)<=1:
                break
            # decrease if as much as possible in while!
            if list1[j] >= list2[pos1]: 
                pos0 = pos1 # include the target in pos0 - pos2
                pos1 = pos0 + int((pos2-pos0)/2)
            else:
                pos2 = pos1
                pos1 = pos0 + int((pos2-pos0)/2)
        if list1[j] == list2[pos1]:
            list3[j] = list2[pos1]
        else:
            if abs(list2[pos2]-list1[j]) < abs(list1[j]-list2[pos0]):
                list3[j] = list2[pos2]
            else:
                list3[j] = list2[pos0]
    sums[i] = sum(list3)

for sum in sums:
    print(sum)