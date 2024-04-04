number = int(input('Введите число: '))
x = 1
print(x)
while True:
    x = x*2
    if x > number:
        break
    print(x, end='\n')