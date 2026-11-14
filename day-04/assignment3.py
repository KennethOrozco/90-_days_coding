words = ["python","code", "python", "ai","programming","code"]

word_lengths = {len(word) for word in words}

print(word_lengths)

word_data = {word:len(word) for word in words}

print (word_data)

long_words = {word:len(word) for word in words if len(word) > 4}

print(long_words)