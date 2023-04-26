import pandas as pd
import numpy as np
from neuralnetwork import ImitationLearning
import tensorflow as tf
import gym
import minerl
import time

output_name = ["attack","back", "forward","jump","left","right","sneak","sprint", "cleft", "cright", "cup", "cdown"]
action_name = ["attack","back", "camera", "forward","jump","left","right","sneak","sprint"]

# Run a random agent through the environment
env = gym.make("MineRLTreechop-v0")  # A MineRLTreechop-v0 env

obs = env.reset()
done = False

model = ImitationLearning(64, len(env.action_space.noop())+3)
model.compile(optimizer='adam',
              loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.neurons.load_weights('./checkpoints/my_checkpoint')

total_reward=0

while not done:
    # Take a no-op through the environment.
    output = model.neurons.predict(tf.expand_dims(obs['pov'], axis=0))[0]
    action = env.action_space.noop()
    if output_name[np.where(output == max(output))[0][0]] in action_name:
        action[output_name[np.where(output == max(output))[0][0]]]+=1
    else:
        action["camera"]=[float(-20*(output[-4]+output[-3])), float(20*(output[-2]-output[-1]))]
    print(action)
    obs, rew, done, _ = env.step(action)
    env.render()

    total_reward += rew
    print(total_reward)
    time.sleep(0.1)


