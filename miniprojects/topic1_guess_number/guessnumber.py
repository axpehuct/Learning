import random
import json

def save_stats(filename, stats):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

        

def load_stats(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Файл не найден")
        return {}

filename = "stats.json"

stats = {}


while True:
    secret = random.randint(1, 100)
    tryCount = 0
    name = input("Введите ваше имя: ")
    if stats.get(name) == None:
        stats[name] = 0
    while True:
        number = int(input("Введите число: "))
        tryCount += 1
        if number < secret:
            print("Загаданное число больше")
        elif number > secret:
            print("Загаданное число меньше")
        else: 
            print(f"Вы угадали c {tryCount} попытки")
            break
    if  stats.get(name) == 0 or stats.get(name) > tryCount:
        stats[name] = tryCount

    again = input("Сыграть еще? (да/нет): ")
    if again != "да":
        save_stats(filename, stats)
        break
    


print("Статистика игроков:")
# for name, count in stats.items():
#     print(f"{name} попыток {count}")
print(load_stats(filename))