def normalize(text):
    new_text =  [w.strip(".,!?;:") for w in text.lower().split()]
    return new_text

def count_word(words):
    return len(words)

def word_frequencies(words):
    dictionary = {}
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1
    return dictionary

def longest_shortest(words):
    if not words:
        return None, None
    return max(words, key=len), min(words, key=len)

def top_words(freq, n = 5):
    return sorted(freq.items(), key = lambda f: f[1], reverse=True)[0:n]

def read_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Введено не число. Введите еще раз: ")

if __name__ == "__main__":
    n = read_int("Сколько слов показать в топе? ")
    words = ["Мама", "мыла", "раму"]
    print(top_words(word_frequencies(words), n))
    