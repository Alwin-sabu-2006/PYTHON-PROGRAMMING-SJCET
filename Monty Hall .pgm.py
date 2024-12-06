'''
Author=Alwin Sabu
Description=Monty Hall problem
Date:6/12/24
'''


print("--------Welcome to Monty Hall Problem--------")
print("Choose Any of The Three Doors,If you can find the car then You'll win or else Loss")
print("All the Best")
door_1="Goat"
door_2="Goat"
door_3="Car"
choice=int(input("Host : Enter the door number--"))
while True:
    if choice== 1:
        print("Host : Do you Want to choose door 2?")
        c=input("Enter Y or N:")
        if c=='Y':
            print("Host:You lose,A goat is behind door 2")
            break
        else:
            print(" Host: You lose,A goat is behind door 1")
            break
    if   choice== 2:
        print("Host : Do you Want to choose  door 3?")
        d=input("Enter Y or N:")
        if d=='Y':
            print("Host : You Won, A car is Behind door 3")
            break
        else:
            print("Host : You lose, A goat is behind door 2")
            break
    if choice== 3:
        print("Host : Do you Want to choose door 1?")
        e=input("Enter Y or N")
        if e=='Y':
            print("Host:You lose,A goat is behind door 1")
            break
        else:
            print("Host: You won,A car is behind door 3 ")
            break
        

        
    
