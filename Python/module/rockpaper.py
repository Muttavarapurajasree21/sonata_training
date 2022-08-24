def RPS(p1,p2):
    if(p1=="r" and p2=="s") or (p1=="s" and p2=="p") or (p1=="p" and p2=="r"):
        print("Player1 won")
    elif (p2 == "r" and p1 == "s") or (p2 == "s" and p1 == "p") or (p2 == "p" and p1 == "r"):
        print("Player2 won")
    elif(p1==p2):
        print("It's a tie break")
    else:
        print("given a unauthorized sign")
RPS("r","s")