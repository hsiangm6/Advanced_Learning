"""熟悉datetime操作的實作"""
import datetime
'''d1=datetime.datetime(2005,5,23)
print(d1)

#日期時間的詳細資料列點或分開顯示
d2=datetime.datetime(2021,7,6,13,5,24)
print("日期:",d2.date())
print("時間:",d2.time())
print("年:",d2.year,end=',  ')
print("月:",d2.month,end=',  ')
print("日:",d2.day,end=',  ')
print("Hour:",d2.hour)
print("星期",d2.date().weekday()+1)
print("今天日期:",datetime.date.today())

#兩個日期時間的相差天數和秒數
d3=datetime.datetime(2021,7,6,13,16,53)
d4=datetime.datetime(2050,7,1,13,16,23)
diff=d4-d3
print("相差幾天幾秒:",diff)
#print(diff.years)   #此列無法執行
print("相差幾天:",diff.days)
print("相差幾秒:",diff.seconds)

#增加天數和秒數給輸入的日期時間
diff2=datetime.timedelta(days=3,seconds=4)
d5=datetime.datetime.now()
d6=d5+diff2
print(d6)

#datetime to string
d7=datetime.datetime.now()
print('現在日期時間:'+str(d7))
print('datetime to string:',d7.strftime('%Y-%m-%d'))
print('datetime to string:',d7.strftime('%B-%d, %Y'))   #如果Y不是大寫而是小寫的話，顯示的只有2021後面的'21'
print('datetime to string:',d7.strftime('%Y-%m-%d %H:%M:%S'))
print('datetime to string:',d7.strftime('%Y-%m-%d %I:%M:%S %p, %A'))

#string to datetime
dstr='2021-07-06 14:41:56'
d8=datetime.datetime.strptime(dstr,'%Y-%m-%d %H:%M:%S')
print("string to datetime:",d8)

#算今天是今年的第幾天
d_str=str(input('輸入形式(20210707):'))
another_d_str=d_str[:4]+'0101'                 #今年的第一天
d=datetime.datetime.strptime(d_str,"%Y%m%d")
another_d=datetime.datetime.strptime(another_d_str,'%Y%m%d')
print(int((d-another_d).days)+1)

#調整時差
loc_dt=datetime.datetime.today()
time_del=datetime.timedelta(hours=3)
new_dt=loc_dt+time_del
loc_dt_format=loc_dt.strftime('%Y/%m/%d %H:%M:%S')
new_dt_format=new_dt.strftime('%Y/%m/%d %H:%M:%S')
print(loc_dt_format)
print(new_dt_format)
'''
#練習題1:利用Python計算由2010年3月2日中午12點15分0秒起算，經過145天10小時又3分鐘之後的時間為何? 你的回答應該使用這個格式: YYYY-MM-DD HH:MM:SS，也就是年月日時分秒。
loc_dt=datetime.datetime(2010,3,2,12,15,0)
time_del=datetime.timedelta(days=145,hours=10,minutes=3)
new_dt=loc_dt+time_del
print(loc_dt)
new_dt_format=new_dt.strftime('%Y-%m-%d %H:%M:%S')
print(new_dt_format)



