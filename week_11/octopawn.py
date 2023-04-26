def score_move(board, move, player):
    _, (i, j) = move
    if player == 1 and i == len(board) - 1:
        return 100
    if player == 2 and i == 0:
        return 100

    opponent = 3 - player
    score = 0

    if player == 1:
        if j > 0 and i < len(board) - 1 and board[i+1][j-1] == opponent:
            score += 50
        if j < len(board[i]) - 1 and i < len(board) - 1 and board[i+1][j+1] == opponent:
            score += 50
        if i < len(board) - 1 and board[i+1][j] == 0:
            score += 10
            if i < len(board) - 2 and board[i+2][j] == opponent:
                score += 20
    else:
        if j > 0 and i > 0 and board[i-1][j-1] == opponent:
            score += 50
        if j < len(board[i]) - 1 and i > 0 and board[i-1][j+1] == opponent:
            score += 50
        if i > 0 and board[i-1][j] == 0:
            score += 10
            if i > 1 and board[i-2][j] == opponent:
                score += 20

    return score


def find_move(board, player):
    moves = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player:
                if player == 1:
                    if i < len(board) - 1 and board[i+1][j] == 0:
                        moves.append(((i, j), (i+1, j)))
                    if j > 0 and i < len(board) - 1 and board[i+1][j-1] == 3 - player:
                        moves.append(((i, j), (i+1, j-1)))
                    if j < len(board[i]) - 1 and i < len(board) - 1 and board[i+1][j+1] == 3 - player:
                        moves.append(((i, j), (i+1, j+1)))
                elif player == 2:
                    if i > 0 and board[i-1][j] == 0:
                        moves.append(((i, j), (i-1, j)))
                    if j > 0 and i > 0 and board[i-1][j-1] == 3 - player:
                        moves.append(((i, j), (i-1, j-1)))
                    if j < len(board[i]) - 1 and i > 0 and board[i-1][j+1] == 3 - player:
                        moves.append(((i, j), (i-1, j+1)))

    best_move = None
    best_score = -1

    for move in moves:
        move_score = score_move(board, move, player)
        if move_score > best_score:
            best_move = move
            best_score = move_score

    return best_move
