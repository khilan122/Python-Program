
def recursive_factorial(n):
  if n == 1:
     return n
  else:
     return n*recursive_factorial(n-1)     #function calling itself

#taking input from the user
number = int(input("User Input : "))
print("The factorial of", number, "is", recursive_factorial(number))

