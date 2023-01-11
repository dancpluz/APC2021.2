from datetime import date
from datetime import timedelta

t = int(input())
data1 = date.today()
data2= data1 - timedelta(days = t)
print(data2)
