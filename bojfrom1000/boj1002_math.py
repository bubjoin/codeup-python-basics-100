# two circles meet
import sys
import math
input = sys.stdin.readline

ans_list = []
t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    d = math.sqrt((x2-x1)**2 + ((y2-y1)**2))
    # using **(0.5) is possible instead of math.sqrt()
    if (d==0) and (r1==r2):
        ans_list.append(-1) 
    elif (d==(r1+r2)) or (d==abs(r2-r1)):
        ans_list.append(1)
    elif (r1+r2) > d > abs(r2-r1):
        ans_list.append(2)
    else:
        ans_list.append(0) 

for ans in ans_list:
    print(ans)