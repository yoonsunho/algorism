# << 연산자
# 1<<n : 2^n 즉, 원소가 n개일 경우의 모든 부분집합의 수를 의미

# & 연산자
# i &(1<<j) : i의 j번째 비트가 1인지 아닌지를 검사

# 잘 모르겠음...
arr = [3, 6, 7, 1, 5, 4]

n = len(arr)    # n: 원소의 개수

for i in range(1 << n):   # 1<<n : 부분집합의 개수
    for j in range(n):  # 원소의 수만큼 비트를 비교
        if i & (1 << j):    # i의 j 번 비트가 1인경우
            print(arr[j], end=', ')  # j 번 원소 출력
    print()
print()
