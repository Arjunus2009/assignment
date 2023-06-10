def printboard():
    print(f"0 | 1 | 2 ")
    print(f"--|-- |--- ")
    print(f"3 | 4 | 5 ")
    print(f"--|-- |--- ")
    print(f"6 | 7 | 8 ")
    print(f"--|-- |--- ")
    
if __name__ == "__main__":
    xstate = [0,0,0,0,0,0,0,0,]
    zstate = [0,0,0,0,0,0,0,0,]
    turn = 1
    print("Wel come to tic tac toe")
    while(True):
        printboard()
        if (turn == 1):
                print("X's Chance")
                value = int(input("Please enter a value"))
                xstate[value] = 1
        else:
                print("X's Chance")
                value = int(input("Please enter a value"))
                zstate[value] = 1
        
        break
    
    