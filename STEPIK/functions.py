n = int(input())

digit = 0

while n > 9:
    last_digit = n % 10
    digit += last_digit
    n = n // 10
    d = 0
    while digit != 0:
        l_digit = digit % 10
        d += l_digit
        digit = digit // 10


print(d)
