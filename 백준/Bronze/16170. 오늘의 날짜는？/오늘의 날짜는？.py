#백준 16170: 오늘 날짜는?

import datetime
now = datetime.datetime.now() - datetime.timedelta(hours=9)

print(now.year)
print(now.month)
print(now.day)