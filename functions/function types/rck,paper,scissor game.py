#makking a rock paper scissor game\
    
import random

while True:
    user_choice=input("please enter: rock,paper or scissor:")
    possible_choice=["rock","scissor","paper"]
    computer_choice=random.choice(possible_choice)
    
    print("your choice is :",user_choice)
    print("computer choice is:",computer_choice)
    
    if user_choice==computer_choice:
        print("the game has resulted in a tie")
        
    elif user_choice=="rock":
        if computer_choice=="paper":
            print("yo have lost the game")
        else:
            print("you win the game")
            
    elif user_choice=="scissor":
        if computer_choice=="paper":
            print("you have the game")
        else:
            
            
            print("you have lost the game")
    elif user_choice=="paper":
        if computer_choice=="scissor":
            print("you have won the game")
        else:
            print("you have lost the game")
            
    play_again=input("do you want to play the game again?yes/no:")
    if play_again.lower=="no":
        break
    
    