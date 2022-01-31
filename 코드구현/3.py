# k번째 큰 수
import sys

sys.stdin = open("input_3.txt", "rt")
n, K = map(int, input().split())  # 두개의 자료를 리스트에 넣음
a = list(map(int, input().split()))  # n개의 자료를 리스트에 넣음

# 중복제거(set)
res = set()

# 3개의 자료만(중복방지)
for i in range(n):  # 1번
    for j in range(i + 1, n):  # 2번
        for m in range(j + 1, n):  # 3번
            res.add(a[i] + a[j] + a[m])  # 값추가
res = list(res)  # res를 list화 시켜줌
res.sort(reverse=True)
print(res[K - 1])
