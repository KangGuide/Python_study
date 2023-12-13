# 리스트 (list) 자바에서 배열과 비슷하다
numbers = [2, 3, 5, 7, 11, 13]
names = ["윤수", "혜린", "태호", "영훈"]

# 인덱싱 (indexing) 이건 자바와 같다
print(numbers[1] + numbers[3])

'''
len() : 리스트 길이찾는 함수
리스트변수명.append(변수) : 리스트에 변수를 넣는 함수 자바에서 list.add 와 같다 (추가함수)
리스트변수명.insert(넣고싶은위치, 변수) : 넣고싶은 위치에 변수를 넣고싶을 때 사용 (삽입함수)
del 리스트변수명[인덱싱] : 인덱싱 번호에 들어있는 변수를 삭제

sorted 함수는 기존의 리스트를 건드리지 않고 새로운 리스트를 만들어서 정렬한다
sorted(변수명)                 오름차순 정렬
sorted(변수명, reverse=true)   내림차순 정렬

sort는 기존의 리스트를 정렬시킨다
변수명.sort()
print(변수명) 이렇게 작성해야 오름차순 정렬로 출력됨
내림차순 정렬은 마찬가지로 괄호안에 reverse=true 를 적으면 된다
'''
'''
# 피보나치 해설
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    previous, current = current, current + previous
    i += 1
'''
# 사전 (dictionary)
# key-value pair (키-값 쌍)

my_dictionary = {
    5: 25
  , 2: 4
  , 3: 9
}
print(my_dictionary[3])

# 사전변수명.items 키와 밸류값을 동시에 받을 수 있고 .key / .value 로 원하는 값만 가져올 수 있다
