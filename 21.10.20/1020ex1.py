## 함수 정의 부분
def plus(v1,v2):
    result=0
    result=v1+v2
    return result

## 변수 선언 부분
hap=0

##메인 코드 부분
while True:
    a=int(input("더할 값을 입력해주세요."))
    b=int(input("더할 값을 입력해주세요."))
          
    hap=plus(a,b)
          
    print("%d과 %d의 plus()함수 결과는 %d"%(a,b,hap))
