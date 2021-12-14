from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from wand.image import *

window, canvas, paper=None, None, None
photo, photo2=None, None 
oriX,oriY,newX, newY=0,0,0,0
menu1=["저장","이미지 처리(1)","명도","채도","색상도","미구현"]

# 함수 정의 부분
def displayImage(img, width, height) :
    global window,canvas, paper, photo, photo2, oriX, oriY

    window.geometry("1080x720")
    if canvas != None :
        canvas.destroy()

    canvas = Canvas(window, width=width, height=height, bd=0, highlightthickness=0,bg="white")
    paper=PhotoImage(width=width, height=height)
    blob=img.make_blob(format="png")
    paper.put(blob)
    canvas.create_image( (width/2, height/2), image=paper, state="normal")
    canvas.place(x=-2 ,y=112)
    
def func_open() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    readFp = askopenfilename(parent=window, filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"),  ("모든 파일", "*.*") ))
    photo = Image(filename=readFp)
    oriX = photo.width
    oriY = photo.height

    photo2 = photo.clone()
    newX = photo2.width 
    newY = photo2.height

    string = readFp
    p =string.split('/')
    s = len(p)
    label1.configure(text=str(p[s-1]))
    
    displayImage(photo2, newX, newY)
    
    for i in range(len(menu1)):
        mainMenu.entryconfig(i, state = "normal")
    #저장이랑 미구현 태그 아직 활성화가 안됨.
        #웨 안될까 저장은 이름이 다르다 쳐도 미구현태그는 왜? 



def func_save() :
    global window,canvas, paper, photo, photo2, oriX, oriY

    if photo2 == None :
        return
    saveFp = asksaveasfile(parent=window, mode="w", defaultextension=".jpg", filetypes=(("JPG 파일", "*.jpg;*.jpeg"),  ("모든 파일", "*.*") ))
    savePhoto = photo2.convert("jpg")
    savePhoto.save(filename=saveFp.name)

def func_exit() :
    window.quit()
    window.destroy()

def func_zoomin() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("확대배수", "확대할 배수를 입력하세요", minvalue=2, maxvalue=4)
    photo2 = photo.clone()
    photo2.resize( int(oriX * scale) , int(oriY * scale) )
    newX = photo2.width 
    newY = photo2.height    
    displayImage(photo2, newX, newY)

def func_zoomout() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("축소", "축소할 배수를 입력하세요", minvalue=2, maxvalue=4)
    photo2 = photo.clone()
    photo2.resize( int(oriX / scale) , int(oriY / scale) )
    newX = photo2.width 
    newY = photo2.height    
    displayImage(photo2, newX, newY)

def func_mirror1() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.clone()
    photo2.flip()
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_mirror2() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.clone()
    photo2.flop()
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_rotate() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    degree = askinteger("회전", "회전할 각도를 입력하세요", minvalue=0, maxvalue=360)
    photo2 = photo.clone()
    photo2.rotate(degree)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_bright() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    value = askinteger("밝게", "값을 입력하세요(100~200)", minvalue=100, maxvalue=200)
    photo2 = photo.clone()
    photo2.modulate(value, 100, 100)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)    

def func_dark() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    value = askinteger("어둡게", "값을 입력하세요(0~100)", minvalue=0, maxvalue=100)
    photo2 = photo.clone()
    photo2.modulate(value, 100, 100)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)
    
def func_clear() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    value = askinteger("선명하게", "값을 입력하세요(100~200)", minvalue=100, maxvalue=200)
    photo2 = photo.clone()
    photo2.modulate(100, value, 100)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_unclear() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    value = askinteger("탁하게", "값을 입력하세요(0~100)", minvalue=0, maxvalue=100)
    photo2 = photo.clone()
    photo2.modulate(100, value, 100)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_color() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    value = askinteger("색상도", "값을 입력하세요(0~255)", minvalue=0, maxvalue=255)
    photo2 = photo.clone()
    photo2.modulate(100, 100, value)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)
    
def func_bw() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.clone()
    photo2.type="grayscale"
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_undo():
    pass    # 포토2,위드,헤이트 리스트만들고 디스플레이 발동할대 각각의 값을 저장하는식
                # 근데 못하겟삼 ㅠㅠ 머리만 아픔 ㅜ 
def func_redo():
    pass        #암튼 이두기능 만들구 나면 창안에 창 넣기랑 버튼이미지써서 파일만 냅두고
                    #나머지는 다 버튼을 넣어서 만들자
                        #원본으로 돌리는 기능도 넣자 
    
# 변수 선언 부분
window,canvas, paper=None, None, None
photo, photo2=None, None
oriX,oriY= 0,0

# 메인 코드 부분
window = Tk()
window.geometry("1080x720")
window.title("포토?샵")
window.resizable(width=FALSE, height=FALSE)

filename1=PhotoImage(file="../../MYBOX/bgImage.png")
imagelabel1=Label(window, image=filename1)
imagelabel1.place(x=-2,y=-2)

label1=Label(window, text= "파일명",font=("HY나무B",15))
label1.place(x=900 , y=40)

mainMenu = Menu(window)
window.config(menu=mainMenu)
photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack( expand=1, anchor=CENTER)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)

fileMenu.add_command(label="새 파일", command=func_open)
fileMenu.add_command(label="저장", command=func_save ,state = "disable")
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지 처리(1)", menu=image1Menu, state = "disable")

image1Menu.add_command(label="확대", command=func_zoomin)
image1Menu.add_command(label="축소", command=func_zoomout)
image1Menu.add_separator()
image1Menu.add_command(label="상하 반전", command=func_mirror1)
image1Menu.add_command(label="좌우 반전", command=func_mirror2)
image1Menu.add_command(label="회전", command=func_rotate)

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label="명도", menu=image2Menu,state = "disable")

image2Menu.add_command(label="밝게", command=func_bright)
image2Menu.add_command(label="어둡게", command=func_dark)

image3Menu = Menu(mainMenu)
mainMenu.add_cascade(label="채도", menu=image3Menu,state = "disable")
image3Menu.add_command(label="선명하게", command=func_clear)
image3Menu.add_command(label="탁하게", command=func_unclear)

image4Menu = Menu(mainMenu)
mainMenu.add_cascade(label="색상도", menu=image4Menu,state = "disable")
image4Menu.add_command(label="색상조절", command=func_color)
image4Menu.add_command(label="흑백이미지", command=func_bw)

UndoMenu = Menu(mainMenu)
mainMenu.add_cascade(label="미구현", menu=UndoMenu,state = "disable")
UndoMenu.add_command(label="Undo", command=func_undo)
UndoMenu.add_command(label="Redo", command=func_redo)

window.mainloop()
