x = input()
x = int(x, 16)
for i in range(1, 16):
    print(f'{x:X}*{i:X}={x*i:X}')
    
