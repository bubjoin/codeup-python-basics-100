a, m, d, n = input().split()
a, m, d, n = int(a), int(m), int(d), int(n)

hang = a
for i in range(n-1):
    hang = hang * m + d 
    
print(hang)
