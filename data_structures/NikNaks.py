# Program that allows a person to play a game of Niknaks against the computer. 
# Name: Natasha Mazibuko
# Date: 04 August 2024

import random

def main():
    print("Guess the mystery 4 letter code. (No letter occurs more than once.)") 
    difficulty = int(input("Choose difficulty level (4 to 26):\n"))
    
    if 4 <= difficulty <= 26:
        letters = list("abcdefghijklmnopqrstuvwxyz")[0: difficulty]
        print("The letters in the code are chosen from: {}.".format(letters))
        
        secret_code = []
        for i in range(4): 
            rand_index = random.randint(0, len(letters)-1) 
            letter = letters.pop(rand_index) 
            secret_code.append(letter) 
            
        attempts = 10
        print("You have {} guesses remaining.".format(attempts))
        
        while attempts > 0:
            guess = input("Enter your guess:\n").strip().lower()
            
            if len(guess) != 4:
                continue
            
            if len(set(guess)) == 4:
                unique_letter = []
                
                for letter in guess:
                    if letter not in unique_letter:
                        unique_letter.append(letter)
                        
                if len(unique_letter) == 4:
                    allowed_letters = "abcdefghijklmnopqrstuvwxyz"[:difficulty]
                    
                    for letters in guess:
                        if letter not in allowed_letters:
                            continue
                        
            nik = 0
            naks = 0
            
            for i in range(4):
                if guess[i] == secret_code[i]:
                    nik += 1
                    
            for i in range(4):
                if guess[i] in secret_code and guess[i] != secret_code[i]:
                    naks += 1
                    
            if nik == 4:
                print("Correct!")
                break
                
            else:
                if nik == 1 and naks == 1:
                    print("There is" , nik , "Niks and", naks , "Naks.")
                elif nik == 1:
                    print("There is" , nik , "Nik and", naks , "Naks.")
                elif naks == 1:
                    print("There are" , nik , "Niks and", naks , "Nak.")
                else:
                    print("There are", nik , "Niks and", naks, "Naks.")
                    
                attempts -= 1
                if attempts > 0:
                    print("You have {} guesses remaining.".format(attempts))
                
        if nik != 4:
            print("Sorry, you lose.\nThe secret number was {}.".format("".join(secret_code)))
                
if __name__ == '__main__':   
    main()