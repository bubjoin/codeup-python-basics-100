n = int(input())
yes = False
for i in range(1, n+1):
    si = str(i)
    for m in si:
        if (m=='3') or (m=='6') or (m=='9'):
            yes = True
    if yes == True:
        print('X', end=' ')
        yes = False
    else:
        print(i, end=' ')
