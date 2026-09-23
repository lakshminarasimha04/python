word = "apple"
words = ['_','_','_','_','_']
lives=0
leng=len(word)
print("Lets play Hangman!!")
print("You have only 6 lives so try to guess the word within 6 attempts! Good luck!")
print(words)
hangman = [
"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
"""
]
while lives<6:
    Guess= input()
    if Guess in word:
        print(lives)
        
        for i in range(leng):
            if word[i] == Guess:
                words[i]=Guess
                
                if "_" not in words:
                    print(lives)
                    print("you Win!")
                    break
    else:
        lives +=1
        print("You guessed", Guess, "that is not present in the word.")
        print("So you loss a life")
        print(hangman[lives - 1])                
