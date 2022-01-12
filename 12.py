'''
람다 함수

def plus_one(x):
    return x+1

print(plus_one(1))

plus_two = lambda x: x+2 #내장함수의 인자로 사용할때 편리하다
print(plus_two(1))

'''

def plus_one(x):
    return x+1

a = [1,2,3]
print(list(map(plus_one,a))) #a가 함수의 적용을 받아서 멥팅이 됨

print(list(map(lambda x:x+1,a))) #위에 코드와 똑같지만 람다함수로 간단하게 표현가능



