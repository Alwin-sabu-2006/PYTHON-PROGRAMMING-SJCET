P1=input("Enter the name of first player")
P2=input("Enter the name of second player")
num=16
player=" "
while True:
    if num!=0:
        c=int(input("Enter choice of :"))
        num=num-c
        player=P1
    if num!=0:
        d=int(input("Enter  choice of:"))
        num=num-d
        player=P2
    if num==0:
        print(player,'loses the game')
        break

