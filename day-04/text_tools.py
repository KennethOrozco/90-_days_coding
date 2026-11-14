def count_words(text):
   return len(text.split())


def count_characters(text):
    return len(text)


def average_word_length(text):
    words = text.split()
    if words:
        sum_ = sum(count_characters(word) for word in words)
        return sum_/count_words(text)
    else:
        return 0