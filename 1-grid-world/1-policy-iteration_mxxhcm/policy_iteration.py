from environment import Env
import random
from copy import deepcopy

class PolicyIteration:
    def __init__(self, env):
        self.env = env
        # value table
        self.value_table = [[0.0] *self.env.width for _ in range(self.env.height)]
        # policy table
        self.policy_table = [[[0.25, 0.25, 0.25, 0.25]] * self.env.width for _ in range(self.env.height)]
        self.policy_table[2][2] = []
        self.discount_factor = 0.9

    # policy evaluation
    def policy_evaluation(self):
        next_value_table = [[0.0] * self.env.width for _ in range(self.env.height)]
        for state in self.env.get_all_states():
            value = 0.0
            if state == [2, 2]:
                next_value_table[state[0]][state[1]] = value
                continue

            # calculate value of state
            for action in self.env.possible_actions:
                reward = self.env.get_reward(state, action)
                next_state = self.env.state_after_action(state, action)
                next_value = self.get_value(next_state)
                value += self.policy_table[state[0]][state[1]][action] * (self.discount_factor * next_value + reward)
            next_value_table[state[0]][state[1]] = round(value,2)

        self.value_table = next_value_table

    def policy_improvement(self):
        next_policy_table = [[[0.25, 0.25, 0.25, 0.25]] * self.env.width for _ in range(self.env.height)]

        for state in self.env.get_all_states():
            if state == [2, 2]:
                continue
            max_value = -0xffff
            temp_index = []
            next_policy = [0, 0, 0, 0]
            for action in self.env.possible_actions:
                reward = self.env.get_reward(state, action)
                next_state = self.env.state_after_action(state, action)
                next_value = self.get_value(next_state)
                value = self.discount_factor * next_value + reward
                if value > max_value:
                    max_value = value
                    temp_index.clear()
                    temp_index.append(action)
                elif value == max_value:
                    temp_index.append(action)

            for i in temp_index:
                next_policy[i] = 1.0/len(temp_index)

            next_policy_table[state[0]][state[1]] = next_policy

        self.policy_table = next_policy_table

    def get_value_table(self):
        return self.value_table

    def get_value(self, state):
        return round(self.value_table[state[0]][state[1]],2)

    def get_action(self, state):
        temp = random.random()
        total = 0.0
        policy = self.get_policy(state)
        for i,p in enumerate(policy):
            total += p
            if total > temp:
                return i

    def get_policy(self,state):
        return self.policy_table[state[0]][state[1]]

    def get_policy_table(self):
        return self.policy_table


if __name__ == "__main__":
    env = Env()
    policy_iteration = PolicyIteration(env)
    policy_change_flag = True
    while policy_change_flag:
        policy_change_flag = False

        value_change_flag = True
        while value_change_flag:
            value_change_flag = False
            old_value_table = policy_iteration.get_value_table()
            policy_iteration.policy_evaluation()
            new_value_table = policy_iteration.get_value_table()
            print(new_value_table)
            for state in policy_iteration.env.get_all_states():
                if old_value_table[state[0]][state[1]] != new_value_table[state[0]][state[1]]:
                    value_change_flag = True

        old_policy_table = policy_iteration.get_policy_table()
        # old_policy_table = deepcopy(policy_iteration.get_policy_table())
        policy_iteration.policy_improvement()
        new_policy_table = policy_iteration.get_policy_table()
        print("new policy",new_policy_table)
        for state in policy_iteration.env.get_all_states():
            if old_policy_table[state[0]][state[1]] != new_policy_table[state[0]][state[1]]:
                policy_change_flag = True

    final_value_table = policy_iteration.get_value_table()
    print(final_value_table)