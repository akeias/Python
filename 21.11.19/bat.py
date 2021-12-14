import table


### Bat 클래스 생성
class Bat:
    ####생성자
    def __init__(self, table, width, height, batImage, x_posn, y_posn, x_speed=10, y_speed=10):
        self.width=width     #배트의 가로 사이즈
        self.height=height  #배트의 세로 사이즈
        self.x_posn=x_posn#배트의 x좌표값
        self.y_posn=y_posn#배트의 y좌표값
        self.batImage=batImage

        self.x_start=x_posn
        self.y_start=y_posn
        self.x_speed=x_speed
        self.y_speed=y_speed


        self.table=table
        self.rectangle=self.table.draw_rectangle(self)
        #이것도 공과 마찬가지로 테이블에서 정의

    ###함수부
    #배트를 위로 움직이는 함수
    def move_up(self, master):
        self.y_posn-=self.y_speed #posn값에 speed 값을 뻄
        if (self.y_posn<=20): #bat가 위 회면에 닿으면 더이상 못올라가게 하는 코드
            self.y_posn=20
            
        x1=self.x_posn
        x2=self.x_posn+self.width
        y1=self.y_posn    #변경된 y_posn값을 y1에 반영
        y2=self.y_posn+self.height

        #변경된 값으로 아이템을 올김
        #Table 클래스의 move_item() 함수를 실행
        self.table.move_item2(self.rectangle, (x1+x2)/2,(y1+y2)/2)

    #배트를 아래로 움직이는 함수
    def move_down(self, master):
            self.y_posn+=self.y_speed 
            if (self.y_posn>=280): 
                self.y_posn=280
                
            x1=self.x_posn
            x2=self.x_posn+self.width
            y1=self.y_posn    
            y2=self.y_posn+self.height
            
            self.table.move_item2(self.rectangle, (x1+x2)/2,(y1+y2)/2)

    #공과 배트의 충돌 감지 및 처리 함수
    def detect_collision(self, ball):
        collision_direction=""  #충돌 방향 저장
        collision=False           #충돌이 감지되면 True로 바뀜
        feel=5                        #배트에서 공을 튕겨낸 다음 반사 각도와 반응 정도를 조정
  
        #배트 변수
        top=self.y_posn
        bottom=self.y_posn+self.height
        left=self.x_posn
        right=self.x_posn+self.width
        v_center=top+(self.height/2) #배트의 탑에서 배트 높이를 2로 나눈값을 더하면 세로 중간
        h_center=left+(self.width/2) #배트의 왼쪽에서 배트의 넓이를 2로 나눈값을 더하면 가로 중간

        #공 변수
        top_b=ball.y_posn
        bottom_b=ball.y_posn+ball.height
        left_b=ball.x_posn
        right_b=ball.x_posn+ball.width
        r=(right_b-left_b)/2 #반지름
        v_center_b=top_b+r #공의 탑에서 반지름을 더하면 세로 중간
        h_center_b=left_b+r #공의 왼쪽에서 반지름을 더하면 가로 중간

        #조건에 맞으면 충돌
        if((bottom_b>top) and (top_b<bottom) and (right_b>left) and (left_b<right)):
            collision=True #collision의 값변경

        #충돌했다면 어느방향으로 충돌햇는지 collion_direction에 저장
        if(collision):
            if((right_b>right) and (left_b<=right) and (top_b>top-r) and (bottom_b<bottom+r)):
                collision_direction="E"
                #abs()함수는 숫자의 부호를 제거하는 함수, 속도 값을 얻는데 사용
                #공이 배트의 어느 부분에 충돌했는지에 따라 공이 튀는 방향을 바꿈
                ball.x_speed=abs(ball.x_speed) #공이 양수값, 오른쪽으로 이동
        
                adjustment=(-(v_center-v_center_b))/(self.height/2)
                
                ball.y_speed=feel*adjustment
        
            elif((left_b<left) and (right_b>=left) and (top_b>top-r) and (bottom_b<bottom+r)):
                collision_direction="W"
                ball.x_speed=-abs(ball.x_speed)

                adjustment=(-(v_center-v_center_b))/(self.height/2)

                ball.y_speed=feel*adjustment
            
        

            return (collision, collision_direction)

    #배트 초기화 
    def start_position(self):
        self.x_posn=self.x_start
        self.y_posn=self.y_start
