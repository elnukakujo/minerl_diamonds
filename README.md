# Learn to use Reinforcement Learning in Video Games with MineRL

This is a personal project using the MineRL library to test reinforcement learning in a video game environment.

## Setup

1. Install Anaconda:
    
    Linux: https://docs.anaconda.com/anaconda/install/linux/

2. Create an environment with Python 3.8:

    conda create -n minecraft python=3.8

3. Install Anaconda library

    conda install -c conda-forge libstdcxx-ng

3. Install the libraries form the requirements.txt file:

    pip install -r requirements.txt


## Work with MineRL

### Run a script

    xvfb-run python3 <your_script.py>

### Download training data

1. Export data directory location:

    sudo nano   ~/.bashrc
    Add export MINERL_DATA_ROOT=/home/noe_jager/Documents/minerl_diamonds/data/
    source ~/.bashrc

2. Download env : 

    python3 -m minerl.data.download --environment "MineRLObtainDiamond-v0"

### View the data

Random trajectory : 
    
    python3 -m minerl.viewer environment
    
Specific trajectory : 

    python3 -m minerl.viewer environment name_of_trajectory

### Interact with the agent:

    python -m minerl.interactor 5656

For more help with MineRL, check out the documentation: https://minerl.readthedocs.io/en/v0.4.4/index.html