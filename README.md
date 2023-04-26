# Learn to use Reinforcement Learning in Video Games with MineRL

This is a personal project using the MineRL library to test reinforcement learning in a video game environment.

## Setup

1. Install gcc and xvfb(used for running scripts):

    sudo apt install gcc
    sudo apt install xvfb

2. Install JDK 1.8 (Debian system):

    sudo add-apt-repository ppa:openjdk-r/ppa
    sudo apt-get update
    sudo apt-get install openjdk-8-jdk

3. Install Anaconda:
    
    Linux: https://docs.anaconda.com/anaconda/install/linux/

4. Create an environment with Python 3.9:

    conda create -n minecraft python=3.9

5. Install Anaconda library

    conda install -c conda-forge libstdcxx-ng

6. Install the libraries form the requirements.txt file:

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