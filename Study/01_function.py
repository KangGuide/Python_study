
# 파이썬 함수 기본 모형
"""
 변수 = 파라미터
 dev 함수이름(파라미터):
    함수내용

    또는

    return 리턴값 = 파라미터
"""

# 연산관련
'''
 연산 과정에서 +, -, *, %(나머지)이 4가지는 정수형 정수형 연산을 제외한 소수형이 하나이상 포함되면 결과값에서 소수형이 나온다.
 / 나누기 연산에서는 무슨 연산을 하던 소수형이 나타난다.
 ** 거듭제곱 // 버림나눗셈
 
 round 함수는 반올림 함수 (값, 소수점아래값갯수)
 '''

# floor division (버림 나눗셈) 일반 나눗셈은 소수형이 나타나지만 버림 나눗셈은 소수형이 아닌 정수형으로 리턴해준다
print(8.0 // 3)

# round (반올림)

print(round(3.1415926535))

# 문자열 연산

print("I'm \"excited\" to learn Pyhton!")
print("3" + "5")

# 형 변환 (Type Conversion) : 값을 한 자료형에서 다른 자료형으로 바꾸는 것
# java에서 cast변환 하듯이 작성하지만 괄호가 변수의값에 들어가야한다

age = 7
# print("제 나이는 " + age + "살입니다.") 자바에서는 되는거지만 파이썬에서는 오류가 난다 문자열 + 정수열 합이기 때문에
print("제 나이는 " + str(age) + "살입니다.")

# format을 이용한 문자열 포매팅
year = 2019
month = 10
day = 29

dateString = "오늘은 {}년 {}월 {}일 입니다"
print(dateString.format(year, month, day))
print("오늘은 {1}년 {2}월 {0}일 입니다".format(year, month, day))
# 최신 방식 f-string
print(f"오늘은 {year}년 {month}월 {day}일 입니다")

#Type 함수
print(type(3))
print(type(3.0))
print(type("3"))
print()

# 파라미터에 기본값 설정
def myself(name, age, nationality="한국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1, "미국")  # 옵셔널 파라미터를 제공하는 경우
print()
myself("코드잇", 1)  # 옵셔널 파라미터를 제공하지 않는 경우 이것은 항상 마지막에 있어야한다

# 상수 (constant)
PI = 3.14 # 상수를 적을때는 대문자로 적어야함
