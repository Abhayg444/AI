'''This is the simple example of Bayesian Belief Network of Buglarry
The CPT for Burglary is set so that there is a 0.001 probability of a burglary occurring and a 0.999 probability of no burglary occurring. 
The CPT for Alarm, given Burglary, is set so that there is a 0.9 probability of the alarm going off if there is a burglary and a 0.1 probability of the alarm going off
if there is no burglary.
The program then creates a BBN object and samples from it. The sample is printed to the console, which will show the state of each node in the BBN.
This is just a simple example of a BBN in Python. More complex BBNs can be created by adding more nodes and edges, and by setting more complex CPTs'''

import numpy as np
import random

class Node:
    def __init__(self, name, states):
        self.name = name
        self.states = states
        self.cpt = np.zeros((len(states), len(states)))

    def set_cpt(self, cpt):
        self.cpt = cpt

    def get_cpt(self):
        return self.cpt

    def sample(self):
        return random.choices(self.states, self.cpt[0])[0]

class BBN:
    def __init__(self, nodes):
        self.nodes = nodes

    def add_node(self, node):
        self.nodes.append(node)

    def get_nodes(self):
        return self.nodes

    def sample(self):
        return {node.name: node.sample() for node in self.nodes}

# Create a BBN with two nodes: Burglary and Alarm
burglary = Node("Burglary", ["True", "False"])
alarm = Node("Alarm", ["True", "False"])

# Set the conditional probability table (CPT) for Burglary
burglary.set_cpt(np.array([[0.001, 0.999], [0.9, 0.1]]))

# Set the CPT for Alarm, given Burglary
alarm.set_cpt(np.array([[0.9, 0.1], [0.1, 0.9]]))

# Create a BBN object
bbn = BBN([burglary, alarm])

# Sample from the BBN
sample = bbn.sample()

# Print the sample
print(sample)
