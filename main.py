# Put your function here
def factorial(n):
  if n>1:
    return n*factorial(n-1)
  if n==1:
    return 1

# testing
num = int(input())
print(factorial(num))
