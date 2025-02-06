# 객체지향 다시

#=========================================================================================================
class Car:
    ## __new__ 사용빈도X, __init__ 많이 사용
    ## Car() 호출하면 아래 메서드가 실행
    ## 모를 때는 None
    def __init__(self, company=None, name=None, plateNumber=None):
        self.__company = company    # 멤버 변수 이름 앞에 __ 쓰면 외부접근 불가
        self.__name = name
        self.__plateNumber = plateNumber
        print('Car 클래스를 새로 생성!')

    # # 클래스 자체가 출력되는데, __str__문자열로 출력되도록 바꿔줌
    # def __str__(self):
    #     return f'제 차는 {self.__company} {self.__name}이고, 차 번호는 {self.__plateNumber}입니다.'
    
    # 외부에서 잘못된 차번호(str이 아닌)를 넣으면 안 들어감
    def setPlateNumber(self, newPlateNumber):
        if type(newPlateNumber) is str:
            self.__plateNumber = newPlateNumber

    def setName(self, newName='글쎄요'):    #이름을 모를 때 글쎼요로 대체.
        self.__name = newName
    
    def getName(self):
        return self.__name
#=========================================================================================================


# 모듈 쓰려면 예제는 주석 처리

# myCar = Car('현대차', '투싼', '54라9537')
# # 파라미터명 = 값으로 매개변수 순서를 변경 가능
# # 객체 생성하면서 직접 값 넘기기
# myCar = Car(name='투싼', plateNumber='54라9537', company='현대차')
# print(myCar) #차의 번호를 출력하고 싶음

# myCar.__plateNumber = 2018 #클래스 외부에서 잘못된 데이터를 넣어도 문제 발생 X
# print(myCar)

# myCar.setPlateNumber('2025')    #setter 메서드로 번호(str) 수정
# print(myCar)

# # Car 객체 기본값
# yourCar = Car()
# print(yourCar)

# # 번호 변경
# yourCar.setPlateNumber('285구8899')
# print(yourCar)

# # 이름 변경
# yourCar.setName('제네시스')
# print(yourCar)