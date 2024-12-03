#import the calender module
import calendar 
import datetime

#user input for month and year
#year=int(input("enter the year: "))
#month=int(input("Enter the month: "))
year=datetime.datetime.now().year
month=datetime.datetime.now().month

#display month of a year
print(calendar.month(year,month))

#print(calendar.calendar(year))
