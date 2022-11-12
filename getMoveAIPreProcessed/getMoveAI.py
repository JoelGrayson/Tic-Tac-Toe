# Load Preprocessed Strategy
import pickle
f=open('./getMoveAIPreProcessed/preprocessed.pickle', 'rb') #because it is called from TTT.py, it needs to import from this path
preprocessed=pickle.load(f)
f.close()
from .helpers import serialize_board, deserialize_board

def getMoveAI(board, turn): # Uses preprocessed solutions
    solution=preprocessed.get((serialize_board(board), turn), "INVALID_BOARD")
    if solution=="INVALID_BOARD":
        raise Exception(f"Invalid board state:\n{str(board)}")
    return solution
