from datetime import datetime
from datetime import timedelta
import datetime
import calendar
import numpy as np

last_day_of_month = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_year_last_day_of_month = [31,29,31,30,31,30,31,31,30,31,30,31]

def get_week_of_month(year, month, day):
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x==day)[0][0] + 1
    first_day_of_month = datetime.date(year,month,1).weekday()
    flag = 0
    if first_day_of_month > 3:
        flag = 1
    week_of_month -= flag
    if week_of_month == 0:
        day_of_week = datetime.date(year,month,day).weekday()
        if day_of_week > 3: # 목요일
            if month == 1:
                year -= 1
                month = 12
            else:
                month -= 1
            if year %4 == 0:
                day = leap_year_last_day_of_month[month - 1]
            else:
                day = last_day_of_month[month - 1]

            x = np.array(calendar.monthcalendar(year, month))
            week_of_month = np.where(x==day)[0][0] + 1
            if datetime.date(year,month,1).weekday() > 3:
                week_of_month -= 1
        else:
            week_of_month = 1
    elif week_of_month == 5:

        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        day = 1
        day_of_week = datetime.date(year,month,day).weekday()

        if day_of_week <= 3: # 목요일
            week_of_month = 1
    return(week_of_month)

def worker():
    date = datetime.date(2022, 1, 1)
    while date != datetime.date(2023,1,1):
        year = date.year
        month = date.month
        day = date.day
        week = get_week_of_month(year,month,day)
        print(date)
        print(week)
        date = date + timedelta(days=1)


worker()