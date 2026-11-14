def analyze_text(text):
    total_chars = len(text)
    total_words = len(text.split())

    data = {
        "characters": total_chars,
        "words": total_words
    }
    return data


text_data = ["Python is becoming easier.", "I am learning how functions work.", "I am building real programs."]

file_path = "notes.txt"

with open(file_path, "w") as file:
    for line in text_data:
        file.write(line + "\n")
    print(f"txt file '{file_path}' was created")

with open(file_path, "r") as file:
    contents = file.read()

message = analyze_text(contents)

for key, value in message.items():
    print(f"{key}: {value}")

