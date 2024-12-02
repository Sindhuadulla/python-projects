
import random 

def display_board(board):
    print(board[1]+"|"+board[2]+"|"+board[3])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[7]+"|"+board[8]+"|"+board[9])
test_board=["#","X","O","X","O","X","O","X","O","X"]




def player_input():
    
    marker=""
    while not (marker=="X" or marker=="O") :
        marker=input("Player1: Do you want to be X or O:").upper()
    if marker=="X":
        return ("X","O")
    else:
        return ("O","X")


def place_board(board,marker,position):
    board[position]=marker 


def win_check(board,mark):
    return ( board[1]==mark and board[2]==mark and board[3]==mark )or ( board[4]==mark and board[5]==mark and board[6]==mark ) or ( board[7]==mark and board[8]==mark and board[9]==mark ) or ( board[1]==mark and board[4]==mark and board[7]==mark ) or( board[2]==mark and board[5]==mark and board[8]==mark ) or ( board[3]==mark and board[6]==mark and board[9]==mark )or ( board[1]==mark and board[5]==mark and board[9]==mark ) or ( board[3]==mark and board[5]==mark and board[7]==mark )

def choose_first():
    flip = random.randint(0,1)
    if flip==0:
        return 'player1'
    else:
        return 'player2'
def space_check(board,position):
    return board[position]==" "
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False 
    return True 
def player_next_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not (space_check(board,position)):
        position=int(input("Choose a position:(1-9)"))
    return position 
def replay():
    ans = input("Do you want to play again:(Say Yes or No)")
    return ans=="Yes"
print("Welcome to play Tic-Tac-Toe")
while True:
    the_board=[" "]*10
    player1,player2=player_input()
    turn = choose_first()
    print(turn+"will go first.") 
    play_game=input("Do you want to play? (Say Yes or No)")
    if play_game=="Yes":
        game_on =True
    else:
        game_on =False 
    while game_on:
        if turn=="player1" :
            display_board(the_board)
            position=player_next_choice(the_board)
            place_board(the_board,player1,position)
            if win_check(the_board,player1):
                display_board(the_board)
                print("Player1 has won!!")
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                    game_on=False
                else:
                    turn="player2"
        else:
            display_board(the_board)
            position=player_next_choice(the_board)
            place_board(the_board,player2,position)
            if win_check(the_board,player2):
                display_board(the_board)
                print("Player2 has won!!")
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                    game_on=False
                else:
                    turn="player1"


    if not replay():
        break 