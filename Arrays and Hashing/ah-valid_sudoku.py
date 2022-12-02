def isValidSudoku(board) -> bool:
    rows = cols = 9

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == '.':
                continue
            else:
                if validate(board, i, j) == False:
                    return False

    return True


def validate(grid, a, b):
    rows = cols = 9
    for i in range(rows):
        if a == i:
            continue
        else:
            if grid[a][b] == grid[i][b]:
                return False
    
    for i in range(rows):
        if b == i:
            continue
        else:
            if grid[a][b] == grid[a][i]:
                return False
    
    for i in range(3*math.floor(a/3), 3*math.floor(a/3)+3):
        for j in range(3*math.floor(b/3), 3*math.floor(b/3)+3):
            if i == a and b == j:
                continue
            else:
                if grid[a][b] == grid[i][j]:
                    return False
        
    return True