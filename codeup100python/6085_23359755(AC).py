w, h, b = input().split()
w, h, b = int(w), int(h), int(b)
print(f"{w*h*b/8/1024/1024:.2f} MB")
