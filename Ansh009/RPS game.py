import random
game_object=["rock", "scissor", "paper"]
'''
rock vs paper -> paper wiins
rock vs scissor-> rock wins
paper vs scissor->scissor wins
'''

    
while True:
    ccount=0
    ucount=0
    uc= int(input('''
 game start....... 
 1 Yes
 2 No | exit                
                '''))
    if uc==1:
        for a in range(1,6):
            userInput= int(input('''
  1 Rock
  2 scissor
  3 Pper                              
                    '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice=="paper"
            Cchoice=random.choice(game_object)
            #print(uchoice)
            #print(Cchoice)
            if Cchoice==uchoice:
                print("computer value", Cchoice)
                print("User value", uchoice )
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif(uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock" or 
                (uchoice=="scissor" and Cchoice=="paper")):
                print("computer value", Cchoice)
                print("User value", uchoice )
                print("You win")
                ucount=ucount+1
            else:
                print("computer value", Cchoice)
                print("User value", uchoice )
                print("computer win")
                ccount=ccount+1
        if ucount==ccount:
            print("Final game Draw....")
            print("User score", ucount)
            print("Computer Score",ccount)
        elif ucount>ccount:
            print("Final you win the game....")
            print("User score",ucount)
            print("Computer Score",ccount)
        else:
            print("Final computer  win the game....")
            print("User score",ucount)
            print("Computer Score",ccount)               
                
    else:
        break
    