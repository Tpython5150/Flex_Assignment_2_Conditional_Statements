# Leap Year Explorer
# Leap Year Checker 3 Task 1
# Write a Python program that prompts the user to input a year.  The program should 
# determine if the give year or ont and then display an appopriate message.  Please
# that this is the defintion of a leap year: Every year that is exactly divisble by four 
# is a leap year, except for years that are exactly divislbe by 100, but these centurial # years are leap years if they are divisible by 400. 

test_year = int(input("Enter a year :"))

if (test_year % 4 == 0 and test_year % 100 != 0 ) or (test_year % 400 == 0 ) :
  print(f"This {test_year} is a leap year!")
else: 
  print(f"This {test_year} is not a leap year!")



