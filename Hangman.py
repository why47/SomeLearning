import random
import string
from Word import Kata

def mengambil_kata_valid(Kata):
    kataKata = random.choice(Kata) # randomly chooses something form the list
    while '-' in kataKata or ' ' in kataKata:
        kataKata = random.choice(Kata)
   
    return kataKata

def hangman():
    kataKata = mengambil_kata_valid(Kata)
    kata_abjad = set(kataKata) # abjad di kata
    alphabet = set(string.ascii_uppercase)
    abjad_Tergunakan = set() # kata player yang telah di gunakan

    lives = 7

    # User input
    while len(kata_abjad) > 0 and lives > 0:
        print(f"you have {lives} lives left and you have used these letters:")
    
        kataList = [letter if letter in abjad_Tergunakan else '-' for letter in Kata]
        print("Kata Sebelumnya: ")
   
        abjadUser = input("Guess a Letter : ").upper()
        if abjadUser in alphabet  - abjad_Tergunakan:
            abjad_Tergunakan.add(abjadUser)
            if abjadUser in kata_abjad:
               kata_abjad.remove(abjadUser)

            else:
                lives = lives - 1
                print("\nYour Letter,", abjadUser, 'is not in the word. ')        

        elif abjadUser in abjad_Tergunakan:
             print("You have already used that character. please try again. ")

        else:
            print('invalid character, please try again.')    

    if lives == 0:
        print(f"you died, sorry , the word was {kataKata}")
    else:
        print('YAY! you guessed the word, word, !!')     

hangman()