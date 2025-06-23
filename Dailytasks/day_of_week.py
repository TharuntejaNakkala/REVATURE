#Given a date in dd mm yyyy format, print the day of the week.
from datetime import datetime

d = "08 05 2015"
dt = datetime.strptime(d, "%d %m %Y")
print(dt.strftime("%A"))
