import sys


def fibo(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


print(sys.version_info)
print(list(fibo(20)))
print(sum(list(fibo(20))))
