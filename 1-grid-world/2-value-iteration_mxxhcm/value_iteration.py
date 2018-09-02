from environment import Env
from copy import deepcopy

class ValueIteration:
    def __init__(self, env):
        self.env = env
        self.value_table = [[0.0] * env.width for _ in range(env.height)]
        self.policy_table = [[[0.25, 0.25, 0.25, 0.25]] * env.width for _ in range(env.height)]
        self.discount_factor = 0.9

    def get_state_value(self, state):
        return self.value_table[state[0]][state[1]]

    def get_policy_table(self):
        return self.policy_table

    def get_value_table(self):
        return self.value_table

    def value_iteration(self):
        # policy evaluation
        next_value_table = [[0.0]*self.env.width for _ in range(self.env.height)]
        for state in self.env.get_all_states():
            max_value = -0xffff
            if state == [2, 2]:
                next_value_table[2][2] = 0.0
                continue
            for action in self.env.possible_actions:
                next_state = self.env.state_after_action(state, action)
                reward = self.env.get_reward(state, action)
                next_value = self.get_state_value(next_state)
                value = reward + next_value * self.discount_factor
                if value > max_value:
                    max_value = value
            next_value_table[state[0]][state[1]] = round(max_value,2)

        self.value_table = next_value_table

        # policy iteration
        # next_policy_table = [[[0.25,0.25,0.25,0.25]]*self.env.width for _ in range(self.env.height)]
        # for state in self.env.get_all_states():
        #     if state == [2, 2]:
        #         continue
        #     max_value = -0xffff
        #     index = []
        #     for action in self.env.possible_actions:
        #         next_state = self.env.state_after_action(state, action)
        #         reward = self.env.get_reward(state, action)
        #         next_value = self.get_state_value(next_state)
        #         value = reward + next_value * self.discount_factor
        #         if value > max_value:
        #             index.clear()
        #             max_value = value
        #             index.append(action)
        #         elif value == max_value:
        #             index.append(action)
        #     new_state_policy = [0, 0, 0, 0]
        #     for i in index:
        #         new_state_policy[i] = 1.0/len(index)
        #     next_policy_table[state[0]][state[1]] = new_state_policy
        # self.policy_table = next_policy_table

if __name__ == "__main__":
    env = Env()
    value_iteration = ValueIteration(env)
    change_flag = True
    while change_flag:
        change_flag = False
        old_value_iteration = deepcopy(value_iteration.get_value_table())
        value_iteration.value_iteration()
        new_value_iteration = deepcopy(value_iteration.get_value_table())
        for i in range(value_iteration.env.width):
            for j in range(value_iteration.env.height):
                if old_value_iteration[i][j] != new_value_iteration[i][j]:
                    change_flag = True
        print(value_iteration.get_value_table())
