# 이긴 횟수 변수 만들기
win = 0

# 처음 행하여지는 가위바위보 수 입력받기
for i in range(int(input())):

# 반복문으로 가위바위보 입력받기
    girl, man = input().split()

# 이겼을때
    if girl == "G":
        if man == "C":
            win += 1

    if girl == "C":
        if man == "P":
            win += 1

    if girl == "P":
        if man == "G":
            win += 1

print(win)


# win = 0

# # 누가 누구를 이기는지 정의
# win_case = {
#     "G": "C",  # 바위 > 가위
#     "C": "P",  # 가위 > 보
#     "P": "G"   # 보 > 바위
# }

# for _ in range(int(input())):
#     girl, man = input().split()
    
#     if win_case[girl] == man:
#         win += 1

# print(win)