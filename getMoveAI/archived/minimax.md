```ts
minimax(board, turn: 'min' | 'max')
    if board=goal state
        return score
    
    for each move in board.moves:
        minimax(move, turn='min' ? 'max' : 'min')

```