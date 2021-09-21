input = input()
hex = int(input, 16)

for i in range(1, 16) :
    value = hex * i
    print("%s*%X=%X" %(input, i, value))


# %s : string
# %d : integer
# %f : float
# %o : octal
# %x : hexadecimal

# print('%s%%' % 100)  # 100%
# print('%%') # %%