class Env():
    def __init__(self):
        self.width = 5
        self.height = 5
        self.action_space = [0, 1, 2, 3]
        self.actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.rewards = [[0.0] * self.width for _ in range(self.height)]
        self.rewards[1][2] = -1.0
        self.rewards[2][1] = -1.0
        self.rewards[2][2] = 1.0

    def reset(self):
        state = [0, 0]
        return state

    #
    def step(self, state, action):
        next_state = self.state_after_action(state, action)
        reward = self.get_rewards(state, action)
        return next_state, reward

    def get_rewards(self, state, action):
        next_state = self.state_after_action(state, action)
        return self.rewards[state[0]][state[1]]

    def state_after_action(self, state, action):
        next_state = self.check_boundary([state[0] + self.actions[action][0], state[1]+ self.actions[action][1]])
        return next_state

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
