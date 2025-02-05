class Person:
    # 명사(속성)인 멤버변수
    name = "수린"
    age = 23
    weight = 40.5
    gender = 'female'

    # 초기화(생성자) 메서드(파이썬 기본으로 포함: 스페셜 메소드)
    def __init__(self, name, age, weight, gender):     # 위 name과는 다름
        self.name = name
        self.age = age
        self.weight = weight
        self.gender = gender

    # 동사(기상)인 멤버함수(메서드)
    def getup(self):    #myself
        print(f'{self.name}이(가) 일어납니다.')

    def setWeight(self, weight):    #!매개변수 2개인데 self 값 안 넣음 선언할 때만 쓰니까 weight 한개
        print(f'{self.name}의 몸무게가 변경됩니다.')
        print(f'현재 {self.weight}kg')
        self.weight = weight
        print(f'변경 후 {self.weight}kg')

    def getGender(self):
        return self.gender


man = Person('수우린', 23, 45.5, 'man')  #__init__() 특수함수를 실행.
#Person을 불러온 후에 .getup 객체 쓰는 것
man.getup()
man.setWeight(80.1) #!그래서 몸무게만 적기
print(f'{man.name}의 성별은 {man.getGender()}.') #{man.gender}, {man.getGender()} 결과는 동일
print('-------------------------------------------------')
print('객체정보')
print(man)