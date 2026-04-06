# 숫자 담을 값들
max_num = 0
min_num = 100
# 사용자에게 단어 갯수 받기
num = int(input())

# 입력값 넣기
word_list = input().split()

# for문으로 하나씩 돌리며 글자수 갯수 새기, 이전 값보다 작거나 크면 추가
for i in range(num):
  update = int(len(word_list[i]))


# 값 넣기, 제일 큰 수, 작은 수 최신화 해주기
  if update > max_num:
      max_num = update

  if update < min_num:
      min_num = update



# 제일 큰 수 - 작은 수 값 출력
print(max_num - min_num)
