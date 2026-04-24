# 첫번째 값 입력 받기
f_num = int(input())
# 두번째 값 입력받기

# count 지정
count = 0
list_kenn = input().split()
# 만약 list_kenn의 값이 1,1,2가 연속된다면 count +1
for index in range(1, f_num + 1):
  
  if list_kenn[index-1:index+2] == ['1','1','2']:
    count += 1
    # 출력
print(count)