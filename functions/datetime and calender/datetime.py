#using and trying the datetime module
import datetime
today=datetime.datetime.now()
day=datetime.date.today()

print("todays date and time is :",today)
print("todays date is:",day)
month=day.month
print(month)
year=datetime.date.today().year
print(year)