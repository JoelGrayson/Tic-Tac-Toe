# Pseudocode
```ts
getMoveAI(board, turn: 1 | 2 /* X or O*/): move
    new_board=board.copy()
    ret minimax(board, turn, 'max').nextMove


minimax(board, turn: 1 | 2, minOrMax: 'min' | 'max'): { payoff: ; nextMove: [number, number] }
    if board==goal state
        return (payoff, nextMove)

    payoffMoves=[]
    for each move in board.moves:
        new_board=board.copy()
        new_board.move(move, turn)
        payoffMoves+={
            payoff: minimax(new_board, turn==1 ? 2 : 1, minOrMax=='min' ? 'max' : 'min') //other player's turn
            nextMove: move
        }

    if minOrMax=='max' //maximum's turn
        ret max(payoffMoves) based on payoff
    if minOrMax=='min' //minimum's turn
        ret min(payoffMoves) based on payoff

```

# Code
```py
def getMoveAI(board, turn: Literal[1] | Literal[2]) -> Tuple[int, int]: # -> move
	new_board=np.copy(board)
	return minimax(new_board, turn, 'max')['nextMove']

# x is max
# o is min
def minimax(board, turn: Literal[1] | Literal[2], minOrMax: Literal['min'] | Literal['max']='max'): # -> { payoff: -1 | 0 | 1, nextMove: (number, number) }
	# Base case: goal state
	(done, res)=checkTerminal(board)
	
	if res==1 and turn==1:
		payoff=1
	if res==2 and turn==2: #loss
		payoff=-1
	if res==0: #draw
		payoff=0

	if done: #done
		return {
			"payoff": payoff,
			"nextMove": None
		}
	
	# Recursive step
	payoffMoves=[]
	for move in get_moves(board): # Loop through all possible moves
		newBoard=np.copy(board) # New board with the move
		newBoard[move]=turn # 0 -> 1 (x), 1 -> 2 (o)
		# Get minimax of new board
		payoffMoves.append({
			"payoff": minimax(
				newBoard,
				2 if turn==1 else 1,
				'min' if minOrMax=='max' else 'max',
			)["payoff"],
			"nextMove": move
		})

	print('payoffMoves', payoffMoves)
	if minOrMax=='max': #maximum's turn
		return max(payoffMoves, key=lambda x: x["payoff"])
	elif minOrMax=='min': #minimum's turn
		return min(payoffMoves, key=lambda x: x["payoff"])


def get_moves(board):
	buff=np.where(board==0)
	moves=[]
	for i in range(len(buff[0])):
		moves.append((buff[0][i], buff[1][i]))
	return moves

```