count = int(input())
inputs = input().split()

number = int(inputs[0])

for i in range(1, len(inputs)) :
    if number > int(inputs[i]) :
        number = int(inputs[i])
    

print(number)