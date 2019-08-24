n = int(input())
a, b = 0, 1
for i in range(n):
    print(a)
    c = a
    a = b
    b = b + c
