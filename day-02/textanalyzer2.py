def count_a(text):

    match_count = 0

    for letter in text:
        if letter == 'a':
            match_count += 1

    return match_count

def count_words(text):
    amount_of_words = len(text.split())
    return amount_of_words


def analyze_text(text):

    Number_of_chars = f"Characters: {len(text)}"
    Number_of_words = f"Words: {count_words(text)}"
    Number_of_a = f"Number of a's: {count_a(text)}"

    if "Python".lower() in text.lower():
        answer = f"Contains Python: True"
    else:
        answer = f"Contains Python: False"

    return Number_of_chars, Number_of_words, Number_of_a, answer

User_text = input("Type some text here: ")

message = analyze_text(User_text)

for section in message:
    print(section)