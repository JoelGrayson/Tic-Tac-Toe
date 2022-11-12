import pickle
from helpers import (
    # Fisher methods
    init_board, checkTerminal, #type: ignore
    # My methods
    get_moves, serialize_board, deserialize_board,
    # Typing
    BoardT, TurnT, MoveT, BoardsAndTurnsT, SolutionsT
)
from ogGetMoveAI import getMoveAI as ogGetMoveAI

def get_all_boards() -> BoardsAndTurnsT: #Returns all possible tic tac toe boards (should be of length 4519)
    boards: BoardsAndTurnsT=set() #hashed boards (bytes)

    def recursive_move(board: BoardT, turn: TurnT): # helper
        for move in get_moves(board):
            new_board=board.copy()
            new_board[move]=turn
            # Guard statements
            hashed=serialize_board(new_board)
            if (hashed, turn) in boards: #avoid duplicate moves. Massive speed boost
                continue
            if checkTerminal(new_board)[0]: #do not add completed boards
                continue

            switched_turn=2 if turn==1 else 1 #same as 3-turn
            boards.add((hashed, switched_turn))
            recursive_move(new_board, switched_turn)

    board=init_board()
    boards.add((serialize_board(board), 1)) #initial state
    recursive_move(board, 1)
    return boards

def solve_boards(boards: BoardsAndTurnsT) -> SolutionsT:
    solutions: SolutionsT={}
    num_boards=len(boards)
    for i, boardAndTurn in enumerate(boards):
        board, turn=boardAndTurn
        print(f'Solved {i+1} out of {num_boards} boards')
        d=deserialize_board(board)
        print(d)
        solutions[boardAndTurn]=ogGetMoveAI(d, turn)
    return solutions


def preprocess():
    print(f'Getting all boards...')
    all_boards=get_all_boards()
    print(f'Done ✅\nGot {len(all_boards)} boards')
    solutions=solve_boards(all_boards)
    print('Done coming up with solutions ✅')

    with open('./preprocessed.pickle', 'wb') as f:
        pickle.dump(solutions, f)
    print('Saved solutions in pickle file')

if __name__=='__main__':
    preprocess()
