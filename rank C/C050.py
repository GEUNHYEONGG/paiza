# 사용자로부터 물건 가격, A자금, B자금 입력 받기
price, a_funds, b_funds = map(int, input().split())
winner = ""
while True:

# 자금을 초과하지 않는지 비교
# A가 먼저 올린거니 A 먼저 비교
  if price + 10 > a_funds:
    # 초과한다면 승자 지정
    winner += "B"
    break
  price += 10

# B가 버틸수 있는지 체크
  if price + 1000 > b_funds:
    # 초과한다면 승자 지정
    winner += "A"
    break
  price += 1000

# 출력
print(winner, price)