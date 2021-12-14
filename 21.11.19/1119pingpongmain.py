from tkinter import *
from table import * # 프롬 모듈 임폴트 * 는 모듈명을 안적어줘도됨
from ball import *
from bat import *
# import table,ball,bat는 모듈명을 일일히 적어줘야함

####전역변수초기화
x_speed=10 #공의 x속도
y_speed=0#공의 y속도

first_serve = True


#메인부
window=Tk()
window.title("MyPingPong")
window.resizable(width=FALSE, height=FALSE)

    
###game_flow()함수부
def game_flow():

    global score_left, score_right, first_serve

    # 첫번째 서브를 기다립니다:
    if(first_serve == True):
        my_ball.stop_ball()
        first_serve = False
    
    #공을 일정 시간마다 움직이게함
    my_ball.move_next()
    window.after(30, game_flow) #30밀리초마다 함 실행
    
    #공이 배트에 닿았는지 충돌확인 
    bat_L.detect_collision(my_ball)
    bat_R.detect_collision(my_ball)

    ##공이 좌우 벽에 충돌 했을 때 처리
      #공이 x좌표값이 0보다 작으면 왼쪽벽에 충돌
    if(my_ball.x_posn<=0):
        my_ball.stop_ball()  # 공이 멈춤
        my_ball.start_position() # 공 위치 초기화
        bat_L.start_position() #배트위치 초기화
        bat_R.start_position()
        my_table.move_item2(bat_L.rectangle, (20+35)/2, (150+250)/2)
        my_table.move_item2(bat_R.rectangle, (565+580)/2, (150+250)/2)
    #득점판 득점 표시
        score_right += 1
        if(score_right>=3):
            score_right="W"
            score_left="L"
        my_table.draw_score(score_left, score_right)
        
    # 이건 오른쪽 벽 
    if(my_ball.x_posn+my_ball.width>=my_table.width):
        my_ball.stop_ball() 
        my_ball.start_position()
        bat_L.start_position()
        bat_R.start_position()
        my_table.move_item2(bat_L.rectangle, (20+35)/2, (150+250)/2)
        my_table.move_item2(bat_R.rectangle, (565+580)/2, (150+250)/2)
    #이것도 득점
        score_left += 1
        if(score_left>=3):
            score_left="W"
            score_right="L"
        my_table.draw_score(score_left, score_right)
    
def restart_game(master):
    global score_left, score_right
    
    my_ball.start_ball(x_speed=x_speed, y_speed=y_speed)

    if(score_left=="W" or score_right=="W"):
        score_left=0
        score_right=0
        my_table.draw_score(score_left, score_right)
    
    bat_L.start_position()
    bat_R.start_position()
    my_table.move_item2(bat_L.rectangle, (20+35)/2, (150+250)/2)
    my_table.move_item2(bat_R.rectangle, (565+580)/2, (150+250)/2)
    

### Table 클래스를 사용해서 테이블 생성
my_table=Table(window, 600, 400, PhotoImage(file="../PPbg.png")) 
                                                                                           
### 공생성
#Ball(self, table, width, height, color, x_speed, y_speed, x_posn, y_posn)
my_ball=Ball(table=my_table, x_speed=5, y_speed=5, width=24, height=24, color="orange", x_posn=288, y_posn=188)
my_ball.move_next()

###배트생성
#Bat(self, table, width, height, color, x_speed=25, y_speed=25, x_posn, y_posn)
bat_L=Bat(table=my_table, width=15, height=100, batImage=PhotoImage(file="../bat1.png"), x_posn=20, y_posn=150)
bat_R=Bat(table=my_table, width=15, height=100, batImage=PhotoImage(file="../bat2.png"), x_posn=565, y_posn=150)

####함수의 실행부
game_flow()

#스페이스바를 눌러 게임시작또는 재시
window.bind("<space>", restart_game)



###배트를 제어하기 위한 키 이벤트 및 연결될 함수 지정
#window.bind("<키명>", 함수명)
window.bind("<Up>", bat_R.move_up)
window.bind("<Down>", bat_R.move_down)
window.bind("<w>", bat_L.move_up)
window.bind("<s>", bat_L.move_down)


window.mainloop()
