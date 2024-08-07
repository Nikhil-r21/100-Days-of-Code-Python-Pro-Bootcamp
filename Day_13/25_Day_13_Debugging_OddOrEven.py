# Read this the code in main.py
# Spot the problems.
# Modify the code to fix the program.
# Fix the code so that it works and passes the tests when you submit.

# Hint
# Review the previous lesson and go through the 10 steps to tackle these debugging problems.




# SOLUTION 



number = int(input())

# if number % 2 = 0: (Before debug)
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
# Error line 4: if number % 2 = 0:
# Remember that single "=" is assignment.
# Double "==" is checking for equality.