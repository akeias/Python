#21.10.15 이경민 논리연산자

#변수 선언
w=0
select=0

#메인 코드

select=int(input("성별을 입력하세요.(1.남성, 2.여성)"))
w=int(input("체중을 입력하세요."))

if select==1: 
    if w>= 85:
        print("과제충 입니다, 운동하세요.")
    elif 50<=w<85:
        print("표중체중 입니다. 현 페이스를 유지하세요.")
    elif w<50:
        print("표준체중 이하입니다. 고기드세요.")
elif select==2:

    if w>= 68:
        print("과제충 입니다, 운동하세요.")
    elif 40<=w<68:
        print("표중체중 입니다. 현 페이스를 유지하세요.")
    elif w<40:
        print("표준체중 이하입니다. 고기드세요.")
else:
    print("1 또는 2만 입력해야합니다.")
    



