# Identify the Greatest 2 task 1
# Write a Python program that prompts the user to enter threemnumber.  The program should
# then identify and print out the largest among the three.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3 :
  print(f"{num1} is the largest.")
elif num2 >= num1 and num2 >= num3 :
  print(f"{num2} is the largest.")
else:
  print(f"{num3} is the largest.")
  
# Identify the Smallest 2 task 2
# Extend your program from Task 1 to also determine the smallest number among the three
# and print it out.

if num1 <= num2 and num1 <= num3 :
  print(f"{num1} is the smallest.")
elif num1 <= num2 and num2 <= num1 and num2 <= num3 :
  print(f"{num2} is the smallest.")
else: 
  print(f"{num3} is the smallest.")

  
 # Equality Check 2 Task 3
 # Enhance your program to handle cases where two or all of the numbers are equal. The # # program should display appropriate messages like "Two number are equal and the largest"
 # or "All numbers are equal."
 
if num1 == num2  == num3:
  print("All numbers are equal.")
elif num1 == num2 or num2 == num3 or num1 == num3 :
  print("Two numbers are the same, one is not!")
else:
  print("All different numbers here!")

# extra credit task 4
# printing out which numbers are the same.

if num1 == num2 :
  print("The first two numbers are the same!")
elif num2 == num3 :
  print("The second and third number are the same!")
else:
  print("The first and the third numbers are the same!")