a,b,c = map(int, input().split())

i = 1 
while i % a != 0 or i % b != 0 or i % c != 0 :
    i+=1
print(i)
