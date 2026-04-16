day_list = []
rainfall_list = []

# 연휴 일수, 여행 일수 입력 받기
holiday, trip = map(int, input().split())

# 날짜, 강수 확률 입력 받기
for i in range(holiday):
    day, rainfall = map(int, input().split())
    day_list.append(day)
    rainfall_list.append(rainfall)

# 최소값 초기화
min_sum = float('inf')
start_day = 0

# 연속 구간 탐색
for i in range(holiday - trip + 1):
    total = sum(rainfall_list[i:i+trip])

    if total < min_sum:
        min_sum = total
        start_day = day_list[i]

# 끝나는 날
end_day = day_list[day_list.index(start_day) + trip - 1]

print(start_day, end_day)