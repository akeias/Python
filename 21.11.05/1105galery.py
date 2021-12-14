from tkinter import * #tk기능 불러오기
from time import * #time기능? 불러오기

#변수 선언 부분

fnameList=["photo1.png","photo2.png","photo3.png","photo4.png","photo5.png","photo6.png",
           "photo7.png","photo8.png","photo9.png"]
nameList=["2014년", "2016년", "2016년", "2016년", "2017년", "2018년", "2018년", "2015년", "2014년" ]
photoList=[None]*9
num=0

#함수 선언 부분

def clickNext():
    global num  #밖에있는 전역변수를 가져와 사용하겠다는 것 
    num+=1      #다음 사진을 보이기 위해 사진번호를 1씩 증가
    if num>8:    
        num=0   # num이 8이넘으면 0으로 돌아간다.

    photo=PhotoImage(file="../../MYBOX/"+fnameList[num])
    tLabel.configure(text = nameList[num]) 
    pLabel.configure(image=photo)
    pLabel.image=photo

def clickPrev():     #clickNext의 반대 작동원리는 같
    global num
    num-=1
    if num<0:
        num=8

    photo=PhotoImage(file="../../MYBOX/"+fnameList[num])
    tLabel.configure(text = nameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo


#메인 코드 부분

window=Tk()
window.geometry("1080x720")
window.title("My Photo Gallery")
window.resizable(width=FALSE, height=FALSE) #크기조정가능여부
window.configure(background="black")


photo=PhotoImage(file="../../MYBOX/"+fnameList[0])
pLabel=Label(window, image=photo)
photoButton1=PhotoImage(file="../../MYBOX/button1.png")
photoButton2=PhotoImage(file="../../MYBOX/button2.png")

label1=Label(window, text="My photo Gallery ",font=("궁서체",30), fg="white",bg="black")
label2=Label(window, text="Since:2014~2018 ",font=("HY나무B",15), fg="white",bg="black")
btnPrev=Button(window, image=photoButton1, command=clickPrev, borderwidth=0)
btnNext=Button(window, image=photoButton2, command=clickNext, borderwidth=0)
tLabel = Label(window, text = nameList[0] ,bg="black", fg="white", font=("HY나무B",20))



pLabel.place(x=140,y=150)
label1.place(x=385,y=40)
label2.place(x=470,y=100)
btnPrev.place(x=140,y=610)
btnNext.place(x=820,y=610)
tLabel.place(x=500,y=610)


window.mainloop()



    
