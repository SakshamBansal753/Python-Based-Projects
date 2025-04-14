

win_conditions = [["", "", ""],
                  ["", "", ""],
                  ["", "", ""]
                  ]
class Win:
    def __init__(self):
        self.count=0




    def Move(self,row,col,move):
        if win_conditions[row][col]=="":
            win_conditions[row][col]=move
            return True
        return False

    def check_win(self,player):
        for row in win_conditions:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(win_conditions[row][col] == player for row in range(3)):
                return True
        if all(win_conditions[i][i] == player for i in range(3)):
            return True
        if all(win_conditions[i][2 - i] == player for i in range(3)):
            return True

        return False