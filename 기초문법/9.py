# 리스트와 내장함수(2)

a= [23,12,36,53,19]

print(a[:3]) #슬라이싱 기능
print(a[1:4])

print(len(a)) #리스트의 값이 몇개가 있는지

for i in range(len(a)): #리스트 값을 인덱스로 접근
    print(a[i], end= ' ')
print()

for x in a:
    print(x, end = ' ') #리스트 값 출력_2
print()

for x in a:
    if x % 2 ==1:
        print(x, end = ' ')
print()

for x in enumerate(a):#인덱스와 값을 둘다 출력함
    print(x)

b = [1,2,3,4,5] #()는 튜플, 값을 바꿀 수 없음
print(b[0])
# b[0] =  7#리스트는 값을 변경할 수 있음

for x in enumerate(a):
    print(x[0],x[1])
print()

for index, value in enumerate(a): #제일 많이 쓰는 방법
    print(index, value)
print()

if all(50>x for x in a): #for문과 조건문을 같이쓴 문장
    #all은 하나라도 거짓이면 false를 출력함
    print("YES")
else:
    print("NO")

if any(15>x for x in a): #for문과 조건문을 같이쓴 문장
    #any는 조건이 하나라도 만족하면 True를 출력함
    print("YES")
else:
    print("NO")
