def normalize(text):
    return [word.strip(",.!?;:") for word in text.lower().split()]

print(normalize(" Привет, Мир! Как дела? "))
