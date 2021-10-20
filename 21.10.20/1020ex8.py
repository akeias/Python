def dic_func(**para): #가변매개변수,**은 딕셔너리형태로 전달
    for k in para.keys():#딕셔너리에는 key값이 존재해야함
        print("%s-->%d명입니다."%(k,para[k]))

dic_func(아이오아이=11, 소녀시대=8, 걸스데이=4,AOA=7)

