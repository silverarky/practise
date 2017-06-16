#-*-coding:utf-8-*-
import datetime as dt
import re
def to_timestamp(time,utc):
    utc=re.match(r'^\w+(\+|\-)(\d{1,2})\:\d+$',utc).group(2)
    time=dt.datetime.strptime(time,'%Y-%m-%d %H:%M:%S')
    
    #方法1：astimezone
    time=time.replace(tzinfo=dt.timezone.utc)
    time=time.astimezone(dt.timezone(dt.timedelta(hours=int(utc))))
    #方法2：设置timezone，直接replace
    utc_5=dt.timezone(dt.timedelta(hours=int(utc)))
    time=time.replace(tzinfo=utc_5)
    
    time=time.timestamp()
    print(time)
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')


