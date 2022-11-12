# read pickle
from getMoveAIPreProcessed.helpers import init_board, serialize_board
from getMoveAIPreProcessed.getMoveAI import getMoveAI
from getMoveAIPreProcessed.ogGetMoveAI import getMoveAI as ogGetMoveAI

import pickle
f=open('./getMoveAIPreProcessed/preprocessed.pickle', 'rb')
preprocessed=pickle.load(f)
f.close()

b=init_board()
b[2, 2]=1
print(getMoveAI(b, 2))
print(ogGetMoveAI(b, 2))

# print(getMoveAI(b, 1))

# print(preprocessed[serialize_board(b)])

# k=list(preprocessed.keys())[0]
# print(k, preprocessed[k])
