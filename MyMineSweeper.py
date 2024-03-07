import random

class boardSpot(object):
    def __init__(self):
        self.value = 0
        self.selected = False
        self.mine = False

    def __str__(self):
        return str(self.value)

    def isMine(self):
        return self.value == -1

class boardClass(object):
    def __init__(self, m_boardSize, m_numMines):
        self.board = [[boardSpot() for i in range(m_boardSize)] for j in range(m_boardSize)]
        self.boardSize = m_boardSize
        self.numMines = m_numMines
        self.selectableSpots = m_boardSize * m_boardSize - m_numMines
        i = 0
        while i < m_numMines:
            x = random.randint(0, self.boardSize-1)
            y = random.randint(0, self.boardSize-1)
            if not self.board[x][y].mine:
                self.addMine(x, y)
                i += 1
            else:
                i -= 1

    def __str__(self):
        returnString = " "
        divider = "\n---"

        for i in range(0, self.boardSize):
            returnString += f" | {i}"
            divider += "----"
        divider += "\n"

        returnString += divider
        for y in range(0, self.boardSize):
            returnString += str(y)
            for x in range(0, self.boardSize):
                if self.board[x][y].mine and self.board[x][y].selected:
                    returnString += f" | {self.board[x][y].value}"
                elif self.board[x][y].selected:
                    returnString += f" | {self.board[x][y].value} "
                else:
                    returnString += " |  "
            returnString += " |"
            returnString += divider
        return returnString

    def addMine(self, x, y):
        self.board[x][y].value = -1
        self.board[x][y].mine = True
        for i in range(max(0, x-1), min(self.boardSize, x+2)):
            for j in range(max(0, y-1), min(self.boardSize, y+2)):
                if not self.board[i][j].mine:
                    self.board[i][j].value += 1

    def makeMove(self, x, y):
        self.board[x][y].selected = True
        self.selectableSpots -= 1
        if self.board[x][y].value == -1:
            return False
        if self.board[x][y].value == 0:
            for i in range(max(0, x-1), min(self.boardSize, x+2)):
                for j in range(max(0, y-1), min(self.boardSize, y+2)):
                    if not self.board[i][j].selected:
                        self.makeMove(i, j)
            return True
        else:
            return True

    def hitMine(self, x, y):
        return self.board[x][y].value == -1

    def isWinner(self):
        return self.selectableSpots == 0

# play game
def playGame():
    boardSize = int(input("Choose the Width of the board: "))
    numMines = int(input("Choose the number of mines: "))
    gameOver = False
    winner = False
    Board = boardClass(boardSize, numMines)
    while not gameOver:
        print(Board)
        print("Make your move:")
        x = int(input("x: "))
        y = int(input("y: "))
        Board.makeMove(x, y)
        gameOver = Board.hitMine(x, y)
        if Board.isWinner() and not gameOver:
            gameOver = True
            winner = True

    print(Board)
    if winner:
        print("Congratulations, You Win!")
    else:
        print("You hit a mine, Game Over!")

if __name__ == "__main__":
    playGame()
