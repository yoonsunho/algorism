def binary_search(target):
    left = 0
    right = len(arr) - 1
    cnt = 0

    while left <= right:
        mid = (left + right) // 2
        cnt += 1        # 검색 횟수 추가
        
        if arr[mid] == target:
            return mid, cnt  # mid index에서 검색 완료~!

        # 왼쪽에 정답이 있다.
        if target < arr[mid]:
            right = mid - 1
        else:  # 오른쪽에 정답이 있다
            left = mid + 1

    return -1, cnt  # target 찾지 못함

def binary_search_recur(left, right,target):
    # left, right 를 작업 영역으로 검색
    # left <= right 만족하면 반복
    if left > right:
        return -1

    mid = (left + right)//2
    # 검색하면 종료
    if target == arr[mid]:
        return mid

    # 한 번 할 때마다 left 와 right 를 mid 기준으로 이동시켜 주면서 진행
    # 왼쪽을 봐야한다
    if target < arr[mid]:
        return binary_search_recur(left,mid-1,target)
    else:
        return binary_search_recur(mid+1,right,target)


arr = [4,2,9,7,11,23,19]

# 이진 검색은 항상 정렬된 데이터에서 적용해야 한다!!!
arr.sort()
# print(arr)  # [2, 4, 7, 9, 11, 19, 23]

print(f'9-{binary_search(9)}')
print(f'2-{binary_search(2)}')
print(f'20-{binary_search(20)}')

print(f'9 - {binary_search_recur(0, len(arr) - 1, 9)}')
print(f'2 - {binary_search_recur(0, len(arr) - 1, 2)}')
print(f'20 - {binary_search_recur(0, len(arr) - 1, 20)}')


