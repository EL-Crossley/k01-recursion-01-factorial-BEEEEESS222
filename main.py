# Put your function here
def factor(n):
  if n>1:
    return n*factor(n-1)
  if n==1:
    return 1

# testing
num = int(input())
print(factorial(num))
