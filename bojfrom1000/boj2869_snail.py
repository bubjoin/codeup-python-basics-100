# A snail watns to go up
# Trying a different soulution

import sys
input=sys.stdin.readline

a, b, v = map(int, input().split())

y = (v-a)/(a-b) +1
if y % 1 == 0:
    y = int(y)
    print(y)
else:
    y = int(y) + 1
    print(y)