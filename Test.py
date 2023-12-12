with open('Data/vocabulary.txt', 'rt', encoding='UTF8') as f:
    English = []
    Korea = []
    
    for line in f:
        data = line.strip().split(": ")
        Korea = data[1]
        English = data[0]
    
print(Korea)
print(English)
while True:
    
    if result == 'q':
        break
    else:
        if result == English:
            print("맞았습니다!\n")
        else:
            print(f". 정답은 {English}입니다.\n")
