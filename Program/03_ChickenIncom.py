day = []
income = []

with open('Data/chicken.txt', 'rt', encoding='UTF8') as f:
    for line in f:
        # 파일을 쪼개서 리스트에 저장
        NameSplit = line.split(": ")
        day.append(NameSplit[0])
        income.append(int(NameSplit[1]))

# 총합구하기
i = 0
total = 0
while i < len(day):
    total = income[i] + total
    i += 1

# 월별로 총합나누기
print(total / len(day))

# 이게 원본계산식
with open('Data/chicken.txt', 'r') as f:
    total_revenue = 0
    total_days = 0
    
    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1])  # 그날의 매출

        total_revenue += revenue
        total_days += 1

    print(total_revenue / total_days)
