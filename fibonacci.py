# Python program to calculate the Fibonacci number
# 0,1,2,3,5,8,13,21,34,55,...
# date : Jan 30, 2020

# fibo function definition
import unittest


def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))


# Calculate Fibonacci number
result = fibo(10)
print('fibo(10)='+str(result))
