#조건문
"""
if 조건식:
    실행할 문장
"""

a=99 #a변수 선언 및 값 대입
if a<100:
    print("100보다 작군요.")


"""
if~else 문 : 참일 때 실행하는 문장과 거짓일 때 실행하는
                문장이 다를 때 사용
if 조건식:
    실행할 문장
else:
    실행할 문장  *주의할점: if와 else는 같은 라인에 있어야한다.

"""
a=110
if a<100:
    print("%d는 100보다 작군요."%a)
else:
    print("%d는 100보다 크군요."%a)
    

#if~else 문 변형 : 사용자로 입력받아 a 값에 대입
print("if~else 문 변형")

a=int(input("정수를 입력하세요."))
if a<100:
    print("%d는 100보다 작군요"%a)
else:
    print("%d는 100보다 크거나 같군요,"%a)


#중첩 if문
print("중첩 if문")

a=int(input("정수를 입력하세요."))

if a<100:
    print("%d는 100보다 작군요"%a)
else:
    if a>100:
        print("%d는 100보다 크군요"%a)
    else:
        print("%d는 100이군요."%a)


#if~elif~else 문

print("if~elif~else 문(학점)")

score=int(input("점수를 입력하세요.:"))

if score>=90:
    print("A",end="")
elif score>=80:
    print("B",end="")
elif score>=70:
    print("C",end="")
elif score>=60:
    print("D",end="")
else:
    print("F",end="")
print("학점입니다.")
print("수고하셨습니다.")


#간단한 계산기 만들기

print("간단한 계산기")

# 변수 선언 부분
a,b,ch=0,0,""

#메인 코드 부분
a=int(input("첫 번째 수를 입력하세요.:"))
ch=input("계산할 연산자를 입력하세요.:")
b=int(input("두 번째 수를 입력하세요.:"))

if ch=="+":
    print("%d+%d=%d 입니다."%(a,b,a+b))
elif ch=="-":
    print("%d-%d=%d 입니다."%(a,b,a-b))
elif ch=="*":
    print("%d*%d=%d 입니다."%(a,b,a*b))
elif ch=="/":
    print("%d/%d=%0.2f 입니다."%(a,b,a/b))
elif ch=="//":
    print("%d로 %d나눈 몫은%d 입니다."%(a,b,a//b))
elif ch=="%":
    print("%d로 %d나눈 나머지 값은 %d 입니다."%(a,b,a%b))
elif ch=="**":
    print("%d**%d=%d 입니다."%(a,b,a**b))
else:
    print("알 수 없는 연산자입니다.")
    





        
