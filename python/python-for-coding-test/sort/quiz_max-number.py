# a = [1,2,5,4,3]
# b = [5,5,6,6,5]

# def max_number(n, k):
#     a.sort()
#     b.sort(reverse=True)
#     for i in range(k):
#         if a[i] < b[i]:
#             a[i], b[i] = b[i], a[i]
#     print(a,b)

# max_number(5,3)


## 풀이

n, k = map(int, input().split) # n, k 입력받기
a = list(map(int, input().split())) # 배열 a의 원소 입력받기
b = list(map(int, input().split())) # 배열 b의 원소 입력받기

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break

print(sum(a))