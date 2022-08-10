#removes the value from the squares option list if it exists
def removeFromOptions(square, value):
    if value in square.options:
        square.options.remove(value)

#sets the squares value, removes the value from all other square options in the row, column and large square
def setSquareValue(square, rowIndex, colIndex, value):
    square.value = value
    for otherSquare in board[rowIndex]:
        removeFromOptions(otherSquare, value)
    for row in board:
        removeFromOptions(row[colIndex], value)
    rowLocation = ""
    colLocation = ""

    if rowIndex%3 == 0:#if this square is on the top row of the square
        rowLocation = "top"
    elif rowIndex%3 == 1:#if its the middle row of a square
        rowLocation = "mid"
    else:#must be the last row of a square
        rowLocation = "bot"

    if colIndex%3 == 0:#if this square is on the first col of the square
        colLocation = "left"
    elif colIndex%3 == 1:#if its the middle col of a square
        colLocation = "mid"
    else:#must be the last col of a square
        colLocation = "right"

#check larger square to see what numbers are contained in it
def checkLargeSquareForOptions(rowNumber, colNumber, square):
    rowLocation = ""
    colLocation = ""

    if rowNumber%3 == 0:#if this square is on the top row of the square
        rowLocation = "top"
    elif rowNumber%3 == 1:#if its the middle row of a square
        rowLocation = "mid"
    else:#must be the last row of a square
        rowLocation = "bot"

    if colNumber%3 == 0:#if this square is on the first col of the square
        colLocation = "left"
    elif colNumber%3 == 1:#if its the middle col of a square
        colLocation = "mid"
    else:#must be the last col of a square
        colLocation = "right"

    if rowLocation == "top" and colLocation == "left":
        compareSquare = board[rowNumber+1][colNumber+1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber+1][colNumber+2]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber+2][colNumber+1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber+2][colNumber+2]
        removeFromOptions(square,compareSquare.value)

    elif rowLocation == "top" and colLocation == "mid":
        compareSquare = board[rowNumber+1][colNumber-1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber+1][colNumber+1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber+2][colNumber-1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber+2][colNumber+1]
        removeFromOptions(square,compareSquare.value)

    elif rowLocation == "top" and colLocation == "right":
        compareSquare = board[rowNumber+1][colNumber-2]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber+1][colNumber-1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber+2][colNumber-2]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber+2][colNumber-1]
        removeFromOptions(square,compareSquare.value)

    elif rowLocation == "mid" and colLocation == "left":
        compareSquare = board[rowNumber-1][colNumber+1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber-1][colNumber+2]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber+1][colNumber+1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber+1][colNumber+2]
        removeFromOptions(square,compareSquare.value)

    elif rowLocation == "mid" and colLocation == "mid":
        compareSquare = board[rowNumber-1][colNumber-1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber-1][colNumber+1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber+1][colNumber-1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber+1][colNumber+1]
        removeFromOptions(square,compareSquare.value)

    elif rowLocation == "mid" and colLocation == "right":
        compareSquare = board[rowNumber-1][colNumber-1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber-1][colNumber-2]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber+1][colNumber-1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber+1][colNumber-2]
        removeFromOptions(square,compareSquare.value)

    elif rowLocation == "bot" and colLocation == "left":
        compareSquare = board[rowNumber-1][colNumber+1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber-2][colNumber+2]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber-1][colNumber+1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber-2][colNumber+2]
        removeFromOptions(square,compareSquare.value)

    elif rowLocation == "bot" and colLocation == "mid":
        compareSquare = board[rowNumber-1][colNumber-1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber-2][colNumber+1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber-1][colNumber-1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber-2][colNumber+1]
        removeFromOptions(square,compareSquare.value)

    elif rowLocation == "bot" and colLocation == "right":
        compareSquare = board[rowNumber-1][colNumber-1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber-2][colNumber-2]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber-1][colNumber-1]
        removeFromOptions(square,compareSquare.value)

        compareSquare = board[rowNumber-2][colNumber-2]
        removeFromOptions(square,compareSquare.value)


#check the passed row to see what numbers are contained in it.
def checkColumnForOptions(colNumber, square):
    for row in board:
        colCompareSquare = row[colNumber]
        removeFromOptions(square, colCompareSquare.value)

#check the passed row to see what numbers are contained in it.
def checkRowForOptions(rowNumber, square):
    for compareSquare in board[rowNumber]:
        removeFromOptions(square, compareSquare.value)

# go through each square and see what that square could be
def checkOptions(board):
    print("checking options")
    rowIndex = 0;
    for row in board:
        colIndex = 0
        for square in row:
            if square.value == 0:
                checkRowForOptions(rowIndex, square)
                checkColumnForOptions(colIndex, square)
                checkLargeSquareForOptions(rowIndex, colIndex, square)
                # if rowIndex == 5 and colIndex == 4:
                #     print(square.options)
            colIndex += 1
        rowIndex += 1


# find squares with only one option
def checkForSingleChoices(board):
    print("checking for single choices")
    rowIndex = 0
    for row in board:
        colIndex = 0
        for square in row:
            if square.value == 0:
                if len(square.options) == 1:
                    setSquareValue(square, rowIndex, colIndex, square.options[0])
            colIndex += 1
        rowIndex +=1

#check if any square still has 0
def checkSolved(board):
    print("checking if its solved")
    rowIndex = 0
    for row in board:
        colIndex = 0
        for square in row:
            if square.value == 0:
                return False
            colIndex += 1
        rowIndex +=1

#prints the resulting board
def printResultString(board):
    print("solved")
    numberNumbers = 0
    rowIndex = 0
    values = ""
    for row in board:
        colIndex = 0
        for square in row:
            values += str(square.value)
            values += " "
            numberNumbers += 1
            colIndex += 1
            if numberNumbers > 0 and numberNumbers % 3 == 0:
                values += "| "
        rowIndex += 1
        if rowIndex > 0 and numberNumbers % 9 == 0:
            print(values)
            values = ""
        if rowIndex > 0 and rowIndex < 9 and rowIndex % 3 == 0:
            rowOfDashes = "-----------------------"
            print(rowOfDashes)

class Square:
    #     options = []
    #     value = 0
    def __init__(self, value, column, square):
        self.options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.value = value
        self.column = column
        self.square = square


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solved = False
    board = []

    rowsSquares = [Square(0, 0, 0), Square(0, 1, 0), Square(0, 2, 0), Square(8, 3, 1), Square(0, 4, 1), Square(5, 5, 1),Square(0, 6, 2), Square(1, 7, 2), Square(3, 8, 2)]
    board.append(rowsSquares)
    rowsSquares = [Square(0, 0, 0), Square(0, 1, 0), Square(0, 2, 0), Square(2, 3, 1), Square(0, 4, 1), Square(3, 5, 1), Square(6, 6, 2), Square(0, 7, 2), Square(0, 8, 2)]
    board.append(rowsSquares)
    rowsSquares = [Square(6, 0, 0), Square(0, 1, 0), Square(0, 2, 0), Square(0, 3, 1), Square(9, 4, 1), Square(0, 5, 1), Square(2, 6, 2), Square(0, 7, 2), Square(4, 8, 2)]
    board.append(rowsSquares)
    rowsSquares = [Square(0, 0, 3), Square(0, 1, 3), Square(0, 2, 3), Square(0, 3, 4), Square(0, 4, 4), Square(0, 5, 4), Square(0, 6, 5), Square(0, 7, 5), Square(5, 8, 5)]
    board.append(rowsSquares)
    rowsSquares = [Square(0, 0, 3), Square(4, 1, 3), Square(0, 2, 3), Square(1, 3, 4), Square(0, 4, 4), Square(0, 5, 4), Square(7, 6, 5), Square(0, 7, 5), Square(6, 8, 5)]
    board.append(rowsSquares)
    rowsSquares = [Square(2, 0, 3), Square(5, 1, 3), Square(6, 2, 3), Square(3, 3, 4), Square(0, 4, 4), Square(4, 5, 4), Square(8, 6, 5), Square(9, 7, 5), Square(0, 8, 5)]
    board.append(rowsSquares)
    rowsSquares = [Square(5, 0, 6), Square(9, 1, 6), Square(0, 2, 6), Square(0, 3, 7), Square(0, 4, 7), Square(7, 5, 7), Square(1, 6, 8), Square(0, 7, 8), Square(2, 8, 8)]
    board.append(rowsSquares)
    rowsSquares = [Square(1, 0, 6), Square(0, 1, 6), Square(2, 2, 6), Square(0, 3, 7), Square(8, 4, 7), Square(0, 5, 7), Square(4, 6, 8), Square(7, 7, 8), Square(0, 8, 8)]
    board.append(rowsSquares)
    rowsSquares = [Square(0, 0, 6), Square(0, 1, 6), Square(4, 2, 6), Square(9, 3, 7), Square(1, 4, 7), Square(0, 5, 7), Square(0, 6, 8), Square(3, 7, 8), Square(8, 8, 8)]
    board.append(rowsSquares)

    solution = [[4, 2, 7, 8, 6, 5, 9, 1, 3], [9, 1, 5, 2, 4, 3, 6, 8, 7], [6, 8, 3, 7, 9, 1, 2, 5, 4],
                [8, 7, 1, 6, 2, 9, 3, 4, 5], [3, 4, 9, 1, 5, 8, 7, 2, 6], [2, 5, 6, 3, 7, 4, 8, 9, 1],
                [5, 9, 8, 4, 3, 7, 1, 6, 2], [1, 3, 2, 5, 8, 6, 4, 7, 9], [7, 6, 4, 9, 1, 2, 5, 3, 8]]

    checkOptions(board)
    while solved == False:
        checkForSingleChoices(board)
        solved = checkSolved(board)
    printResultString(board)
