import numpy as np
# from getMoveAI.getMoveAI import getMoveAI
# from getMoveAIOptimized.getMoveAIOptimized import getMoveAI
from getMoveAIPreProcessed.getMoveAI import getMoveAI

"""
0 -> empty
1 -> X
2 -> O
"""
#global constant
num2XO={0:' ', 1:'X', 2:'O'}

#return an empty 3x3 for the tic tac toe game
def init_board():
	return np.zeros((3,3), dtype=np.int8)

#print the board in a nice format
def show_board(brd):
	s = ""
	for i in range(2):
		s += f"{num2XO[brd[i,0]]} | {num2XO[brd[i,1]]} | {num2XO[brd[i,2]]}\n" 
		s += "-- --- --\n"
	s += f"{num2XO[brd[2,0]]} | {num2XO[brd[2,1]]} | {num2XO[brd[2,2]]}\n" 
	print(s)


"""
Return value
0 -> No winner
1 -> player 1 (X) wins 
2 -> player 2 (O) wins 
"""
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

#################
# Get Move AI: YOUR CODE HERE
# minimax algorithm



#returns a tupe of ints (row, column)
def getMoveHuman(brd, turn):
	valid = False
	#loop while haven't gotten a valid move
	while not valid:
		print(f"Enter the ROW and COLUMN of the spot you would like to place your {num2XO[turn]}")
		mv = input("separated by a SPACE: ")
		try: #avoid crash on typos
			row, col = mv.split()
			row, col = int(row), int(col)
		except:
			valid = False
			continue #restart loop if bad format

		#make sure move is possible
		if brd[row,col] == 0:
			valid = True

	return row, col #type: ignore


#gm1 and gm2 are FUNCTIONS that 
#take a board and a 1/2 for current players turn
#and must return a tuple (r,c) for where to place the next piece
def game(gm1, gm2):
	brd = init_board()

	done = False
	winner = 0
	turn = 1

	#list of functions
	#either getHumanMove or an AI
	moveFns = [gm1, gm2]

	#loop while game no over
	#each loop is one turn
	while not done:
		#display the board
		show_board(brd)

		#get the currect players move fn
		getMove = moveFns[turn-1]

		#pass in copy of board to avoid it being modified
		r,c = getMove(brd.copy(), turn)

		if brd[r,c] != 0:
			print("Error: illegal Move")

		else:
			#update move
			brd[r,c] = turn

			#switch turns
			#1 -> 2, 2 -> 1
			turn = 3 - turn

			#check if the game has ended
			done, winner = checkTerminal(brd)


	show_board(brd)


	if winner:
		print(f"Player {num2XO[winner]} wins!")
	else:
		print("It's a draw!")




def main():
	"""
	#########################
	To test your AI, replace one of the 
	arguments to game with your AI function (without parens)
	"""

	while True:
		print('What would you like to do?')
		print('  "1" Play against AI (you go first)')
		print('  "2" Play against AI (AI goes first)')
		print('  "3" Watch AI play against AI')
		print('  "q" to quit')
		print('Type a number > ', end='')
		choice=input()
		if choice=='1':
			game(getMoveHuman, getMoveAI)
		elif choice=='2':
			game(getMoveAI, getMoveHuman)
		elif choice=='3':
			game(getMoveAI, getMoveAI)
		elif choice=='q':
			break
		else:
			print('Invalid choice')

if __name__=='__main__':
	main()
