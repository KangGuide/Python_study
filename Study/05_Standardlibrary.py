import datetime

"""
datetime 값 생성
2020년 3월 14일을 파이썬으로 어떻게 표현할 수 있을까요? 이렇게 하면 됩니다.
오늘 날짜
작성방법: today = datetime.datetime.now()
"""
pi_day = datetime.datetime(2020, 3, 14)
print(pi_day)
print(type(pi_day))

pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)
print(type(pi_day))

today = datetime.datetime.now()
print(today)
print(type(today))

'''
timedelta 타입
두 datetime 값 사이의 기간을 알고 싶으면, 마치 숫자 뺄셈을 하듯이 그냥 빼면 됩니다.
'''
today = datetime.datetime.now()

pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)
print(type(today - pi_day))

today = datetime.datetime.now()

print(today)
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초

# 포매팅
print(today)
print(today.strftime("%A, %B %dth %Y"))
