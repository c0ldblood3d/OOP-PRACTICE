class RemovePunctuation:

    def __init__(self, text):
        print("Start RemovePunctuation.__init__")
        self.text = text
        self.clean_text = text.translate(str.maketrans('', '', ',!?;:-.'))
        print("End RemovePunctuation.__init__")

class WordCounter(RemovePunctuation):
    
    def __init__(self, text):
        print("Start WordCounter.__init__")
        super().__init__(text)
        self.word_count = len(self.clean_text.split())
        print("End WordCounter.__init__")

class UniqueWords(RemovePunctuation):

    def __init__(self, text):
        print("Start UniqueWords.__init__")
        super().__init__(text)
        words = self.clean_text.split()
        self.unique_words = set(words)
        print("End UniqueWords.__init__")

class TextCleaner(WordCounter, UniqueWords):

    def __init__(self, text):
        print("Start TextCleaner.__init__")
        super().__init__(text)
        print(f"Очищенный текст: {self.clean_text}")
        print(f"Количество слов: {self.word_count}")
        print(f"Уникальные слова: {self.unique_words}")
        print("End TextCleaner.__init__")
