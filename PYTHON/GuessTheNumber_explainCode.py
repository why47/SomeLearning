# Tebak kata
# Guest the number game is where the player think of a number 
# between a certain range and the other player ties to guess the number 
import random # import acak values
def guess(x):
    random_number = random.randint(0,x) # acak angka dari 0 dan guess
    guess = 0 # mengasih values ke guess 
    while guess != random_number:
         guess = int(input(f"Guess number between 1 and {x}: "))
         if guess < random_number: # kurang dari random number
              print("sorry, guess again, TooLow.")
         elif guess>random_number: # lebih dari random number
              print("sorry, guess again, Too High,")

    print(f"yay, congrats. you gave guess the number {random_number}")           

##lguess(10)

def computer_guess(x):
     low = 1
     high = x
     feedback =''
     while feedback != 'c':
          if low != high:
               guess = random.randint(low,high)
          else:
               guess = low     
         
          guess = random.randint(low,high)
          feedback= input(f'Is {guess} too high (H), to low (L), or correct (C)?? ').lower() # player give advice to computer is high or low and correct
          
          if feedback == 'h':
               high = guess - 1
          elif feedback == 'l':
               low = guess + 1

     print(f"yay! The Computer guessed your number, {guess}, correctly")

computer_guess(10) # meentukan banyakn nya values di guess