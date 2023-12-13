from random import randint

# 숫자 3개 뽑는 함수
def generate_numbers():
    numbers = []
    
    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)
        

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

# 숫자 예측 함수
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    i = 1
    
    while i <= 3:
        num = int(input(f'{i}번째 숫자를 입력하세요: '))
        if num > 9:
            print('범위를 벗어나는 숫자입니다. 다시입력하세요')
        elif num in new_guess:
            print('중복되는 숫자를 입력하셨습니다. 다시입력하세요')
        else:
            new_guess.append(num)
            i += 1
    
    return new_guess
    
# 점수계산 함수
def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0
    i = 0
    
    for i in range(3):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1
    
    '''
    # 내가한 생각 아직 약간 자바느낌으로 생각중
    while i < 3:
        if guesses[i] in solution:
            if guesses[i] == solution[i]:
                strike_count += 1
                i += 1
            else:
                ball_count += 1
                i += 1
        else:
            i += 1
    '''    
    return strike_count, ball_count


# 테스트 코드
ANSWER = generate_numbers()
tries = 1

while True:
    print(f'{tries}번째 도전중입니다.')
    guess = take_guess()
    strike, ball = get_score(guess, ANSWER)
    print(f'{strike}S {ball}B')
    if strike == 3:
        break
    tries += 1

print(f'축하합니다. {tries}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.')