import random 
name = input("What is your name? ") 

print("Good Luck ! ", name) 
  
words = ['rainbow', 'computer', 'science', 'programming']
word = random.choice(words) 
print("Guess the characters") 
guesses = '' 
turns = 4
while turns > 0: -
    failed=0
    for char in word:  
        if char in guesses:  
            print(char) 
        else:  
            print("_")
            failed += 1
    if failed == 0: 
        print("You Win")  
        print("The word is: ", word)  
        break
    guess = input("guess a character:") .
