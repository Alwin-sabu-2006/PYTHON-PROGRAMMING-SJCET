import random
game=['Rock','Paper','Scissor']
while True:
    print(" Rock \n Paper \n Scissor \n Do you want to continue Yes or No")
    guess=input("Enter your choice:")
    random_check=random.choice(game)
    guess=guess.upper()
    if random_check=="Rock" and guess=="Rock":
        print("TIE!")
    elif random_check=="Rock" and guess=="Paper":
        print("You won!")
    elif random_check=="Paper" and guess=="Scissor":
        print("YOU won!")
    elif random_check=="Scissor" and guess=="Paper":
        print("Computer Wins")
    elif random_check=="Scissor" and guess=="Scissor":
        print("TIE!")
    elif random_check=="Paper" and guess=="Rock":
        print("Computer wins!")
    elif random_check=="Paper" and guess=="Paper":
        print("TIE!")
    elif  random_check=="Scissor" and guess=="Rock":
        print("You Win !")
    elif  random_check=="Rock" and guess=="Paper":
        print("Computer Wins!")
    elif guess=="Yes":
        break
    elif guess not in game:
        print("Invalid Entry")
        continue
    else:
        print("You lose")
        
        


    
