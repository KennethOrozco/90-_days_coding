text = input("Enter some text: ")

char_count = len(text)

words = text.split()

word_count = len(words)

match_count = 0

print(char_count)

print(word_count)

search = input("Enter a word to search for: ")

for word in words:
    if search.lower() == word.lower():
        match_count += 1

print(f"{search} appears {match_count} times.")

