
def brureforce(p, t):
    N = len(t)
    M = len(p)
    i = j = 0
    while i < N and j < M:
        if t[i] != p[j]:  # 다르면
            i = i - j + 1  # i - j 비교를 시작했던 위치  # i와 j 의 인덱스 증가율이 동일 하므로..
            j = 0
        else:  # 같으면
            i += 1
            j += 1
    if j == M:
        return i - j  # 패턴의 시작 인덱스
    else:
        return -1


t = 'TTTTTATAATA'
p = 'TTA'

print(brureforce(p, t))

# 패턴의 등장 횟수 리턴
def pattern_count(p,t):
    N = len(t)
    M = len(p)
    i = j = 0
    cnt = 0
    while i < N:
        if t[i] != p[j]:  # 다르면
            i = i - j + 1  # i - j 비교를 시작했던 위치
            j = 0
        else:  # 같으면
            i += 1
            j += 1
        if j == M:  # 패턴을 찾은 경우
            cnt += 1
            i = i - j + 1
            j = 0
    return cnt

                    

