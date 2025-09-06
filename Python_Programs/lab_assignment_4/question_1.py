# -------------------- Experiment 1:  4 Lab-Python-Core-6-AUG-2025 --------------------

# Q1) Python program to check leap year.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(year, "is a leap year.")
else:
  print(year, "is not a leap year.")


'''
OutPut:- 
Enter a year: 2004
2004 is a leap year.

Enter a year: 2003
2003 is not a leap year.
'''
