import numpy as np
from typing import Any, Dict, List, Literal, Tuple, Union
from numpy import float64
from numpy._typing import NDArray



# <Check Terminal>
def checkWin(brd):
	#HORIZONTAL + VERTICAL
	for i in range(3):
		if (brd[i,:] == 1).all() or (brd[:,i] == 1).all():
			return 1 #X wins
		if (brd[i,:] == 2).all() or (brd[:,i] == 2).all():
			return 2 #O wins

	#DIAGONAL
	center = brd[1,1] #store center player
	#down  diag
	if brd[0,0] == center and brd[2,2] == center:
		return center
	#up diag
	if brd[2,0] == center and brd[0,2] == center:
		return center	

	#no winner (either draw or game not over)
	return 0

def checkTerminal(brd):
	#call check win
	res = checkWin(brd)
	done = True
	#if no winner, check for draw
	if res == 0:
		#any empty spots means game not over
		if (brd == 0).any():
			done = False

	#return done and result of checkWin
	return (done, res)
# </Check Terminal>





# Typing
TurnT=Literal[1, 2]
PayoffT=Literal[-1, 0, 1]
MoveT=Tuple[int, int]
BoardT=NDArray[float64]
DepthT=int
PairT=Tuple[PayoffT, MoveT | None, DepthT] #Payoff, nextMove, and depth (number of moves from root)

def getMoveAI(board: BoardT, turn: TurnT) -> MoveT: # -> move
	move=minimax(board, turn, 0)[1]
	if move is None: #for typing. should never happen
		raise Exception('No move found. Something is wrong :(')
		return
	return move

def get_moves(board: BoardT) -> List[MoveT]:
	buff=np.where(board==0)
	moves=[]
	for i in range(len(buff[0])):
		moves.append((buff[0][i], buff[1][i])) #get x and y coords
	return moves

def minimax(board: BoardT, turn: TurnT, depth: DepthT=0) -> PairT: # (payoff: -1 | 0 | 1; nextMove: move; depth: int)
	# Base case
	(done, res)=checkTerminal(board) # Res: 1 -> x won, 2 -> o won, 0 -> draw
	if done:
		if res==0: #draw
			return 0, None, depth
		if res==1: #x wins
			return 1, None, depth
		if res==2: #o wins
			return -1, None, depth

	# Recursive step
	payoffMoves: List[PairT]=[]
	for move in get_moves(board):
		newBoard=board.copy()
		newBoard[move]=turn
		res=minimax(newBoard, 2 if turn==1 else 1, depth+1)
		payoffMoves.append((
			res[0], #payoff
			move, #move
			res[2] #depth
		))
	
	if turn==1: #maximum's turn (X):
		return max(payoffMoves) #sorts based on first and third ∴ sorts primarily based on how payoff and secondarily based on depth (how many moves it takes)
	if turn==2: #minimum's turn (O):
		return min(payoffMoves)


