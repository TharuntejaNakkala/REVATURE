#Check if a given month and year has a Friday the 13th.
def has_friday_13(month, year):
    import datetime
    return datetime.date(year, month, 13).weekday() == 4

print(has_friday_13(9, 2025))
