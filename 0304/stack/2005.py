import sys
sys.stdin = open("txt/2005.txt", "r")

# 대략 20m

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    pascal = [([1]*(i+1)) for i in range(N)]


    if N >= 3:
        for i in range(2,N):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]




    print(f'#{tc}')
    for i in range(N):
        print(" ".join(map(str,pascal[i])))