# 변수명 정하기
# 1. 영문과 숫자, _로 이루어진다
# 2. 대소문자를 구분한다
# 3. 문자나, _로 시작한다
# 4. 특수문자를 사용하면안된다(%,$)
# 5. 키워드를 사용하면 안된다(if, for)

a = 1 #1을 a라는 변수에 대입한다
A = 2
A1 = 3
# 2b = 3
_b = 4
print(a,A, A1)

a,b,c = 3,2,1 #기존 a값을 지우고 새로운 값이 들어감
print(a,b,c)

#값교환
a,b = 10,20
print(a,b)
a,b = b,a
print(a,b)

#변수 타입
a = 12345
print(type(a)) #정수형
a = 12.1234567890
print(type(a)) #실수형은 8파이트까지 넣을수 있으므로 7에서 짤린다
a = 'student'
print(type(a)) #문자형

#출력방식
print("number")
a,b,c = 1,2,3
print(a,b,c)
print("number : ",a,b,c)
print(a,b,c, sep = ', ') #사이에 ,를 넣어서 출력하라
print(a,b,c, sep = '\n')
print(a, end = '  ') #기본적으로 있는 줄바꿈을 없애고 띄어쓰기를 넣었다
print(b, end = '  ')
print(c)


