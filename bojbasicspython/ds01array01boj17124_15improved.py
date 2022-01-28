# https://www.acmicpc.net/problem/17124
from sys import stdin

t = int(stdin.readline())
sums = [0] * t
for i in range(t):
    len1, len2 = map(int,stdin.readline().split())
    list1 = tuple(map(int,stdin.readline().split()))
    list2 = list(map(int,stdin.readline().split()))
    list2.sort()
    sum = 0 # You only need to get the sum, not whole list here
    for j in range(len1):
        pos0 = 0
        pos2 = len2-1
        pos1 = len2//2 # Do not call int() for int
        num = list1[j] # Don't repeat calling list indexing in while
        while True:
            if (pos2-pos0)<=1:
                break
            # decrease if as much as possible in while!
            if num >= list2[pos1]: 
                pos0 = pos1 # include the target in pos0 - pos2
                pos1 = pos0 + ((pos2-pos0)//2)
            else:
                pos2 = pos1
                pos1 = pos0 + ((pos2-pos0)//2)
        if abs(list2[pos2]-num) < abs(num-list2[pos0]):
            sum += list2[pos2]
        else: # remove redundancy
            sum += list2[pos0]
    sums[i] = sum

for sum in sums:
    print(sum)