# 전투횟수, 최초 레벨 입력받기
fight, my_level = map(int, input().split())

# 횟수는 반복문으로
for i in range(fight):
    enemy_level = int(input())
    
    # 만약 상대보다 레벨이 높으면 상대의 레벨 /2 획득
    if my_level > enemy_level:    
        my_level += enemy_level // 2
    
    elif my_level == enemy_level:
        pass
    # 상대보다 레벨이 낮으면  현재 레벨의 /2
    else:
        my_level = my_level // 2

# 현재 나의 레벨 출력
print(my_level)