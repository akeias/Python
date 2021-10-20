## 함수 정의 부분
def calc(v1,v2,op):
    result=0
    if op=='+':
        result=v1+v2
    elif op=='-':
        result=v1-v2
    elif op=='*':
        result=v1*v2
    elif op=='/':
        result=v1/v2

    return result

##변수 선언 부분
res=0
var1,var2,oper=0,0,""

##메인 코드 부분
while True:
    oper=input("원하시는 계산방법을 입력하시오.(+,-,*,/):")
    var1=int(input("첫 번째 숫자를 입력하시오.:"))
    var2=int(input("두 번째 숫자를 입력하시오.:"))

    res=calc(var1,var2,oper)

    print("계산기: %d %s %d = %d"%(var1,oper,var2,res))






