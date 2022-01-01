#조건문 if(분기, 중첩)

x = 5
if x != 7:
    print("Lucky")
    print("kkk")

x = 15
if x >= 10:
    if x %2 ==1:
        print("10이상의 홀수")


x = 10
# if x>0 and x<10: 두개의 조건을 한번에 묶을 수 있음
# if 0<x<10 파이썬에서는 이런 기능도 가능
if x > 0:
    if x<10:
        print("10보다 작은 자연수")

x = 10 #분기문
if x>0:
    print("양수")
else:
    print("음수")

x = 93
if x>=90: #첫번째 조건문에 걸리면 이것만 출력한다
    print('A')
elif x>=80:
    print('B')
elif x>=70:
    print('C')
elif x>=60:
    print('D')
else:
    print('F')

x = 93
if x>=90: #각자 if기때문에 위에 다중분기와는 다르게 전부 출력된다
    print('A')
if x>=80:
    print('B')
if x>=70:
    print('C')
