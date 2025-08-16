#Print Tic Tac Toe Board:
def print_tic_tac_toe(board):
    for row in board:
        print("|".join(row))
        print("_"*5)

def is_win(board,row,col,player):

    if all(board[i][col]==player for i in range(3)):
        return True

    if all (board[row][i]==player for i in range(3)):
        return True
    if all(board[i][i] ==player for i in range(3)):
        return True
    if all(board[i][2-i] ==player for i in range (3)):
        return True
    return  False




def game():
    board=[]
    count=1
    for i in range(3):
       board.append([str(count),str(count+1),str(count+2)])
       count+=3
    print(r"""
 ______ ____   __      ______  ____    __      ______  ___    ___          __  __ __ __  __  __      __  __  ___   __  __ 
|      |    | /  ]    |      |/    |  /  ]    |      |/   \  /  _]        |  ||  |  |  ||  ||  |    |  ||  |/   \ |  ||  |
|      ||  | /  /     |      |  o  | /  /     |      |     |/  [_         |_ ||_ |  |  ||_ ||_ |    |_ ||_ |     ||_ ||_ |
|_|  |_||  |/  /      |_|  |_|     |/  /      |_|  |_|  O  |    _]          \|  \|_   _|  \|  \|      \|  \|  O  |  \|  \|
  |  |  |  /   \_       |  | |  _  /   \_       |  | |     |   [_                |     |                   |     |        
  |  |  |  \     |      |  | |  |  \     |      |  | |     |     |               |  |  |                   |     |        
  |__| |____\____|      |__| |__|__|\____|      |__|  \___/|_____|               |__|__|                    \___/     
    """)
    print("Welcome To The World OF Tic Tac Toe\n")
    players=["X","0"]


    is_turn=True

    turn=0
    while is_turn:
        print_tic_tac_toe(board)
        player=players[turn%2]

        try:
            player_input=int(input(f"Enter Block Number Player {player}:{turn%2}-->"))
        except TypeError:
            print("Invalid input")
            continue
        if player_input>9:
            print("Wrong Input Please Enter Again")
            continue
        row,col=None,None
        for i in range(len(board)):
            for j in range(3):
                if (board[i][j])==str(player_input):
                    row,col=i,j
                    break
            if row is not None:
                break
        if row is None:
            print("Spot already Taken")
            continue
        board[row][col]=player

        if is_win(board,row, col, player):
            print(f"{player} is The Winner congratulations player {turn%2} 🎉🎉🎉🎉🎉")
            is_turn=False
        turn += 1
        if turn==9:
            print("Board is Full Game is Draw")
            is_turn=False

game()
