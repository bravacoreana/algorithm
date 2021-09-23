a,m,d,n = map(int, input().split())


value = a 
for i in range(0, n-1) :
    value = value * m + d
print(value)


# def myFunc(n) :
#     return len(n)
# x = map(myFunc, ('apple', 'banana', 'cherry'))