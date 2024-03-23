#Conditional Statements 1 task 1
#Buggy Code  

#You are provided with a Python script that used conditional statements to tell if a 
#number is positive, negative, or zero, but it has some errors. Identify and fox them.

number = int(input("Enter a number: ")) # Had to convert number to int to cover negative numbers

if number > 0:
  print("The number is positive.")
elif number == 0:    # Needed another == to make code work.
  print("The number is zero.")  
else:
  print("The number is negative.")
  
# The Code works now.
