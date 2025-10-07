from collections import Counter
import string

print("Advanced Word Analysis Tool")

sentence = input("Enter a sentence: ").strip()

# Clean and normalize
for p in string.punctuation:
    sentence = sentence.replace(p, "")
words = sentence.lower().split()

# Analyses
char_count = len(sentence.replace(" ", ""))
word_count = len(words)
unique_words = set(words)
longest_word = max(words, key=len)
word_frequency = Counter(words)
most_common_word, freq = word_frequency.most_common(1)[0]

# Output
print("\n--- Text Summary ---")
print(f"Total characters (no spaces): {char_count}")
print(f"Total words: {word_count}")
print(f"Unique words: {len(unique_words)} → {sorted(unique_words)}")
print(f"Longest word: '{longest_word}'")
print(f"Most frequent word: '{most_common_word}' ({freq} times)")
print("\nWords sorted by length:")
for w in sorted(unique_words, key=len):
    print(f"  {w} ({len(w)} letters)")
