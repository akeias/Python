import random, table

### Ball 클래스 생성
class Ball:
    ####생성자
    def __init__(self, table, width, height, color, x_speed, y_speed, x_posn, y_posn):
        self.width=width     #공의 가로 사이즈
        self.height=height  #공의 세로 사이즈
        self.x_posn=x_posn#공의 x좌표값
        self.y_posn=y_posn#공의 y좌표값
        self.color=color       #공의 색상

        self.x_start=x_posn
        self.y_start=y_posn
        self.x_speed=x_speed
        self.y_speed=y_speed

        self.table=table
        self.circle=self.table.draw_oval(self) #Ball자기자신을 draw_oval로 넘김
        # 테이블위에 공을 만들어야하기때문에 테이블에 draw_oval 함수를 정의

    ###함수부
        #공이 움직이는 부분
    def move_next(self):
        self.x_posn+=self.x_speed #현재 공 위치에 이동할 거리 x추가
        self.y_posn+=self.y_speed # 이건 y추가

        #공이 벽 위 아래 벽에 충돌 했을 때 처리
        #공이 벽에서 튕겨나오게 처리,y_speed의 부호변경
        
        #공의 위쪽 벽에 충돌
        if(self.y_posn<=20):
            self.y_posn=20
            self.y_speed=-self.y_speed

        #공의 아래쪽  벽에 충돌
        if(self.y_posn>=(self.table.height-self.height-20)):
            self.y_posn=(self.table.height-self.height-20)
            self.y_speed=-self.y_speed
    

        #공의 변경된 위치 지정 및 이동
        x1=self.x_posn
        x2=self.x_posn+self.width
        y1=self.y_posn  
        y2=self.y_posn+self.height

        self.table.move_item1(self.circle, x1, y1, x2 ,y2)


    #공의 초기 위치값지정
    def start_position(self):
        self.x_posn=self.x_start
        self.y_posn=self.y_start


    #전연변수 x_speed를 불러와 공의 속도에 대입, 랜덤값에의해 -,+로 값이 적
    def start_ball(self, x_speed, y_speed):
        self.x_speed=-x_speed if random.randint(0,1) else x_speed
        self.y_speed=-y_speed if random.randint(0,1) else y_speed
        self.start_position()

    #공을 멈추는 함수 
    def stop_ball(self):
        self.x_speed=0
        self.y_speed=0
