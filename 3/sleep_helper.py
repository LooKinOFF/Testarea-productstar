import time

# Запрашиваем у пользователя количество овец
num_sheep = int(input("Введите количество овец, которые перепрыгнут забор: "))

def sheep_plural(n):
    if n % 10 == 1 and n % 100 != 11:
        return "овца"
    elif n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14]:
        return "овцы"
    else:
        return "овец"

for i in range(1, num_sheep + 1):
    print(f"{i} {sheep_plural(i)} за забором")
    time.sleep(1)  # Пауза в 1 секунду после каждой фразы


print("Все овцы посчитаны!")