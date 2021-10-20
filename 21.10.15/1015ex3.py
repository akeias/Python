#21.10.15 이경민 비교연산자


#변수선언
X=0

#메인코드

while True:
    X=int(input("성적을 입력하세요:"))

    if X>= 95:
        print("축하합니다. A+입니다.")
    elif 95>X>=90:
        print("축하합니다. A입니다.")
    elif 90>X>=85:
        print("축하합니다. B+입니다.")
    elif 85>X>=80:
        print("축하합니다. B입니다.")
    elif 80>X>=75:
        print("축하합니다. C+입니다.")
    elif 75>X>=70:
        print("축하합니다. C입니다.")
    elif 70>X>=65:
        print("축하합니다. D+입니다.")
    elif 65>X>=60:
        print("축하합니다. D입니다.")
    elif 60>X:
        print("축하합니다. F입니다.^^;;")
    print("계속하시려면 아무키나 입력하세요.")
    input(continue)
