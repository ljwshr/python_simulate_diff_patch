import datetime
from builtins import str
temp_my_time = datetime.datetime.now()
result_date=""
#print ("%s%s%s%s%s%s" % (i.year, i.month, i.day, i.hour,i.minute,i.second) )
result_date+= str(temp_my_time.year)
result_date+=str(temp_my_time.month)
result_date+=str(temp_my_time.day)
result_date+=str(temp_my_time.hour)
result_date+=str(temp_my_time.minute)
result_date+=str(temp_my_time.second)
print(result_date)
