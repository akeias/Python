from tkinter import *

### 전역 변수
score_left=0 #왼쪽 득점판
score_right=0 #오른쪽 득점판

### Table 클래스 생성

class Table:
    ####생성자
    def __init__(self, window, width, height, bgImage):
        self.width=width
        self.height=height
        self.bgImage=bgImage

        #Table 클래스 내에서 캔버스 생성
        self.canvas=Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        self.canvas.create_image(0, 0, anchor=NW, image=bgImage)

        #Table 클래스 내에서 득점판 생성
        font=("monaco", 65)
        self.scoreboard=self.canvas.create_text(self.width/2, 65, font=font ,fill="sea green1", text=str(score_left)+" "+str(score_right))

    ###함수부
    #Canvas(Table)에 공을 추가하는 함수
    def draw_oval(self,oval): # oval은 넘어온 ball
        x1=oval.x_posn
        x2=oval.x_posn+oval.width
        y1=oval.y_posn
        y2=oval.y_posn+oval.height
        c=oval.color
        return self.canvas.create_oval(x1, y1, x2, y2, fill=c)

    #Canvas(Table)에 배트를 추가하는 함수
    def draw_rectangle(self,rectangle): 
        x1=rectangle.x_posn
        x2=rectangle.x_posn+rectangle.width
        y1=rectangle.y_posn
        y2=rectangle.y_posn+rectangle.height
        c=rectangle.batImage
        return self.canvas.create_image((x1+x2)/2, (y1+y2)/2, image=c)
        

    #Canvas(Table)에 아이템(공과 배트)를 조작할 수 있는 함수 coords() 이용
    #변경된 위치값으로 공과 배트의 위치 변경          #coords)_는 입력받은 값으로 속성값을 업데이트하는 함수
    def move_item1(self, item, x1, y1, x2, y2):
        self.canvas.coords(item, x1, y1, x2, y2)
        
    def move_item2(self, item, x, y):
        self.canvas.coords(item, x , y)

    #Canvas(Table)에 득점판을 갱신하는 함수
    def draw_score(self, left, right):
        scores=str(left)+" "+str(right)
        self.canvas.itemconfigure(self.scoreboard, text=scores)
