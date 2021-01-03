#Used model from deep Q netwrok excercise with few modifications
#Import all torch necessary
import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, fc_units= [64, 64]):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Number of states
            action_size (int): Number of actions
            seed (int): Random seed
            fc1_units (int): Number of units in first hidden layer
            fc2_units (int): Number of units in second hidden layer
        """
        #allows us to access methods from base class
        super(QNetwork, self).__init__()
        #Set the seed in our neural net
        self.seed = torch.manual_seed(seed)
        #Fully connected layers from state (fc1) to actions (fc3)
        self.norm = nn.LayerNorm(state_size)
        self.fc1 = nn.Linear(state_size, fc_units[0])
        self.fc2 = nn.Linear(fc_units[0], fc_units[1])
        self.fc3 = nn.Linear(fc_units[1], action_size)

    def forward(self, x):
        """Build a network that maps state to action values."""
        x = self.norm(x)
        x = self.fc1(x) 
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        return(x)