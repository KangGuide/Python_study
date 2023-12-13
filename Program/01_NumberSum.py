# 자리수 합 리턴
def sum_digit(num):
    if len(str(num)) > 1:
        if len(str(num)) <= 2:
            number = str(num)[0]
            number1 = str(num)[1]
            x = int(number) + int(number1)
            return x

        elif len(str(num)) <= 3:
            number = str(num)[0]
            number1 = str(num)[1]
            number2 = str(num)[2]
            x = int(number) + int(number1) + int(number2)
            return x

        elif len(str(num)) <= 4:
            x= 1
            return x
    else:
        x = num
        return x
# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
y = 0
i = 1
while i <= 1000:
    y = sum_digit(i) + y
    i += 1

print(y)


'''
# 자리수 합 리턴
def sum_digit(num):
    total = 0
    str_num = str(num)
    
    for digit in str_num:
        total += int(digit)

    return total


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
digit_total = 0
for i in range(1, 1001):
    digit_total += sum_digit(i)

print(digit_total)

'''