#guessing game
import random
play=True
choice=str(random.randint(20,30))
print(" the computer has chosen arandom number between 20 to 30,please guess it to win the game")

while play:
    guess_1=input("please enter your number you guessed")
    if guess_1==choice:
        print("you o\have guessed it right,hurray!")
        break
    else:
        print("wrong guess try again")

        
    
   