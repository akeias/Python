#for문

"""
for 변수 in range(시작값, 끝값+1, 증가값):
    반복 실행할 문장 프린트
"""
for i in range(0,3,1):
    print("안녕하세요? for문을 공부중입니다. ^^")

"""
for 변수 in [배열]:
    반복 실행할 문장 프린트
"""
for i in [0,1,2]:
    print("안녕하세요? for문을 공부중입니다. ^^")

for i in range(1,6,1): #증가값과 시작값은 생략이 가능
    print("%d" %i, end=" ") #end=" "는 한줄로 결과 출력

#1에서 10까지의 합을 구하기 
hap=0

for i in range(1,11,1):
    hap=hap+i #곱일 경우 연산자를 *로 바꾸고 hap이 0이아닌 1로 시작
    print(hap) #중간과정이 궁금할 때 print로 출력해보기

print("1에서 10까지의 합 : %d"%hap)

#500과 1000사이에 있는 홀수의 합 구하기
"""
i,hap=0,0

for i in range(501,1001,2):
    hap=hap+i

print("500에서 1000까지의 홀수의 합:%d"%hap)
"""
#위 아래 동일 식 

i,hap=0,0

for i in range(501,1001,1):
    if i%2 == 1:  # ==1은 !=0 으로써두댐 
        hap=hap+i

print("500에서 1000까지의 홀수의 합:%d"%hap)

#입력한 값까지 합 구하기

i,hap=0,0
num1,num2,num3=0,0,0

num1=int(input("시작값 입력:"))
num2=int(input("끝값 입력:"))
num3=int(input("증가값 입력:"))

for i in range(num1,num2+1,num3):
    hap=hap+i

print("%d에서 %d까지 %d씩 증가한 값의 합 : %d"%(num1,num2,num3,hap))

#구구단 만들기
i,dan=0,0

dan=int(input("몇 단?"))

for i in range(1,10,1):
    print("%dX%d=%d"%(dan,i,dan*i))
