def analyze_word(word):
    Word = f"Word: {word}"
    Length = f"Length: {len(word)}"
    Long = len(word) > 5
    a_in_word = 'a' in word.lower()
    match_count = 0

    for letter in word.lower():
        if letter == 'a':
         match_count += 1
    amount_a = f"Number of a's: {match_count}"

    return Word, Length, Long, a_in_word, amount_a

User_word = input("Type a word: ")

message = analyze_word(User_word)

for section in message:
    print(section)




