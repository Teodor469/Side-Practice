# Text Analyzer
from collections import Counter
import re

class TextAnalyzer:
    def __init__(self, text) -> None:
        self.text = text

    def word_count(self):
        words = len(re.findall(r'\w+', self.text))
        return words
    
    def character_count(self):
        characters = len(re.findall(r'[A-Za-z]', self.text))
        return characters
    
    def most_common_word(self):
        words = self.text.split()
        word_counts = Counter(words)
        most_common = word_counts.most_common(1)
        return most_common[0][0] if most_common else None
    
    def get_words(self, start_index, end_index):
        words = self.text.split()
        return " ".join(words[start_index:end_index+1])

input_text = input("Enter the text for analysis: ")
text_analyzer = TextAnalyzer(input_text)
while True:
    command = input()
    if command == 'Stop':
        break

    if command == 'Word count':
        print(f"Word Count: {text_analyzer.word_count()}")
    elif command == 'Character count':
        print(f"Character Count: {text_analyzer.character_count()}")
    elif command == 'Most common word':
        print(f"Most Common Word: {text_analyzer.most_common_word()}")
    elif command == 'Get words':
        start_index = int(input("Enter start index: "))
        end_index = int(input("Enter end index: "))
        print(f"Words from index {start_index} to {end_index}: {text_analyzer.get_words(start_index, end_index)}")
    else:
        print("Invalid command. Please try again.")