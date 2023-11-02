import datetime

# 현재 날짜와 시간을 가져옴
current_datetime = datetime.datetime.now()

# 9시간을 더함
new_datetime = current_datetime + datetime.timedelta(hours=9)

# "YYYY-MM-DD" 형식으로 출력
formatted_date = new_datetime.strftime("%Y-%m-%d")
print(formatted_date)
