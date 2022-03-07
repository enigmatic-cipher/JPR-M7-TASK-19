"""
Fibonacci series is a series of numbers where the next term is the sum of the previous 2 terms. The first two terms in the series are 0 and 1. Given a number as input, calculate the value of nth term in the Fibonacci series. Use recursion.
"""

def recur(n):
  if (n==0):
    return 0
  
  elif (n==1):
    return 1
    
  else:
    return (recur(n-1) + recur(n-2))

n = 9
print(recur(n))
                             