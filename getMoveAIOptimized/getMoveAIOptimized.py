import numpy as np
from typing import Any, Dict, List, Literal, Tuple, Union
from numpy import float64
from numpy._typing import NDArray
from .checkTerminal import checkTerminal, init_board
import math

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

def number_of_moves_into_the_game(board: BoardT) -> int: #part of optimization
	num_empty_squares=len(np.where(board==0)[0])
	num_elements=math.prod(board.shape)
	return num_elements-num_empty_squares


def get_moves(board: BoardT) -> List[MoveT]:
	buff=np.where(board==0)
	moves=[]
	for i in range(len(buff[0])):
		moves.append((buff[0][i], buff[1][i]))
	return moves


def rotate90(move: MoveT) -> MoveT: #rotates a move 90°
	# (0, 0) -> ()
	sequences: List[List[MoveT]]=[
		[(1, 1)], #center
		[(0, 1), (1, 2), (2, 1), (1, 0)], #top middle
		[(0, 0), (0, 2), (2, 2), (2, 0)] #corners
	]
	for sequence in sequences:
		if move in sequence:
			indexOfItem=sequence.index(move)
			newIndex=(indexOfItem+1) % len(sequence)
			return sequence[newIndex]
	raise Exception(f'Cannot rotate move {move} by 90°. Invalid move')

def test_rotate90():
	assert rotate90((0, 1))==(1, 2)
	assert rotate90((1, 2))==(2, 1)
	assert rotate90((2, 1))==(1, 0)
	assert rotate90((0, 0))==(0, 2)
	assert rotate90((0, 2))==(2, 2)
	assert rotate90((2, 2))==(2, 0)
	assert rotate90((2, 0))==(0, 0)
	assert rotate90((1, 1))==(1, 1)


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


	# Interesting for debugging ↓
	# print('Depth', depth, '#moves into game', number_of_moves_into_the_game(board))
	# time.sleep(1)
	
	
	# <Optimizations>
	if depth==0 and number_of_moves_into_the_game(board)==0: #no moves made yet optimization
		firstBoard, secondBoard, thirdBoard=init_board(), init_board(), init_board()
		firstBoard[0, 0]=turn
		secondBoard[0, 1]=turn
		thirdBoard[1, 1]=turn
		
		threeBestMoves={
			str(firstBoard): minimax(firstBoard, 2 if turn==1 else 1, depth+1),
			str(secondBoard): minimax(secondBoard, 2 if turn==1 else 1, depth+1),
			str(thirdBoard): minimax(thirdBoard, 2 if turn==1 else 1, depth+1)
		}

		return max([threeBestMoves[str(firstBoard)], threeBestMoves[str(secondBoard)], threeBestMoves[str(thirdBoard)]])

	if depth==1 and number_of_moves_into_the_game(board)==1: #first move optimization
		print('depth at 1')
		firstBoard, secondBoard, thirdBoard=init_board(), init_board(), init_board()
		firstBoard[0, 0]=turn
		secondBoard[0, 1]=turn
		thirdBoard[1, 1]=turn
		
		threeBestMoves={
			str(firstBoard):  minimax(firstBoard,  2 if turn==1 else 1, depth+1),
			str(secondBoard): minimax(secondBoard, 2 if turn==1 else 1, depth+1),
			str(thirdBoard):  minimax(thirdBoard,  2 if turn==1 else 1, depth+1)
		}

		for numRotations in range(4): #can only rotate 4 times
			if str(board) in threeBestMoves:
				bestPair=threeBestMoves[str(board)]
				bestMove=bestPair[1] #need to rotate
				if bestMove==None:
					raise Exception(f'Move is invalid')
				for i in range(numRotations):
					bestMove=rotate90(bestMove)
				return (bestPair[0], bestMove, bestPair[2])
	# </Optimizations>


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


