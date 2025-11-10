from Text2 import TextCleaner

text = "Hello, world! Hello, Python!"

cleaner = TextCleaner(text)

print(f"clean_text: {cleaner.clean_text}")
print(f"word_count: {cleaner.word_count}")
print(f"unique_words: {cleaner.unique_words}")