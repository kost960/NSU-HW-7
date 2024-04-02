while True:
    number = int(input())
    if number ** 0.5 % 1 == 0:
        print('Число является полным квадратом')
        break
    print('Число не является полным квадратом')