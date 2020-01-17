a = int(input())
b = int(input())
if a > b:
    n = b
else:
    n = a
for i in range(1, n + 1):
    if a % i == 0 and b % i == 0:
        x = i

    else:
        pass
l = a * b // x
print("lcm is", l, "the hcf is ", x)
