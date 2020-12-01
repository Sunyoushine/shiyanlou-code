a = range(1,101)
for i in a:
    if a % 7 == 0 or a % 10 == 7 or a // 10 == 7:
        continue
    else:
        print(i)
