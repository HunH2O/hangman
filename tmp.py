x_str = '2001'
ii = []


for i in range(10, 100):
    n1 = str(i) + x_str
    n2 = x_str + str(i)
    if int(n1) % i == 0:
        if int(n2) % i ==0:
            ii.append(i)


print(len(ii))
print(ii)
