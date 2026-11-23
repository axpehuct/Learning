import numpy as np

def start(count):
    print(f"Кол-во бросков: {count}")
    rolls = np.random.randint(1, 7, size=count)
    counter = []
    for number in range(1, 7):
        counter.append(np.sum(rolls == number))
    for number in range(1, 7):
        print(f"Количество выпавших {number}: {counter[number - 1]}")
    print(f"Минимум значение: {np.min(rolls)}")
    print(f"Максимальное значение: {np.max(rolls)}")
    print(f"Среднее значение: {np.mean(rolls)}")
    print(f"Доля шестерок: {counter[5] / count}")


if __name__ == "__main__":
    start(10000)
    start(100)
    try:
        print(np.array([1,2,3]) + np.array([10,20])) #Ошибка ValueError: operands could not be broadcast together with shapes (3,) (2,) 
    except ValueError as e:
        print(e)