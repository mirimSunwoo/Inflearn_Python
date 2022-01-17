#반복문을 이용한 문제풀이

#1부터 N까지 홀수 출력하기
n = int(input())
for i in range(1,n+1):
    if i%2 == 1:
        print(i)
#1부터 N까지 합 출력하기
n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)
#N의 약수 출력하기
n = int(input())
for i in range(1,n+1):
    if n%i == 0:
        print(i, end='')

n = int(input()) #정수형으로 바꿔주지 않으면 문자형으로 인식되어서 오류가남
for i in range(1,n+1):
    print(i)

