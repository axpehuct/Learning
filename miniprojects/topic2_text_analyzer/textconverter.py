def normalize(text):
    newText =  [w.strip(".,!?;:") for w in text.lower().split()]
    return newText

def count_word(words):
    return len(words)

def word_frequinceies(words):
    dictionary = {}
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1
    return dictionary

def longest_shortest(words):
    sorted_words = sorted(words, key = lambda w: len(w))
    longest, shortest = sorted_words[-1], sorted_words[0]
    return longest, shortest

def top_words(freq, n = 5):
    try:
        return sorted(freq.items(), key = lambda f: f[1], reverse=True)[0:n]
    except ValueError:
        print("Неправильно введено количество слов в топе.")
    


input_text = "Мама мыла раму и мама поливала цветы!"
print(f"Список чистых слов: {normalize(input_text)}")
print(f"Количество слов в тексте: {count_word(input_text)}")
print(f"Частота встречаемых слов: {word_frequinceies(normalize(input_text))}")
print(f"Самое длинное и самое короткое слово: {longest_shortest(normalize(input_text))}")
print(f"Топ самых частых слов: {top_words(word_frequinceies(normalize(input_text)), 2)}")
