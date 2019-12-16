# CPS109 - Assignment 2
# Muhammad Alvi
# November 25th, 2019

# Initialize crossword matrix
board = [[' '] * 20 for i in range(20)]
v, h = 0, 0  # Global variables for intersections


# Function to display the updated board
def printboard(board):
    print(' ' + '~~' * len(board))

    m, n = len(board), len(board[0])

    for i in range(m):
        print('{', end='')
        for j in range(n):
            print(board[i][j], end=' ')
        print('} ')

    print(' ' + '~~' * len(board) + ' ')


# Function prints the first word to the middle of the board
def addfirstword(board, word) :
    # Checking to see if the word is too long
    if len(word) > len(board) :
        return False

    # Appending the letters of the word to the center of the board
    for i in range(len(word)) :
        row = len(board) // 2
        column = row - len(word) // 2 + i
        board[row][column] = word[i]
    printboard(board)
    return True


# Function to check vertical adjacencies
def isAdjacentV(board, word, intersect,  row, col):
    isAdjacent = True

    # Before intersection letter:
    if row - intersect <= 20:
        for k in range(1, intersect-1):
            if board[row-k][col+1] == ' ' and board[row-k][col-1] == ' ' and board[row-k][col] == ' ':
                isAdjacent = False
            else:
                return True

    # After intersection letter
    if row + len(word[intersect:]) <= 20:
        for k in range(1, len(word[intersect:])):
            if board[row+k][col+1] == ' ' and board[row+k][col-1] == ' ' and board[row+k][col] == ' ':
                isAdjacent = False
            else:
                return True

    return isAdjacent


# Function to check to see if its possible to add a word vertically
def checkvertical(board, word, row, col) :
    global v
    W = len(word)

    for v in range(W):
        if board[row][col] == word[v]:
            if v <= 20-row:
                # Only returns true if there are no vertical adjacencies
                if not isAdjacentV(board, word, v, row, col):
                    return True
    return False


def addvertical(board, word):
    m, n = len(board), len(board[0])

    for i in range(m):
        for j in range(n):
            if checkvertical(board, word, i, j):
                # Adds the letters to the board
                for w in range(len(word)):
                    if w <= v:
                        board[i-w][j] = word[v-w]
                    if v == 0:
                        if len(word) - v > w >= v:
                            board[i+w][j] = word[v + w]
                    else:
                        if len(word)-v+(v-1) > w >= v:
                            board[i+w-(v-1)][j] = word[v+w-(v-1)]

                # Prints the board if the word is successfully added
                printboard(board)
                return True
    return False


# Function to check horizontal adjacencies
def isAdjacentH(board, word, intersect,  row, col):
    isAdjacent = True

    # Before intersection letter:
    if col - intersect <= 20:
        for k in range(1, intersect+2):
            if board[row-1][col-k] == ' ' and board[row+1][col-k] == ' ' and board[row][col-k] == ' ':
                isAdjacent = False
            else:
                return True

    # After intersection letter
    if col + len(word[intersect:]) <= 20:
        for k in range(1, len(word[intersect:])):
            if board[row+1][col+k] == ' ' and board[row-1][col+k] == ' ' and board[row][col+k] == ' ':
                isAdjacent = False
            else:
                return True

    return isAdjacent


# Function to check to see if its possible to add a word vertically
def checkhorizontal(board, word, row, col):
    global h
    W = len(word)

    for h in range(W):
        if board[row][col] == word[h]:
            if h <= 20-col:
                # Only returns true if there are no horizontal adjacencies
                if not isAdjacentH(board, word, h, row, col):
                    return True
    return False


def addhorizontal(board, word):
    m, n = len(board), len(board[0])

    for i in range(m):
        for j in range(n):
            if checkhorizontal(board, word, i, j):
                # Adds the letters to the board
                for w in range(len(word)):
                    if w <= h:
                        board[i][j-w] = word[h-w]
                    if h == 0:
                        if len(word)-h > w >= h:
                            board[i][j+w] = word[h+w]
                    else:
                        if len(word)-h+(h-1) > w >= h:
                            board[i][j+w-(h-1)] = word[h+w-(h-1)]

                # Prints the board if the word is successfully added
                printboard(board)
                return True
    return False


# Function to add words to the board (alternates between horizontal and vertical)
def crossword(L, board):
    board = [[' '] * 20 for i in range(20)]
    addfirstword(board, L[0])

    # Alternates between adding words vertically and horizontally
    for i in range(1, len(L)):
        if i % 2 == 1:
            if not addvertical(board, L[i]):
                addhorizontal(board, L[i])
        else:
            if not addhorizontal(board, L[i]):
                addvertical(board, L[i])


crossword(['hippopotamus', 'horse', 'loon', 'snake', 'cat', 'rattlesnake', 'dinosaur'], board)
crossword(['deer', 'rainforest', 'google', 'cool', 'animal', 'life', 'cat'], board)




