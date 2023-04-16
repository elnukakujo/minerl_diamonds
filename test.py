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
    x.append(current_state['pov'][0])

    # Print the action
    # Camera array: [Left/Right, Up/Down]

    camera = action["camera"][0]
    action.pop("camera")

    camerax = camera[0]
    cameray = camera[1]

    action["camerax"] = camerax
    action["cameray"] = cameray

    if type(y)!=pd.DataFrame:
        y = pd.DataFrame.from_dict(action)
    else:
        y = pd.concat([y, pd.DataFrame.from_dict(action)], ignore_index=True)
    
    i+=1
    if i >= 100000:
        break

train = y
train["pov"] = x

train.to_csv('Treechop_data.csv', index=False)