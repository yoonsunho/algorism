import sys
sys.stdin = open("txt/1952.txt", "r")

# dp을 하는 버전
T = int((input()))

for tc in range(1, T+1):
    
    # 이용건 가격들(1일,1달,3달,1년)
    cost_day, cost_month,cost_month3, cost_year = map(int, input().split())

    # 12개월 이용 계획
    days = [0] + list(map(int, input().split()))

    dp = [0] * 13
    # 시작점 초기화(1,2월)
    # 1월의 가격(1일권 구매 vs 1달권 구매)
    dp[1] = min(days[1] * cost_day,cost_month)
    # 2울의 가격= 1월 가격 + (1일권 구매 vs 1달권 구매)
    dp[2] = dp[1] + min(days[2]* cost_day,cost_month)
    
    # 3월 ~ 12월은 반복하면서 계산
    for month in range(3,13):
        # N월의 최소 비용 후보
        # 1. (N-3)월에 3개월 이용권 구입한 경우
        # 2. (N-1)월의 최소 비용 + 1일권 구매
        # 3. (N-1)월의 최소 비용  + 1달권 구매
        dp[month] = min(
            dp[month-3]+ cost_month3,
            dp[month-1] + (days[month] * cost_day),
            dp[month-1] + cost_month
        )

    # 12월의 누적 최소 금액 vs 1년권
    answer = min(dp[12], cost_year)

    print(f'#{tc} {answer}')

    