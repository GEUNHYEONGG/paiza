# 경우의 수 지정
count = 0
# 입력 받기
num1, num2 = map(int, input().split())

# 1부터 첫번째 입력값 까지 반복문
for m in range(1, num1):
    # 첫번째 입력값부터 두번째 입력값 반복
    for n in range(1, num2):

    # 첫번째값 제곱 + 두번째값 제곱 = 로그 정수가 딱 덜어지면 경우의수 1 추가
        value = ((m * m) + (n * n)) ** 0.5
        if (value * 10) % 10 == 0:
            count += 1
print(count)