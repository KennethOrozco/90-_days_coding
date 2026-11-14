def analyze_words(words):
    total_words = len(words)
    unique_words = len(set(words))
    longest = words[0]
    shortest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

        if len(word) < len(shortest):
            shortest = word


    analysis = { "total": total_words,
                  "unique": unique_words,
                  "long": longest,
                  "short": shortest
                  }
    return analysis

list_of_words = ["apple", "banana", "cat", "elephant", "apple"]

dictionary = analyze_words(list_of_words)

items = dictionary.items()

for key, value in items:
    print(f"{key}: {value}")
