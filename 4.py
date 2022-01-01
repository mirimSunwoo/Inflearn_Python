#반복문(for, while)

a = range(1,10) #정수 리스트(1~10까지 생성)
print(list(a))

for i in range(1,11): #10번 반복한다
    print(i)

for i in range(10,0, -2): #감소하고 싶다면 값을 하나 더 추가해서 -1울 넣어주어야한다(간격도 바꿀 수 있다
    print(i)

i = 1
while i<=10:
    print(i)
    i = i+1

i = 10
while i>=1:
    print(i)
    i = i-1

# break, continue

i = 1
while True:
    print(i)
    if i== 10:
        break #반복문을 멈추게 한다
    i+=1

for i in range(1,11):
    if i%2==0:
        continue #특정값을 실행하지 않는다
    print(i)

##for~else구문(정상종료가 된다면 else문을 거침)
for i in range(1,11):
    print(i)
    if i >15: #정상종료가 되지 않는다면 else를 거치지 않고, 정상종료가 된다면 else를 거쳐 11까지 출력하게 된다
        break
else:
    print(11)