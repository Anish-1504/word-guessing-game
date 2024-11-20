import random 

name = input("What's your Name...?\n  ")

print("Good Luck !!! ",name)

words = ['rainbow', 'computer', 'science', 'programming', 
         'python', 'maths', 'player', 'condition', 
         'water', 'board' ]

# print(words)

word = random.choice(words)

print("Guess the characters")

guesses = ''
turns = 12

while turns > 0 :
    
    failed = 0 
    
    for char in word :
        
        if char in guesses :
            print(char, end=" ")
        else:
            print("_")
            failed += 1
    
    if failed == 0:
        print("You Won..!")
        print("The word is ",word)
        break
        
    print()
    guess = input("Enter the character : ")
    guesses += guess

    if guess not in word:
        
        turns -= 1
        print("Wrong")
        print(f"You have {turns} more guesses to go....")
        
        if turns == 0 :
            print("You Lost the Game :( .... Better luck Next time")
        