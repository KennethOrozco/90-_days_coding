text = input("Enter some text: ") 
char_count = len(text) 

x = text.split() 
word_count = len(x) 

index = 0 
match_count = 0 

print(f"Characters: {char_count}") 
print(f"Total words: {word_count}") 

# Make sure you press ENTER after typing this next word
search = input("Enter a word to search for: ") 

while True: 
    if index >= len(x): 
        break 
        
    word = x[index] 
    
    if word == search: 
        match_count += 1 
        
    # Crucial: This must line up perfectly with 'word = x[index]'
    index += 1 

print(f"'{search}' appears {match_count} times.")
