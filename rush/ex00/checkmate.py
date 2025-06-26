def checkmate(board_str):
    board = [list(row) for row in board_str.strip().split('\n')]
    size = len(board)

    # Locate King
    king_pos = None
    for y in range(size):
        for x in range(len(board[y])):
            if board[y][x] == 'K':
                king_pos = (y, x)
                break
        if king_pos:
            break

    if not king_pos:
        print("Fail")
        return

    def in_bounds(y, x):
        return 0 <= y < size and 0 <= x < len(board[y])

    # check if pawn is attacking king
    def pawn():
        dy = 1
        for dx in [-1, 1]:
            ny, nx = king_pos[0] + dy, king_pos[1] + dx
            if in_bounds(ny, nx) and board[ny][nx] == 'P':
                return True
        return False
    #check bishop
    def bishop():
        for dy, dx in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            y, x = king_pos
            while True:
                y += dy
                x += dx
                if not in_bounds(y, x):
                    break
                if board[y][x] != '.':
                    if board[y][x] in ['B', 'Q']:
                        return True
                    break
        return False
 #check rook
    def rook():
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            y, x = king_pos
            while True:
                y += dy
                x += dx
                if not in_bounds(y, x):
                    break
                if board[y][x] != '.':
                    if board[y][x] in ['R', 'Q']:
                        return True
                    break
        return False
    #final check
    if pawn() or bishop() or rook():
        print("Success")
    else:
        print("Fail")