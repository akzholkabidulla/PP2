#example1
import datetime 
x =  datetime.datetime.now()
print(x)

#example2
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
#Return the year and name of weekday

#example3
import datetime
x = datetime.datetime(2005,11,8)
print(x)

#example4
import datetime
x = datetime.datetime(2018,6,1)
print(x.strftime("%B")) #"%B" - print the month -> "June"