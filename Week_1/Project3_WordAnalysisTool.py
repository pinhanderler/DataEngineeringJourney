# Project 3: Word Analysis Tool 

sentence = input("Enter a sentence: ")

words = sentence.split()
char_count = len(sentence.replace(" ", ""))
word_count = len(words)
unique_words = set(words)

longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("\nCharacter count (no spaces):", char_count)
print("Word count:", word_count)
print("Unique words:", unique_words)
print("Longest word:", longest_word)
