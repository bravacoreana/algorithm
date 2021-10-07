data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)) : # 두 번째 수부터 시작
    num = int(data[i])

    # 두 수 중 하나라도 0이거나 1인 경우에는 더하기 실행
    if num <= 1 or result <= 1 :
        result += num
    else :
        result *= num

print(result)