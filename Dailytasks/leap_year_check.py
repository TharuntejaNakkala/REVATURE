"""Check whether the given year is a leap year."""
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('leap year')
else:
    print('not leap year')
# Output: leap year or not leap year based on the input year
# Example:  If the input is 2020, the output will be "leap year".