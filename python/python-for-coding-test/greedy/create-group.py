n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data)

result = 0 # 총 그룹의 수
count = 0 # "현재" 그룹에 포함 된 모험가의 수

for i in data : # 낮은 공포도부터 하나씩 확인
    count += 1  # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i : # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 그룹 수 출력
