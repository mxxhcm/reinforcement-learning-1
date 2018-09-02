import numpy as np

WIDTH = 5
HEIGHT = 5
POSSIBLE_ACTIONS = [0, 1, 2, 3]     # up, down,left,right
ACTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Env:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.rewards = [[0.0] * self.width for _ in range(self.height)]
        self.states = []
        self.rewards[1][2] = - 1.0
        self.rewards[2][1] = - 1.0
        self.rewards[2][2] = 1.0
        self.possible_actions = POSSIBLE_ACTIONS
        self.actions = ACTIONS
        for i in range(self.height):
            for j in range(self.width):
                self.states.append([i, j])

    # get reward
    def get_reward(self,state, action):
        next_state = self.state_after_action(state, action)
        return self.rewards[next_state[0]][next_state[1]]

    # get states
    def get_all_states(self):
        return self.states

    # get next state
    def state_after_action(self, state, action):
        next_state = self.check_boundary([state[0] + self.actions[action][0], state[1]+ self.actions[action][1]])
        return next_state

    def check_boundary(self, state):
        if state[0] < 0:
            state[0] = 0
        elif state[0] > self.height - 1:
            state[0] = self.height -1
        if state[1] < 0:
            state[1] = 0
        elif state[1] > self.width - 1:
            state[1] = self.width - 1
        return state
