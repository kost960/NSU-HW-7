number = int(input('Введите объем кубика: '))
v = 0
cube = 0
while True:
    cube += 1
    v = cube ** 3
    if v > number:
        break
    print(v, end=' ')