try:
  a = float(input("enter first number:"))
  b = float(input("Enter second number:"))
   print(f"Addition:{a+b}")
print(f"Subtraction:{a-b}")
except ValueError:
print("Please enter valid number")
