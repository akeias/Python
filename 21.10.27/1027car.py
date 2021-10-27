#클래스 정의 부분
class  Car :
    #필드 부분
    color="" #필드에서 color 선언및 초기값 대입
    speed=0 #필드에서 speed 선언및 초기값 대입
    name="" #인스턴스 변수
    count=0  #클래스 변수

    #메소드 부분
    def upSpeed(self,value): #upSpeed의 메소드 정의부분
        self.speed+=value

    def downSpeed(self,value): #downSpeed의 메소드 정의부분
        self.speed-=value

    def getName(self):
        return self.name
        
    #생성자 추가 / 인스턴스를 생성하면 무조건 호출되는 메소드(무조건 실행된다는 뜻)
    def __init__(self,color,speed,name): #매게변수를 입력받아 생성자 실행
        Car.count += 1 
        self.color=color#(빨강)        #self는 무조건 있어야하고
        self.speed=speed#0           #self만 있으면 매게변수가 없는 실행자
        self.name=name#ㄴ이 주석은 self만 있을때 color와 speed값을 지정해준것.
        
   

#변수 선언 부분

Car1,Car2=None,None,
#메인 코드 부분

Car1=Car("빨강",10,"쉐보레")        
"""
Car1.color="빨강"    
Car1.speed=0      
"""

Car2=Car("빨강",0,"아우디")  


myCar3=Car("노랑",10,"레이") # myCar3의 인스턴스 생성
"""
myCar3.color="노랑"  #myCar3의 color필드의 필드값 대입
myCar3.speed=0      #myCar3의 speed필드의 필드값 대입
"""

Car1.upSpeed(30)   
print("%s의 색상은 %s이며, 현재 속도는 %dkm, 생산된 자동차 숫자는 총 %d대입니다."%(Car1.getName(),Car1.color,Car1.speed,Car.count))

Car2.upSpeed(60)
print("%s의 색상은 %s이며, 현재 속도는 %dkm, 생산된 자동차 숫자는 총 %d대입니다."%(Car2.getName(),Car2.color,Car2.speed,Car.count))    

myCar3.upSpeed(0)#myCar3 메소드 실행 부분
print("%s의 색상은 %s이며, 현재 속도는 %dkm입니다."%(myCar3.getName(),myCar3.color,myCar3.speed))  
