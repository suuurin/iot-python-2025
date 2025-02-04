# 복합자료형
# 자료구조 및 알고리즘

# 리스트 이전
a = 1
b = 2
c = 3
d = 4
e = 5

sum = a + b + c + d + e
print(sum)

# 리스트 () - 다른 언어에선 리스트와 배열은 다른것
f = [1, 2, 3, 4, 5]
print(f)
print(type(f))

f = ['Life', 'is', True, 0, None, [1,2,3]]
print(f)
print(f[0])

f[3] = 100  # 리스트의 한 요소에도 값을 집어넣을 수 있음
print(f)

## 튜플 ()
# 리스트와 거의 흡사. 값을 변경할 수 없음
t = (1,2,3,4)
print(t)
print(t[3])
# t[0] = 5 # 주석 Ctrl + / 사용
print(type(t))

## 딕셔너리(사전형) {} {key : value}의 집합, dict
spiderman = { 'name': 'Peter Parker', 'age': 20, 'weapon': 'Web Shooter'}
print(spiderman)
print(type(spiderman))

print(spiderman['name']) #리스트, 튜플은 숫자로 딕셔너리는 key로

spiderman['age'] = 21
print(spiderman)


## 집합 set (), {}, [] 모두 사용, 리스트처럼 인덱스가 없음
s = set([1, 2, 3, 5, 7, 9, 5])  # 집합: 중복 제거(5)
print(s)
print(type(s))

s = set('Hello World')
print(s)

## 변수명 지정 방식
## 의미있는 단어들의 조합으로 만들것
phoneNumber = '010-6688-7733'
salaryBankAccount = '866-12-335566'

samsung = ''
samsung1 = ""
# 1samsung = ''         # 숫자로 변수명 시작불가
# samsung! = ''         # _ 이외의 특수문자 모두 사용불가
# samsung-apple = ''    # 파이썬 연산자는 사용불가
_samsung = ''
samsung_ = ''