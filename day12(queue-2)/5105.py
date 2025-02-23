def bfs(i, j, N):     # 시작 위치i,j, 크기 N
    visited = [[0] * N for _ in range(N)]   # visited 생성
    q = []              # 큐 생성
    q.append([i, j])     # 시작점 인큐
    visited[i][j] = 1    # 시작점 인큐 표시
    # 큐에 남은 칸이 없을 때 까지... 큐가 비워질 때까지
    while q:
        ti, tj = q.pop(0)   # t <- 디큐
        if maze[ti][tj] == '3':  # t 에서 할 일..
            # return 1        # 출구(3)에 도착하면 1 아니면 0리턴
            return visited[ti][tj] - 2      # 입구에서 출구 사이의 빈칸 수 # 출발 도착점은 제외하므로 -2해줌
        # t에 인접 w중, 인큐되지 않은 곳이면
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti + di, tj + dj
            # 미로를 벗어나지 않고, 벽이 아니고, 방문하지 않은 곳이라면
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != '1' and visited[wi][wj] == 0:
                q.append([wi, wj])       # 인큐, 표시
                visited[wi][wj] = visited[ti][tj] + 1
    return 0        # 출구(3)에 도착하면 1 아니면 0리턴

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j


T = int(input())
for tc in range(1,T+1):

    N = int(input())    # 미로의 크기
    maze = [input() for _ in range(N)]

    sti, stj = find_start(N)

    ans = bfs(sti, stj, N)


    print(f'#{tc}')