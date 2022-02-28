import sys
input = sys.stdin.readline

answer = [0,0]
def fibo(num: int):
    if num==0:
        answer[0] += 1
        return 0
    elif num==1:
        answer[1] += 1
        return 1
    else:
        return fibo(num-1)+fibo(num-2)

answers = []

t = int(input())

for i in range(t):
    n = int(input())
    fibo(n)
    answers.append(answer[:])
    answer[0], answer[1] = 0, 0

for ans in answers:
    print(ans[0], ans[1])