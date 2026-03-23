# 왼 오 무게 저장
l_weight = 0
r_weight = 0
# 반복할 횟수 인풋
roof = int(input())
# 인풋 받은 값으로 반복
for i in range(roof):
    # 왼 중 오입력 받기
    left, middle, light = input().split()

    # 숫자형으로 바꿔주기
    num_light = int(light)

    # middle이 left면
    if middle == "L":
        # 입력받은 값이 1, 2, 3에 따른 계산
        if left == "1":
            l_weight += num_light

        # 2이면 -무게
        elif left == "2":
            l_weight -= num_light

        # 3이면 무게 옳기기
        else:
            l_weight -= num_light
            r_weight += num_light

    # middle이 light면
    else :

        # 입력받은 값이 1, 2, 3에 따른 계산
        if left == "1":
            r_weight += num_light

        # 2이면 -무게
        elif left == "2":
            r_weight -= num_light

        # 3이면 무게 옳기기
        else:
            r_weight -= num_light
            l_weight += num_light


        # 더 무거운 쪽 출력
    if l_weight > r_weight:
        print(">")
    elif l_weight < r_weight:
        print("<")
    else:
        print("=")