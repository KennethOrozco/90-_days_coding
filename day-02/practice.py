def count_long_words(words):
    index = 0
    for word in words:
        if word.count() > 5:
            index += 1
    return index
