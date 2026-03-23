# 사용자에게 입력받기 3개의 변수 지정
people, a, b = map(int, input().split())

# 사람 수가 끝날때까지 반복
for man_num in range(1, people+1):

# 두 수의 배수면 AB 출력
    if 0 == man_num % a and 0 == man_num % b:
        print("AB")
 
# a의 배수면 A 출력
    elif  0 == man_num % a:
        print("A")

# b의 배수면 B 출력
    elif  0 == man_num % b:
        print("B")

# 만약 해당되는게 없으면 N 출력
    else:
        print("N")