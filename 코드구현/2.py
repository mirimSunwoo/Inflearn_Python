#k번째 수
import sys
sys.stdin = open("input.txt",'rt')

T = int(input()) #입력받은 개수 구하기
for t in range(T): #T만큼 돌려주기
    n, s, e , k = map(int, input().split()) #정수형으로 바꿔주고 띄어쓰기 된걸 나눠준다
    a = list(map(int, input().split())) #리스트에 한줄을 리스트화 시켜서 넣는다
    a = a[s-1:e] #리스트의 s부터 e까지 a에 넣음
    a.sort() #오름차순으로 정렬
    print("#%d %d" %(t+1,a[k-1])) #출력결과 #@ k번째 수 츨력