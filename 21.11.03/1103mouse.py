from tkinter import *
from tkinter import messagebox

#함수 정의 부분
#키보드나 마우스를 누르는것을 이벤트(event)라고함
"""
def clickLeft(event):
    messagebox.showinfo("마우스","마우스 왼쪽 버튼이 클릭됨.")

def clickRight(event):
    messagebox.showinfo("마우스","마우스 오른쪽 버튼이 클릭됨.")
    
def clickRabbit(event):
    messagebox.showinfo("마우스","토끼에 마우스가 올라감.")
"""
def clickMouse(event):
    txt=""
    if event.num==1:
        txt+="마우스 왼쪽 버튼이 ("
    elif event.num==3:
        txt+="마우스 오른쪽 버튼이("
    txt+="x"+str(event.x)+",y"+str(event.y)+")에서 클릭됨"
    label1.configure(text=txt)
    label1.place(x=str(event.x),y=str(event.y)) # 마우스를 누르는곳에 출력이 되도록해줌

#메인 코드 부분
window =Tk()
window.geometry("400x400")

label1=Label(window, text="이곳이 바뀜")

"""
photoList=PhotoImage(file="../gif/rabbit.gif")
imagelabel=Label(window, image=photoList)
imagelabel.pack(expand=1, anchor=CENTER)
#expane: 미사용 공간 확보, True,False
#할당되지 않은 미사용 공간을 모두 현재 위젯의 할당된 공간으로 변경

imagelabel.bind("<Enter>", clickRabbit)     
window.bind("<Button-1>",clickLeft)  # 버튼1은 왼쪽
window.bind("<Button-3>",clickRight) # 버튼 3은 오른쪽/ 2는 가운데라는데 휠인듯?
"""

window.bind("<Button>",clickMouse)

label1.pack(expand=1, anchor=CENTER)

window.mainloop()
