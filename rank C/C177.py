# 회계 기록의 수를 나타내는 정수 입력 받기
accounting = int(input())
total = 0
count = 0
# 하한값, 승격조건 합계 금액 입력 받기
lower_limit, month_total = map(int,input().split())

# 회계금액 입력 받기
partial_price = input().split()

# 한달 금액 다 더하기
for i in partial_price:
    total += int(i)
    # 하한값 카운팅
    if int(i) >= lower_limit:
        count += 1
# 만약 하한값 이상의 금액을 2번 이상 하고 1개월 금약 합계가 m이상이면 실버
if total >= month_total and count >= 3:
    print("silver")

# 안되면 브론즈
else:
    print("bronze")
