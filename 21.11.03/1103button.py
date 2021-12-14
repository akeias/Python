from tkinter import *

window=Tk()
window.geometry("210x210")

"""
#이미지 생성
photoList1=PhotoImage(file="../gif/puz1.gif")
photoList2=PhotoImage(file="../gif/puz2.gif")
photoList3=PhotoImage(file="../gif/puz3.gif")

#버튼 생성
button1=Button(window, text="버튼1") / 이미지의 경우 image=photoList[i] 
button2=Button(window, text="버튼2")
button3=Button(window, text="버튼3")


#버튼 출력
button1.pack(side=LEFT) / 좌표로 위치 지정시  .place(x=0,y=0)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
"""
#위의 노가다를 반복문과 리스트를 활용하여 소스코드 수정하기
#빈공간 만들기
button=[None]*9 
photoList=[None]*9
xPos, yPos=0,0
i=0

#이중포문을 이용해서 3x3버튼 만들기->이미지도 추가
for y in range(0,3):
    for x in range(0,3):
        photoList[i]=PhotoImage(file="../gif/puz"+str(i+1)+".gif")
        button[i]=Button(window, image=photoList[i])
        button[i].place(x=xPos,y=yPos) #x=0, y=0으로 시작
        xPos+=70 # for x 가 반복되면 xPos가 70씩 오름
        i+=1 
    xPos=0 #for y가 한싸이클 반복이 끝나면 xPos이 0으로 초기화 됨
    yPos+=70 # 이후 yPos값이 70이 오름 이상태로 다시 for x가 작동




window.mainloop()
