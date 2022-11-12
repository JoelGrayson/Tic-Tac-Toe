```ts
type move=[number, number]

getMoveAI(board, turn: 1 | 2 /* X or O*/): move
    new_board=board.copy()
    return minimax(board, turn, 0).nextMove


minimax(board, turn: 1 | 2, depth=0 /* want lowest depth (fastest win) */): { payoff: -1 | 0 | 1; nextMove: move }
    // turn:
    //     1 -> X, max
    //     2 -> O, min
    // payoff:
    //     1 -> X wins
    //     0 -> draw
    //    -1 -> O wins

    // Base
    if board is done
        if X wins
            return { payoff: 1, nextMove: None }
        if O wins
            return { payoff: -1, nextMove: None }
        if draw
            return { payoff: 0, nextMove: None }


    // Recursive step
    payoffMoves=[]
    for each move in getMoves(board):
        new_board=board.copy()
        new_board.move(move, turn)

        payoffMoves+={
            payoff: minimax(new_board, turn==1 ? 2 : 1, depth+1).payoff  //other player's turn
            nextMove: move
        }

    if turn==1 //maximum's turn
        ret max(payoffMoves) based on payoff
    if turn==2 //minimum's turn
        ret min(payoffMoves) based on payoff


getMoves()
    ...

```