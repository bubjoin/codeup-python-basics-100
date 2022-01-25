h, b, c, s = input().split()
h, b, c, s = int(h), int(b), int(c), int(s)
bitsum = h * b * c * s
mb = bitsum / 8 / 1024 / 1024
print(f"{mb:.1f} MB")

