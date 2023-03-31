# To run: 
# xvfb-run python3 <your_script.py>

import gym
import minerl

#Creates the env
env = gym.make('MineRLNavigateDense-v0')

#Take actions
obs = env.reset() #Resets the env and return initial observation

done = False
net_reward = 0

while not done:
    """action = env.action_space.sample() #Sample random action from list of valid actions"""

    action = env.action_space.noop() # Gives dictionnary of actions with 0 for each value    

    action['camera'] = [0, 0.03*obs["compass"]["angle"]]
    action['back'] = 0
    action['forward'] = 1
    action['jump'] = 1
    action['attack'] = 1

    obs, reward, done, _ = env.step(action) #Take a step, get the new observation, get reward and see if finished

    net_reward += reward
    print("Total reward:", net_reward)
