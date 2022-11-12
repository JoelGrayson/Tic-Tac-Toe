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

