import random
while True :
    c=random.randint(1,3)
    if c==1:
        c="paper"
    elif c==2:
        c="scissors"
    elif c==3:
        c="rock"
    print("rock  paper  scissors")
    u=input("baraye bazi entekhab konid va agar ghasde khoroj ra darid benevesid (exit)     :")
    if u=="exit":
        break
    else:
        if u==c :
            print("mosavi shod")
        elif u=="rock" and c=="scissors":
            print("bordi")
        elif u=="rock" and c=="paper":
            print("bakhti")
        elif u=="paper" and c=="scissors":
            print("bakhti")
        elif u=="paper" and c=="rock":
            print("bordi")
        elif u=="scissors" and c=="paper":
            print("bordi")
        elif u=="scissors" and c=="rock":
            print("bakhti")
    print( )