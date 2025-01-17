import bisect

# 입력
n = int(input())
arr = list(map(int, input().split()))

def median(n, arr):
    current_numbers = []  # 중앙값 계산용 리스트

    for i in range(n):
        # 현재 숫자를 정렬된 상태로 삽입
        bisect.insort(current_numbers, arr[i])

        # 홀수 번째 원소 처리
        if (i + 1) % 2 != 0:
            # 중앙값 계산
            med = current_numbers[(i + 1) // 2 ]
            print(med, end=' ')

median(n, arr)

'''
홀수일 때 읽을 때 마다 지금 까지 입력받은 값중 중앙 값을 차례대로 공백을 사이에 두고 출력 

1. 홀수일 때 읽을때 마다
for 문으로 리스트를 0에서 str의 길이 만큼 탐색했을떄
홀수 인덱스일때 값을 가져와야한다.

2. 중앙값 공식
중앙값=str[현재 탐색 한 홀수 인덱스+1//2]

3. 공백을 사이에 두고 출력 
print(중앙값,end=' ')

# 함수 호출
median(n, arr)

# 입력
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

def median(n, arr):
    for i in range(n):
        if (i + 1) % 2 != 0:
            med = arr[(i + 1) // 2 ]
            print(med, end=' ')


median(n, arr)
'''

