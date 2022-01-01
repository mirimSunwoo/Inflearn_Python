#변수입력과 연산자

a = input("숫자를 입력하세요 : ")
print(a)

a,b = input("숫자를 입력하세요 : ").split()
print(a+b) #a,b가 문자형이기 때문에 더해지지 않고 글자가 붙어서 나온다

a,b = map(int,input("숫자를 입력하세요 : ").split()) #map은 자신이 원하는 형으로 만드는 내장함수 이다(맵핑한다는뜻)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #몫
print(a%b) #나머지
print(a**b) #거듭제곱

a = 4.3
b = 5
c = a+b
print(type(c)) #실수와 정수가 연산되면 실수형으로 나온다(실수>정수) => 더 큰 범위의 형으로 바뀐다
