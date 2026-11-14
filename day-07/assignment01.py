def word_statistics(words):
    statistics = {}
    for word in words:
        if word not in statistics:
            statistics[word] = {"count": 1, "length": len(word)}
        else:
            statistics[word]['count'] += 1
    return statistics

def most_common_words(statistics):
    highest = 0
    for word in statistics:
        if statistics[word]['count'] > highest:
            highest = statistics[word]['count']
    return [word for word in statistics if statistics[word]['count'] == highest]

# def most_common_words(statistics):
#     if not statistics:
#         return []

#     highest = max(info["count"] for info in statistics.values())

#     return [
#         word
#         for word in statistics
#         if statistics[word]["count"] == highest
#     ]
words = [
    "python",
    "javascript",
    "python",
    "java",
    "javascript",
    "python",
    "c",
    "java",
    "rust",
    "python"
]

statistics = word_statistics(words)

print(most_common_words(statistics))

