def reverseNumber(n):
    if n == 0:
        return 0
    lastDigit = n%10
    n //= 10
    return int(str(lastDigit) + str(reverseNumber(n))) if n else lastDigit

for test in (0, 123000, 120):
    print(test, reverseNumber(test))