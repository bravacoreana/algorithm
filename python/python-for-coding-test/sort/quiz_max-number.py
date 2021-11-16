# a = [1,2,5,4,3]
# b = [5,5,6,6,5]

# def max_number(n, k):
#     a.sort()
#     b.sort(reverse=True)
#     for i in range(k):
#         if a[i] < b[i]:
#             a[i], b[i] = b[i], a[i]
#     print(sum(a))

# max_number(5,3)


## 풀이

n, k = map(int, input().split) # n, k 입력받기
a = list(map(int, input().split())) # 배열 a의 원소 입력받기
b = list(map(int, input().split())) # 배열 b의 원소 입력받기

a.sort() # 배열 a는 오름차순 정렬 수행
b.sort(reverse=True) # 배열 b는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며 두 배열의 원소를 최대 k 번 비교
for i in range(k):
    # a의 원소가 b의 원소보다 작은 경우
    if a[i]<b[i]:
        # 두 원소를 교체
        a[i],b[i] = b[i],a[i]
    else: # a의 원소가 b의 원소보다 크거나 같을 때 반복문을 탈출
        break

print(sum(a)) # 배열 a의 모든 원소의 합을 출력