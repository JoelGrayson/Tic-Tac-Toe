import numpy as np
from numpy._typing import NDArray
from typing import List, Literal, Tuple, Set, Dict

# <Typing>
TurnT=Literal[1, 2]
PayoffT=Literal[-1, 0, 1]
MoveT=Tuple[int, int]
BoardT=NDArray[np.int8]
DepthT=int
PairT=Tuple[PayoffT, MoveT | None, DepthT] #Payoff, nextMove, and depth (number of moves from root)
BoardsT=Set[bytes]
SerializedBoardT=bytes
BoardsAndTurnsT=Set[Tuple[SerializedBoardT, TurnT]]
SolutionsT=Dict[Tuple[SerializedBoardT, TurnT], MoveT]
# </Typing>

# My methods
def get_moves(board: BoardT) -> List[MoveT]:
	buff=np.where(board==0)
	moves=[]
	for i in range(len(buff[0])):
		moves.append((buff[0][i], buff[1][i]))
	return moves

def serialize_board(board: BoardT) -> bytes:
    return board.tobytes()


def deserialize_board(board: bytes) -> BoardT:
    return np.fromstring(board, dtype=np.int8).reshape((3, 3)) #type: ignore


# Fisher methods
def init_board():
	return np.zeros((3,3), dtype=np.int8)

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


"""
Returns a (boolean, int) tuple
Tuples contents repesent (is_game_over?, who_won?)
Not over -> (False, 0)
X wins -> (True, 1)
O wins -> (True, 2)
Draw -> (True, 0)
"""
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
