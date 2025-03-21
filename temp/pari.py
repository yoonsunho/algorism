import sys
sys.stdin = open("pari.txt", "r")

T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int, input().split())     # 5 <= N <=15, 2 <= M <= N

    area = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N-M+1):
       for j in range(N-M+1):
           pari_sum = 0
           for l in range(M):
               for k in range(M):
                   pari_sum += area[i+l][j+k]
           max_v = max(max_v, pari_sum)

            # pari_sum += area[i][j]
            # max_v = max(pari_sum, max_v)

    
    print(f'#{test_case} {max_v}')
