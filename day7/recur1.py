def f(i, N):
    if i == N:    # 중단조건
        return
    else:  # 재귀호출
        f(i+1, N)

f(0, 3)
# f(0, 1000)      # RecursionError: maximum recursion depth exceeded in comparison

def f(i, N): # i 배열 인덱스, N 배열크기
    if i==N:    # 중단조건
        return
    else:  # 재귀호출
        print(A[i])
        f(i+1, N)

A = [1,2,3]
f(0, 3)     # 1 2 3