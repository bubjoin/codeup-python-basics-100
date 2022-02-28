# n  0  1  2  3  4  5  6  7  8  9  10
# n0 1  0  1  1  2  3  5  8  13 21 34
# n1 0  1  1  2  3  5  8  13 21 34 55

total = int(input())

for t in range(total):
    n = int(input())
    n0 = [0] * (n+1)
    n1 = [0] * (n+1)
    
    if n==0:
        n0 = 1
        n1 = 0
        print(f'{n0} {n1}')
    elif n==1:
        n0 = 0
        n1 = 1
        print(f'{n0} {n1}')
    else:
        n0[0] = 1
        n0[1] = 0
        for num in range(2, n+1):
            n0[num] = n0[num-1] + n0[num-2]

        n1[0] = 0
        n1[1] = 1
        for num in range(2, n+1):
            n1[num] = n1[num-1] + n1[num-2]
        
        print(f'{n0[n]} {n1[n]}')
