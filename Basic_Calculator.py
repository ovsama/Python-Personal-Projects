#This python program builds a simple calculator that allows performing Basic Arithmetic Operations

def prog():
  n1 = float(input("Enter first number: "))  #catch the 1st number
  n2 = float(input("Enter second number: "))  #catch the 2nd number
  op = input("Enter operator: ")               #catch the operator
  if op == "+":
    x = n1 + n2        #perform addition
  elif op == "-": 
    x = n1 - n2        #perform substraction
  elif op == "*":
    x = n1 * n2        #perform multiplication
  elif op == "/":
    x = n1 / n2        #perform division
  else:
    x = "Error : Invalid Operator"   # otherwise, throw an error.
  return print(x)

#Call the function
prog()
