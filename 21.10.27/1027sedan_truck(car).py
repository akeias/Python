#클래스 선언
class Car: #상위  클래스
    speed = 0

    def upSpeed(self, value):
        self.speed+=value

        print("현재 속도(슈퍼클래스):%d"%self.speed)
        
class Sedan(Car): #상위클래스 Car를 상속받은 하위클래스
    seatNum=0
    
    def getSeatNum(self):
        return self.seatNum
    
    def upSpeed(self,value):
        self.speed+=value

        if self.speed>150: #메소드 오버라이딩 : 상위  클래스의 메소드를 하위 클래에서 재정의 하는것
            self.speed=150 #여기서는 속도올리()메소드를 받앗지 속도제한이 필요해서 재정의해서 사용

            print("현재 속도(서브 클래스):%d"%self.speed)

class Truck(Car): #상위클래스 Car를 상속받은 하위클래스
    pass

    def getCapacity(self):
        return self.capacity

#변수 선언

sedan1, truck1 = None, None

#메인 코드 부분

sedan1=Sedan()
truck1=Truck()

sedan1.seatNum=5
truck1.capacity=50

print("승용차의 좌석수는 %d개입니다."%sedan1.getSeatNum())
print("트럭의총중량은 %d톤입니다."%truck1.getCapacity())

print("승용차 --> ", end="")
sedan1.upSpeed(200)

print("트럭--> ", end="")
truck1.upSpeed(200)
