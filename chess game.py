import chess
import chess.svg

def print_board(board):
    return chess.svg.board(board=board)

def is_valid_move(board, move):
    try:
        chess.Move.from_uci(move)
        return move in [m.uci() for m in board.legal_moves]
    except ValueError:
        return False

def main():
    board = chess.Board()
    while not board.is_game_over():
        print(print_board(board))
        move = input("Enter your move (e.g., 'e2e4'): ")
        
        if is_valid_move(board, move):
            board.push(chess.Move.from_uci(move))
        else:
            print("Invalid move. Try again.")

    print("Game over. Result: " + board.result())

if __name__ == "__main__":
    main()
