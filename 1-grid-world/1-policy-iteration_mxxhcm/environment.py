import numpy as np


WIDTH = 5
HEIGHT = 5
TRANSITION_PROB = 1
POSSIBLE_ACTIONS = [0, 1, 2, 3]    # up,down,left,right
ACTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# environment need provide reward and state transition
class Env:
    def __init__(self):
        self.height = HEIGHT
        self.width = WIDTH
        self.transition_prob = TRANSITION_PROB
        self.possible_actions = POSSIBLE_ACTIONS
        self.actions = ACTIONS
        self.rewards = [[0] * self.width for _ in range(self.height)]
        self.rewards[2][2] = 1
        self.rewards[2][1] = -1
        self.rewards[1][2] = -1
        self.states = []

        for i in range(self.height):
            for j in range(self.width):
                self.states.append([i, j])

    # get reward
    def get_reward(self, state, action):
        next_state = self.state_after_action(state, action)
        print(next_state)
        return self.rewards[next_state[0]][next_state[1]]

    # state transition
    def state_after_action(self, state, action_index):
        next_state = [state[0] + self.actions[action_index][0], state[1] + self.actions[action_index][1]]
        return self.check_boundary(next_state)

    # get all states
    def get_all_states(self):
        return self.states

    # check boundary
    def check_boundary(self, state):
        if state[0] < 0:
            state[0] = 0
        elif state[0] > self.height - 1:
            state[0] = self.height - 1

        if state[1] < 0:
            state[1] = 0
        elif state[1] > self.width - 1:
            state[1] = self.width - 1
        return state