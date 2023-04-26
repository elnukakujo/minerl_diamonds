import os 
import numpy as np
import minerl
from minerl.data import BufferedBatchIter
import pandas as pd

x=list()
y=0
i=0

data = minerl.data.make('MineRLTreechop-v0')
iterator = BufferedBatchIter(data)
for current_state, action, reward, next_state, done in iterator.buffered_batch_iter(batch_size=1, num_epochs=1):
    print(i)

    # Print the POV @ the first step of the sequence
    

    # Print the action
    # Camera array: [Left/Right, Up/Down]

    camera = action["camera"][0]
    action.pop("camera")

    if camera[0] > 0:
        cleft = int(0)
        cright = int(1)
    elif camera[0] == 0:
        cleft = int(0)
        cright = int(0)
    elif camera[0] < 0:
        cleft = int(1)
        cright = int(0)
    
    if camera[1] > 0:
        cup = int(1)
        cdown = int(0)
    elif camera[1] == 0:
        cup = int(0)
        cdown = int(0)
    elif camera[1] < 0:
        cup = int(0)
        cdown = int(1)

    action["cleft"] = cleft
    action["cright"] = cright
    action["cup"] = cup
    action["cdown"] = cdown

    if type(y)!=pd.DataFrame:
        y = pd.DataFrame(action)
    else:
        y = pd.concat([y, pd.DataFrame(action)], ignore_index=True)
    x.append(current_state['pov'][0])
    
    i+=1
    if i >= 25000:
        break

np.save('X_tree.npy', np.array(x))

y.astype('int32').to_csv('y_tree.csv', index=False)