#SHOWING HOW TO PLAY THE GAME.


lstexample=['1','2','3','4','5','6','7',"8","9"]
print(lstexample[6]+" ! "+ lstexample[7]+" ! " + lstexample[8] +"\n\n"+lstexample[3]+" ! "+ lstexample[4]+" ! " + lstexample[5] +"\n\n"+lstexample[0]+" ! "+ lstexample[1]+" ! " + lstexample[2])
print('\n\n As seen above, use the keypad to input your turn into the game board \n\n')


#MAKING A FUNCTION TO CHECK IF A PLAYER WINS.

def win_check(lst):
    
    if ((lst[0]==second_player and lst[1]==second_player and lst[2]==second_player) or (lst[3]==second_player and lst[4]==second_player and lst[5]==second_player) or (lst[6]==second_player and lst[7]==second_player and lst[8]==second_player) or (lst[6]==second_player and lst[3]==second_player and lst[0]==second_player) or (lst[7]==second_player and lst[1]==second_player and lst[4]==second_player) or (lst[8]==second_player and lst[5]==second_player and lst[2]==second_player) or (lst[6]==second_player and lst[4]==second_player and lst[2]==second_player) or (lst[8]==second_player and lst[4]==second_player and lst[0]==second_player)) or ((lst[0]==first_player and lst[1]==first_player and lst[2]==first_player) or (lst[3]==first_player and lst[4]==first_player and lst[5]==first_player) or (lst[6]==first_player and lst[7]==first_player and lst[8]==first_player) or (lst[6]==first_player and lst[3]==first_player and lst[0]==first_player) or (lst[7]==first_player and lst[1]==first_player and lst[4]==first_player) or (lst[8]==first_player and lst[5]==first_player and lst[2]==first_player) or (lst[6]==first_player and lst[4]==first_player and lst[2]==first_player) or (lst[8]==first_player and lst[4]==first_player and lst[0]==first_player)):
        return True

#BUILDING A BASIC LIST AND GAME BOARD
lst=[" "," "," "," "," "," "," "," "," "]

print(lst[6]+" ! "+ lst[7]+" ! " + lst[8] +"\n\n"+lst[3]+" ! "+ lst[4]+" ! " + lst[5] +"\n\n"+lst[0]+" ! "+ lst[1]+" ! " + lst[2])

second_player=""

first_player= (input("who is first player (X OR O) : ")).upper()

#DEFINING A FUNCTION TO ENTER THE PLAYER'S INPUT INTO THE TABLE AND PRINT THE GAME BOARD

def game_board1(lst1,index,player):
    lst[(index-1)]=player
    game_board= lst[6]+" ! "+ lst[7]+" ! " + lst[8] +"\n\n"+lst[3]+" ! "+ lst[4]+" ! " + lst[5] +"\n\n"+lst[0]+" ! "+ lst[1]+" ! " + lst[2]
    print(game_board)
#ASSIGNING X AND O TO THE RESPECTIVE PLAYER
if first_player=="X":
    second_player="O"

    
else:
    second_player="X"

#RUNNING A LOOP TO GET THE INPUT OF THE PLAYER'S UNTIL SOMEONE WINS
i=0
while True:

    i=i+1
    
    print("Player One's turn","(", first_player,")")
    
    a= int(input("Enter a number: "))
    
    #CALLING THE FUNCTION
    
    game_board1(lst,a,first_player)

    if win_check(lst)==True:
        print("Player 1 wins")
        break
    
    #CHECK TO SEE IF THE MATCH IS A DRAW.
    
    if i<=7:
        pass
    else:
        print("The match is a draw")
        break
    
    i+=1
    print("Player Two's Turn","(", second_player,")")
    
    b=int(input("Enter a number: "))
    
    #CALLING THE FUNCTION
    
    game_board1(lst,b,second_player)

    if win_check(lst):
        print("\n Player 2 wins")
        break


    

    

        
