'''
함수 만들기

def add(a,b): #함수가 밑에 있으면 인식을 못하기때문에 오류가남
    c = a +b
    print(c)

add(3,2)
add(5,7)


def add(a, b):
    c = a+b
    return c #함수 값을 반환, 함수를 끝내주는 역할도 함

x = add(3,2)
print(x)


def add(a,b):
    c = a+b
    b = a-b
    return c,b #여러개의 값을 리턴할 수 있다

print(add(3,2))

'''

def isPrime(x):
    for i in range(2,x):
        if x%i == 0: #다른 약수가 있다면 이것은 약수가 아니다.
            return False #그러므로 false
        return True #다른약수가 없으면 True
a = [12,13,7,9,19]
for y in a :
    if isPrime(y): #여기서 True를 반환 해서
        print(y, end = ' ') #여기서 출력함
