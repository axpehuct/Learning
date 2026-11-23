class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."                     # базовая реализация-заглушка

class Dog(Animal):                       # в скобках — родитель
    def speak(self):
        return f"{self.name}: Гав!"

class Cat(Animal):
    def speak(self):
        return f"{self.name}: Мяу!"

class Cow(Animal):
    def speak(self):
        return f"{self.name}: Муу!"

print(Dog("Рекс").speak())   # Рекс: Гав!
print(Cat("Мурзик").speak()) # Мурзик: Мяу!
print(Cow("Борька").speak()) # Борька: Муу!
print(Animal("Животное").speak()) # ...