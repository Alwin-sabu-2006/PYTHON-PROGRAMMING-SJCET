print("Welcome to the Game of sticks!!!!")
player_1 = input("Enter the name of player 1:")
player_2 = input("Enter the name of player 2:")
l=[1,2,3]
stick =16

while True:

    if stick != 0:
        print(stick)
        choice = int(input(f"{player_1} Enter a Number from (1,2,3)"))
        if choice not in l:
              print("Invalid Entry")
              break
        else:
            stick = stick- choice
            player = player_1


   
    if stick != 0:
        print(stick)
        choice = int(input(f"{player_2} Enter a Number from (1,2,3)"))
        if choice not in l:
                print("Invalid Entry")
                break
        else:
            stick = stick- choice
            player = player_1





    if stick == 0:
        print(f"{player} has lost the game")
        break




