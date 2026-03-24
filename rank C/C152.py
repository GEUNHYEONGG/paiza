rainbow = []
# 예보가 주어지는 일수 입력받기
weather_cast = int(input())

# 0맑음 1흐림 2비 입력 받은 수를 리스트로 만들기
weather = list(map(int, input().split()))

# 전날이 비가 오면 당일은 맑은날에 무지개를 볼 수 있음
# 만약 전날이 비가오면(2)..
for i in range(weather_cast-1):

    # 만약 비가 오고나서 해가 뜨면(0) 그 날짜는 !무지개!
    if weather[i] == 2:
        if weather[i + 1] == 0:
            
            rainbow.append(i + 1)


# 무지개가 뜨는 날이 없으면 "-1" 출력
if not rainbow:
    print(-1)
else:
    print(*rainbow)
