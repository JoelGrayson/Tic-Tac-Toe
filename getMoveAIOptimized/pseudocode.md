# Dumb getMoveAI() results
empty -> (2, 2)
(0, 0) -> (1, 1)
(0, 1) -> (0, 0)
(1, 1) -> (0, 0)


```ts

minimax
    threeBestMoves={ //on first move
        Board with turn at (0, 0): (1, 1),
        Board with turn at (0, 1): (0, 0),
        Board with turn at (1, 1): (0, 0)
    }

    if zero moves have been made:
        // try the three only moves possible ie (0, 0), (1, 0), (1, 1) recursively and 
        // save the result in threeBestMoves
    if one move has been made
        moveMadeSoFar=moveMadeSoFarOfBoard(board)
        for numRotations in range(4) //can only rotate 4 times
            moveMadeSoFar=rotate90(moveMadeSoFar)
            if moveMadeSoFar in threeBestMoves
                return rotate90 threeBestMoves[moveMadeSoFar] numRotation times
        new Error(`If the code reached this point, the move entered (${move}) is invalid`)

    else
        standard minimax procedure
        

rotate90()



```