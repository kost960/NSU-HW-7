past_temp = 0
decrease = 0
while True:
    temp = float(input('Введите число: '))
    if temp == 0:
        print(decrease)
        break
    elif temp < past_temp:
        decrease += 1
    past_temp = temp
