from text_utils import normalize, count_word, word_frequencies, longest_shortest, top_words

input_text = "Мама мыла раму и мама поливала цветы!"
normalized_input = normalize(input_text)
print(f"Список чистых слов: {normalized_input}")
print(f"Количество слов в тексте: {count_word(normalized_input)}")
print(f"Частота встречаемых слов: {word_frequencies(normalized_input)}")
print(f"Самое длинное и самое короткое слово: {longest_shortest(normalized_input)}")
print(f"Топ самых частых слов: {top_words(word_frequencies(normalized_input), 2)}")