import datetime
import pytz

# td = datetime.date.today()
#
# tdelta = datetime.timedelta(days=7)
#
# # print(td + tdelta)
#
# bday = datetime.date(2023, 5, 31)
#
# till_bday = bday - td
# print(till_bday.total_seconds())

# t = datetime.datetime.today()
#
# tdelta = datetime.timedelta(hours=7)
#
# print(t + tdelta)
#
# dt_today = datetime.datetime.today()
# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)
#
# # for tz in pytz.all_timezones:
# #     print(tz)
#
# dt_my = dt_utcnow.astimezone(pytz.timezone('Europe/Moscow'))
# print(dt_my)
#
# dt_mtn = datetime.datetime.now()
# dt_msc = dt_mtn.astimezone(pytz.timezone('Europe/Moscow'))
# dt_utcnow = datetime.datetime.utcnow()
#
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# dt = datetime.datetime(2016, 7, 27, 12, 30 , 45, tzinfo=pytz.UTC)
# print(dt)

dt_mtn = datetime.datetime.now(tz=pytz.timezone('Europe/Moscow'))

print(dt_mtn.isoformat())
print(dt_mtn.strftime('%B %d %Y'))

dt_str = 'July 21 2023'

dt = datetime.datetime.strptime(dt_str, '%B %d %Y')
print(dt)
