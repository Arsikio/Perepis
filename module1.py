#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ars
#
# Created:     23.01.2024
# Copyright:   (c) Ars 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
x = 0
with open('111.txt', 'r') as f:
    for i in f:
        familii= i.split()[0]
        print(familii)
        datd= i.split('.')[2]
        if datd < '1978':
            x+=1
    print('Число родившихся раньше 1978 года:',x)
f.close()

print()
min_year = int(input("Введите минимальный год рождения: "))
max_year = int(input("Введите максимальный год рождения: "))
print('В заданом диапазоне родились:')
with open('111.txt', 'r') as f:
    for line in f:
        a, b, c, year =line.split()[0],line.split()[1],line.split()[2],  int(line.split('.')[2])
        if min_year <= year <= max_year:
            print(a,b,c,year)