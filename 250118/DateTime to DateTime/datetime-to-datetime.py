from datetime import datetime

# 기준 시간
start_time = datetime(2011, 11, 11, 11, 11)
# 입력된 시간
end_time = datetime(2011, 11, 12, 13, 14)

# 두 시간의 차이를 분 단위로 계산
time_difference = (end_time - start_time).total_seconds() // 60

# 결과 출력
if time_difference < 0:
    print(-1)
else:
    print(int(time_difference))
