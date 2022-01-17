# 문자열과 내장함수

msg = "It is Time"
print(msg.upper()) #대문자(원본유지)
print(msg.lower()) #소문자(원본유지)
print(msg)

tmp = msg.upper() #대문자(원본바뀜)
print(tmp)

print(tmp.find('T')) #T의 인덱스 찾기(인덱스는 0부터 시작)
print(tmp.count('T')) #T의 갯수 찾기

print(msg)
print(msg[:2]) #처음부터 인덱스 2전까지 뽑아내서 출력한다(index:0,1)
print(msg[3:5]) #인덱스 3부터 5전까지 출력한다(index:3,4)

print(len(msg)) #msg문자열의 길이를 반환해준다

#접근방법1
for i in range(len(msg)): #0~9까지 돌림
    print(msg[i], end=' ')
print()

#접근방법2
for x in msg:
    print(x, end=' ')
print()

#대문자만 출력
for x in msg:
    if x.isupper(): #x가 대문자인지 탐색
        print(x, end='')
print()

#소문자만 출력
for x in msg:
    if x.islower(): #x가 소문자인지 탐색
        print(x, end='')
print()

#공백제거
for x in msg:
    if x.isalpha(): #알파벣인지 탐색
        print(x, end='')
print()

#아스키 문자 출력(A:65~Z:90)
tmp = 'AZ'
for x in tmp:
    print(ord(x))

#아스키 문자 출력(a:97~z:122)
tmp = 'az'
for x in tmp:
    print(ord(x))

tmp = 65
print(chr(tmp))