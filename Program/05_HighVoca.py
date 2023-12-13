import random

with open('Data/vocabulary.txt', 'rt', encoding='UTF8') as f:
    English = []
    Korean = []
    
    for line in f:
        data = line.strip().split(": ")
        English.append(data[0])
        Korean.append(data[1])


while True:
# random.choice 리스트 안에 있는 숫자 랜덤하게 가져오는 함수
    Quiz = random.choice(Korean)
    
    i = 0
    while i <= len(Korean) :
        if Quiz == Korean[i]:
            break
        else:
            i += 1
        
    result = input(f'{Quiz}: ')
    
    if result == 'q':
        break
    
    if result == English[i]:
        print('맞았습니다!')
    else:
        print(f'틀렸습니다. 정답은 {English[i]}입니다.')