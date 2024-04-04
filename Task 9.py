number = input('Введите число: ')
n = int(number.split()[0])
k = 1 + int(number.split()[1])/100
r = int(number.split()[2])
day = 1
while True:
    n *= k
    day += 1
    if n >= r:
        print(day)
        break