
#tkinter는 파이썬에서 GUI관련 모듈을 제공 
#위젯(widget)-윈도우 창에 나올 수 있는 문자,버튼,체크박스,라디오버튼 등
from tkinter import *
from tkinter import messagebox
#messagebox는 현재 버전 이후에 나온 기능이라 따로 추가해줘야함


#함수 정의 부분
def myFunc():
    messagebox.showinfo("강아지버튼", "강아지가 귀엽죠?")
    #버튼을 눌렀을 때, 간단한 메세지 창이 나오도록 해주는 함수

def myFunc1():
    if chk.get()==0:
        messagebox.showinfo("","체크버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("","체크버튼이 켜졌어요.")
    #chk.get()함수로 체크버튼에 설정된 값을 가져와 메세지 출력

def myFunc2():
    if var.get()==1:
        Label1.configure(text="파이썬")
    elif var.get()==2:
        Label1.configure(text="C++")
    else:
        Label1.configure(text="Java")
    #위젯명.configure(옵션=값)은 해당 위젯의 옵션값을 변경해주는 함수
    #var값에 따라 출력되는 값이 다름


#메인 코드 부분
window=Tk( )
#tk는 기본이 되는 윈도우를 반환, 루트 윈도우 또는 베이스 윈도우 라고함.

#윈도우창 제목 표시
window.title("윈도창 연습")
#윈도우창 초기 크기 지정
window.geometry("800x600")
#윈도우창의 크기 변경 가능 여부설정/TRUE,FALSE or 0,1
window.resizable(width=TRUE, height=TRUE)


#라벨(Label)은 문자를 표현할 수 있는 위젯
#위젯은 생성하고 디스플레이하는 2스텝으로 진행

#1.라벨 위젯 표시
#step1. 라벨 위젯 생성
label1=Label(window, text="SWEDU~~Python을")
label2=Label(window, text="오늘은 불금", font=("궁서체",30), fg="blue")
label3=Label(window, text="공부 중입니다.", bg="magenta", width=20, height=5, anchor=SE)
#anchor는 위젯의 위치 지정(N,NE,E,SE,W,NW,S,SW,CENTER 등이며 디폴트값은 CENTER다.)

#step2. 라벨 위젯을 화면에 표시
label1.pack() # pack함수를 사용하여 화면에 디스플레이 됨.
label2.pack()
label3.pack()

#2.이미지 위젯 표시
#step.1 이미지 불러오기(gif랑 png만 지원됨 여기선)
filename1=PhotoImage(file="../gif/dog4.gif")
filename2=PhotoImage(file="../gif/dog2.gif")
filename3=PhotoImage(file="../gif/jeju2.gif")
#step.2 라벨 위젯 생성
imagelabel3=Label(window, image=filename3)
imagelabel1=Label(window, image=filename1)
imagelabel2=Label(window, image=filename2)
#step.3 라벨 위젯을 화면에 표시
imagelabel3.place(x=-2,y=-2)
imagelabel1.pack(side=LEFT)
imagelabel2.pack(side=RIGHT)

#3 버튼 위젯 표시
#step1. 버튼 위젯을 생성
button=Button(window, image=filename2, fg="red", command=myFunc)
#버튼에 이미지 표시하는법
"""
button1=Button(window, text="파이썬 종료", fg="red", command=quit)
button1.pack()
프로그램 종료 버튼을 만들어주는 코드
"""
#step2. 버튼 위젯을 화면에 표시
button.pack()

#체크버튼은 다중선택을 하기 위해 사용되는 위젯
#Checkbutton(부모 윈도우,옵션)
chk=IntVar()
#IntVar()는 정수형 형식의 변수를 생성하는 함수
cb1=Checkbutton(window, text="클릭하세요", variable=chk, command=myFunc1)
#체크버튼을 켜면 chk에 1이, 끄면 chk에 0이 대입됨


#체크버튼 cb1 화면 표시
cb1.pack()

#라디오 버튼은 여러개 중 하나를 선택하기 위해 사용되는 위젯
var=IntVar()

rb1=Radiobutton(window, text="파이썬", variable=var, value=1, command=myFunc2)
rb2=Radiobutton(window, text="C++", variable=var, value=2, command=myFunc2)
rb3=Radiobutton(window, text="Java", variable=var, value=3, command=myFunc2)

Label1=Label(window, text="선택한 언어 : ", fg="red")

rb1.pack()
rb2.pack()
rb3.pack()
Label1.pack()


#화면을 구성하고 처리
#윈도우 창에 키보드,마우스 입력 등 다양한 이벤트 처리
window.mainloop()

















