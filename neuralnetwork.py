import os
import torch
from torch import nn

class BehaviourCloning(nn.Module):
    def __init__(self, in_channels, action_size):
        self.in_channels = in_channels
        self.action_size = action_size
        self.neurons = nn.Sequential(
            nn.Conv2d(self.in_channels, 20, (5,5)),
            nn.ReLU(),
            nn.MaxPool2d((2,2), stride=(2,2)),
            nn.Conv2d(20, 50, (5,5)),
            nn.ReLU(),
            nn.MaxPool2d((2,2), stride=(2,2)),
            nn.Linear(in_features=800, out_features=500),
            nn.ReLU(),
            nn.Linear(in_features=500, out_features=self.action_size),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        output = self.neurons(x)