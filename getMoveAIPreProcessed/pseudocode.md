# About
There are 5478 legal game states
    of which 958 are finished games (no more moves possible)
    and 4519 are unfinished (game in progress). This is what get_all_boards() returns.


# Preprocess
```ts

fn get_all_boards(): BoardT[]
    boards=[]

    fn recursive_move(board, turn) //helper
        if board game is over
            return null
        else
            for each move in board //valid moves
                newBoard=board.copy() moved to move
                boards.add(newBoard)
                recursive_move(newBoard, switch turns)

    board=new Board()
    recursive_move(board, turn=X) //X always goes first

    return boards

fn solve_boards(boards): object mapping board (key) to best move (value)
    solutions={}

    num_boards=boards.length //progress bar
    for i, board in enumerate(boards)
        solutions[board.toString()]=solve(board)
        print(`Solved ${i} out of ${num_boards} boards`) //Progress bar

    return solutions


fn preprocess()
    boards=get_all_boards()
    solutions=solve_boards(boards)
    write solutions to file
        .txt file for reading
        .pickle for python

if name is main:
    preprocess()


```
