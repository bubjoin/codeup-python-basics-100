import sys
input = sys.stdin.readline

zero = 0
one = 0
def fibo(num: int):
    if num==0:
        global zero 
        zero += 1
        return 0
    elif num==1:
        global one 
        one += 1
        return 1
    else:
        return fibo(num-1)+fibo(num-2)

t = int(input())

for i in range(t):
    n = int(input())
    fibo(n)
    print(zero, one)
    zero, one = 0, 0