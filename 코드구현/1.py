#k번째 약수 풀이
import sys
sys.stdin = open("input.txt",'rt')

n,k = map(int, input().split()) #각각의 숫자들을 int형으로 바꿈
cnt = 0
for i in range(1,n+1):
    if n%i == 0: #약수찾기
        cnt += 1
    if cnt==k:
        print(i)
        break
else: #정상적으로 끝났을때 else문 사용
    print(-1)
