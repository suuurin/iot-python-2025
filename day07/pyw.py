# 1. 원의 넓이

# r = float(input("반지름 입력: "))
# pi = 3.1415
# area = pi * (r**2)
# print(f'반지름이 {r}인 원의 넓이는 {area:.4f}이다.')

# 문자열 변환

# name = input('이름을 입력하세요: ')
# age = int(input('나이를 입력하세요: '))
# print(f'이름은 {name}, 나이는 {age}')

# 짝/홀 판별(조건문)

# num = int(input('숫자를 입력하세요: '))

# if num%2 == 0:
#     print(f'{num}은 짝수입니다.')
# else:
#     print('홀수입니다.')

# 1부터 N까지 합(반복문)

n = int(input("N을 입력하세요: "))
total = 0

for i in range(1, n+1):
    total += i
print(f'{total}')

# # 시간복잡도 O(1) 합
# n = int(input('N을 입력하세요: '))
# total = n * (n+1) // 2  
# print(f'1부터 {n}까지의 합은 {total}입니다.')