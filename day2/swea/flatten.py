import sys
sys.stdin = open("flatten.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    # 강사님 풀이
    dump = int(input())
    box_heights = list(map(int, input().split()))

    for _ in range(dump):   # 이 for문은 반복문에 불과하기 때문에 _ 사용
        max_box_height = max(box_heights)   # .max() 시간복잡도: O(n)
        min_box_height = min(box_heights)
        
        # 평탄화 높이 차이가 1 이하라면 굳이 평탄화를 할 필요가 없음
        if max_box_height - min_box_height <=1:
            break

        #index라는 내장함수 안쓸 순 없을까? .index() 시간 복잡도:O(n)이기 때문..
        max_idx = box_heights.index(max_box_height)
        min_idx = box_heights.index(min_box_height)

        box_heights[max_idx] -= 1
        box_heights[min_idx] += 1

    # 평탄화가 끝나고 나서도, 또 최대 높이의 상자와 최소 높이의 상자가 바뀌었을 수도 있다.
    print(f'{test_case} {max(box_heights)-min(box_heights)}')


    # dump = int(input())
    # box_height = list(map(int, input().split()))
    #
    # min_dif = 100
    # max_hei = box_height[0]
    # min_hei = box_height[0]
    # for i in range(dump):