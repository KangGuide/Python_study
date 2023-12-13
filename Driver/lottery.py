import random

# 로또 번호 뽑기 함수
def generate_numbers(n):
    random_number = []
    while len(random_number) < n:
        num = random.randint(1, 45)
        
        # 로또 중복숫자 제거
        if num not in random_number:
            random_number.append(num)
            
    return random_number

# 로또 실제 번호 뽑기 함수
def draw_winning_numbers():
    
    # 해답
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]
    
    '''
    내 생각
    real_num = generate_numbers(6)
    real_num.sort()
    real_num = real_num + generate_numbers(1)
    
    return real_num
    '''

# 로또 번호 매치 함수
def count_matching_numbers(numbers, winning_numbers):
    match_num = 0
    
    for i in numbers:
        if i in winning_numbers:
            match_num += 1
            
    return match_num

# 로또 당첨금 확인
def check(numbers, winning_numbers):
    match_num = 0
    bonus = 0
    
    for i in numbers:
        if i in winning_numbers[6:]:
            bonus += 1
            continue
        
        if i in winning_numbers:
            match_num += 1
    
    
    # 이런 조건의 경우 큰값 즉 1등부터 내려오게끔 해야한다
    if match_num == 6:
        return 1000000000
    elif bonus == 1 and match_num == 5:
        return 50000000
    elif match_num == 5:
        return 1000000
    elif match_num == 4:
        return 50000
    elif match_num == 3:
        return 5000
    else:
        return 0


print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))