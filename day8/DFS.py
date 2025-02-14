# DFS 알고리즘

'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(v,N):       # v출발, N마지막 정점
    visited = [0] * (N+1)   # 방문표시
    stack = []              # 스택

    while True:
        if visited[v] == 0:    # 첫 방문이면,,
            visited[v] = 1
            print(v)
        for w in adj_list[v]:   # v에 인접하고 방문 안한 w가 있으면
            if visited[w] == 0:
                stack.append(v)     # 현재 정점 push
                v = w       # w로 이동
                break       # for w
        else:               # 더 이상 갈 곳 이 없는경우 top>-1
            if stack:       # pop
                v = stack.pop()


V, E = map(int, input().split())
graph = list(map(int, input().split()))
adj_list = [[] for _ in range(V+1)]     #인접 리스트

