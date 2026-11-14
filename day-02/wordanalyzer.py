def  analyze_words(words):
    longest_word = words[0]
    shortest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

        if len(word) < len(shortest_word):
            shortest_word = word
  
    return longest_word, shortest_word

while True:
    user_input = input("Please enter at least two words: ")

    user_words = user_input.split()


  
    if len(user_words) >= 2:
        longest, shortest = analyze_words(user_words)
        print(f"Longest word: {longest}")
        print(f"Shortest word: {shortest}")
        break
    else:
        print("Error: You must enter more than one word. Try again.")

      

