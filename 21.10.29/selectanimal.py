#라벨, 라디오버튼, 버튼, 이미지 모두 활용
from tkinter import *
window=Tk( )
window.geometry("1280x800")
window.title("애완동물 선택 하기")

#함수 정의 부분


def myFunc2():
    if var.get()==1:
        labelText2.configure(text="강아지를 좋아하시네요^^")
        labelImage.configure(image=photo1)
    elif var.get()==2:
        labelText2.configure(text="고양이를 좋아하시네요^^")
        labelImage.configure(image=photo2)
    else:
        labelText2.configure(text="토끼를 좋아하시네요^^")
        labelImage.configure(image=photo3)

#메인 코드 부분

#배경이미지 표시
filename1=PhotoImage(file="../gif/nature.png")
imagelabel1=Label(window, image=filename1)
imagelabel1.place(x=-2,y=-2)

labelText=Label(window, text="좋아하는 동물 투표", fg="blue", font=("나눔고딕", 20))

var=IntVar()
rb1=Radiobutton(window, text="강아지", variable=var, value=1,command=myFunc2)
rb2=Radiobutton(window, text="고양이", variable=var, value=2,command=myFunc2)
rb3=Radiobutton(window, text="토끼", variable=var, value=3,command=myFunc2)
labelText2=Label(window, text="무엇을 좋아하시나요?", fg="black")

photo1=PhotoImage(file="../gif/dog2.gif")
photo2=PhotoImage(file="../gif/cat2.gif")
photo3=PhotoImage(file="../gif/rabbit.gif")


labelImage=Label(window, width=200, height=200, bg="black", image=photo1)

labelText.pack(padx=5, pady=5)
rb1.pack(padx=5, pady=5)
rb2.pack(padx=5, pady=5)
rb3.pack(padx=5, pady=5)
labelImage.pack(padx=5, pady=5)
labelText2.pack()

window.mainloop()

