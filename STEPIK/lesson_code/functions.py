a = int(input())
b = int(input())

t = 0

for i in range(a, b + 1):
    s = 0
    for j in range(1, b + 1):
        if i % j == 0:
            s += j
    if s >= t:
        t = s
        number = i

print(number, t)



