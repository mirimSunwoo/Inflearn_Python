# 리스트와 내장함수

import  random as r

a=[] #빈 리스트만들기
b = list() #빈 리스트 만들기2

a = [1,2,3,4,5]
print(a)
print(a[0]) #a의 0번 인덱스를 출력하라

b = list(range(1,11)) #range를활용한 리스트 만들기
print(b)

c= a+b #리스트를 합칠 수 있다
print(c)

print(a)
a.append(6) #값을 추가함(뒤에다가)
print(a)

a.insert(3,7) #3번 인덱스에 7이 들어감(원하는곳에 추가)
print(a)

a.pop() #끝에서 하나를 꺼냄
print(a)
a.pop(3) #3번 인덱스 값을 꺼내서 사라짐
print(a)

a.remove(4) #4를 찾아서 제거함
print(a)

print(a.index(5)) #5라는 값이 몇번인덱스에 있는지 출력해줌

a = list(range(1,11))
print(a)
print(sum(a)) #a리스트의 합을 출력
print(max(a)) #a리스트의 최대값을 출력
print(min(a)) #a리스트의 최솟값을 출력
print(min(7,5)) #7과 5 중에서 최솟값을 찾음
print(min(7,5,3)) #7과 5,3 중에서 최솟값을 찾음

r.shuffle(a) #무작위로 섞음
print(a)
a.sort() #오름차순으로 바꿈
print(a)
a.sort(reverse=True) #내림차순
print(a)