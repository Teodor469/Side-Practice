sentence = input()

words = sentence.split()

reversed_words = []

for word in reversed(words):
    reversed_words.append(word)

reversed_sentences = " " .join(reversed_words)

print(reversed_sentences)