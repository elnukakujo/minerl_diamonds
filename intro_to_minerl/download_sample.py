# Export data directory location:
# 1. sudo nano   ~/.bashrc
# 2. Add export MINERL_DATA_ROOT=/home/noe_jager/Documents/minecraft/data/
# 3. source ~/.bashrc
# Download env : 
# python3 -m minerl.data.download --environment "MineRLObtainDiamond-v0"
# Then sample it 

import minerl
from minerl.data import BufferedBatchIter

data = minerl.data.make('MineRLTreechop-v0')
iterator = BufferedBatchIter(data)
for current_state, action, reward, next_state, done in iterator.buffered_batch_iter(batch_size=1, num_epochs=1):

    # Print the POV @ the first step of the sequence
    print("Current state", current_state['pov'][0])

    # Print the final reward pf the sequence!
    print("Rewards", reward[-1])

    # Check if final (next_state) is terminal.
    print("Done", done[-1])

    # ... do something with the data.
    print("At the end of trajectories the length can be < max_sequence_len", len(reward))
    quit()