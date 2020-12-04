from datetime import date, timedelta
dt = date(2020, 12, 2)
print(dt)
delta_1 = timedelta(days=1)
delta_2 = timedelta(days=30)
#print(delta_1)
one_day = dt - delta_1
print(one_day)
one_month = dt - delta_2
print(one_month)