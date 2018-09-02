from collecti
ons import defaultdict
import random

class MCAgent():
    def __init__(self, actions):
        self.width = 5
        self.height = 5
        self.learning_rate = 0.01
        self.discount_factor = 0.9
        self.actions = actions
        self.epsilon = 0.1
        #
        self.value_tables = defaultdict(float)

    def get_action(self):

    def update(self):

    def save_samples(self):
