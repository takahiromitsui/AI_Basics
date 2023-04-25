################################################################################
# Problem Setup: You want the perfect bread
# What influences this?
#  - how long do you toast it?
#  - how long after toasting do you eat the bread?
#  - Do you have power? And how much?
#  - Which toaster do you use?
################################################################################

import math
import random
from typing import Tuple, Union


################################################################################
# the function you are supposed to optimize.
# It has the following input:
#  toast_duration: duration of toasting in seconds. It is supposed to be an integer between 1 and 100
#  wait_duration: duration of waiting after toasting in seconds. It's supposed to be an integer between 1 and 100
#  toaster: the number of the toaster you want to use. It's supposed to be an integer, between 1 and 10.
#  power: how much power the toaster has (it's supposed to be a floating point number between 0 and 2)
################################################################################
def utility(toast_duration, wait_duration, power=1.0, toaster=1):
    # handle input errors
    if (not type(toast_duration) is int) and not (1 <= toast_duration <= 100):
        raise ValueError("toast_duration is not an integer")
    if (not type(wait_duration) is int) and not (1 <= wait_duration <= 100):
        raise ValueError("wait_duration is not an integer")
    if (not type(toaster) is int) and not (1 <= toaster <= 10):
        raise ValueError("toaster is not an integer or is not in a valid range")
    if (not type(power) is float) and not (0.0 <= power <= 2.0):
        raise ValueError("power is not a float or not in the valid range")

    # get toaster specific configuration
    hpt = [10, 8, 15, 7, 9, 2, 9, 19, 92, 32][toaster - 1]
    hpw = [1, 4, 19, 3, 20, 3, 1, 4, 1, 62][toaster - 1]
    toaster_utility = [1, 0.9, 0.7, 1.3, 0.3, 0.8, 0.5, 0.8, 3, 0.2][toaster - 1]

    # calculate values
    toast_utility = -0.1 * (toast_duration - hpt) ** 2 + 1
    wait_utility = -0.01 * (wait_duration - hpw) ** 2 + 1
    overall_utility = (toast_utility + wait_utility) * toaster_utility

    # apply modifier based on electricity
    power_factor = math.sin(10 * power + math.pi / 2 - 10) + power * 0.2
    overall_utility *= power_factor

    return overall_utility


################################################################################
# Writing this function is your homework.
# The function should return the tuple of parameters that optmizes the function.
#
# You can implement it in multiple difficulty levels:
# easy:
#     - implement it with only two parameters: toast_duration and wait_duration
#     - e.g., utility(2,3)
#     - Implement the function by testing all possible values for these variables.
#     - (This state space has only 10000 values, so it shouldn't take too long)
#
# medium:
#    - same as easy, but implement hill climbing
#    - see pseudo code
# hard:
#    - also use the parameter power
#    - e.g., utility(2,3,1.2)
#    - this introduces the following complications:
#        - multiple maxima
#        - a continuous parameter
#    - implement gradient ascent
# very hard:
#    - Same as hard, but use repeated search to find all maxima.
#    - repeated search:
#        - apply gradient descent from different starting points.
#    - I think there are 5 maxima. But I'm not sure :-P
# prepare to cry:
#    - find the optimum for all four parameters
#    - define your own algorithm!


class OptimiseAlgo:
    def __init__(self, objective_function):
        self.objective_function = objective_function

    # simple
    def simple_exhaustive_search(self) -> Tuple[int, int]:
        combinations = [(x, y) for x in range(1, 101) for y in range(1, 101)]

        maximum = (1, 1)
        for comb in combinations:
            if self.objective_function(*comb) > self.objective_function(*maximum):
                maximum = comb
        return maximum

    # medium and above
    def __generate_initial_value(
        self, param_num: int = 2
    ) -> Tuple[Union[int, float], ...]:
        if param_num == 2:
            return (random.randint(1, 100), random.randint(1, 100))
        if param_num == 3:
            return (
                random.randint(1, 100),
                random.randint(1, 100),
                random.uniform(0.0, 2.0),
            )
        if param_num == 4:
            return (
                random.randint(1, 100),
                random.randint(1, 100),
                random.uniform(0.0, 2.0),
                random.randint(1, 10),
            )
        else:
            raise ("param_num is not valid")

    def __get_best_neighbour(self, current_value: Tuple[int, int]) -> Tuple[int, int]:
        current_value_x = current_value[0]
        current_value_y = current_value[1]

        # generate all possible neighbours
        neighbours = [
            (current_value_x + 1, current_value_y),
            (current_value_x - 1, current_value_y),
            (current_value_x, current_value_y + 1),
            (current_value_x, current_value_y - 1),
            (current_value_x + 1, current_value_y + 1),
            (current_value_x - 1, current_value_y - 1),
            (current_value_x + 1, current_value_y - 1),
            (current_value_x - 1, current_value_y + 1),
        ]

        for neighbour in neighbours:
            if (
                neighbour[0] < 1
                or neighbour[0] > 100
                or neighbour[1] < 1
                or neighbour[1] > 100
            ):
                neighbours.remove(neighbour)

        # get the best neighbour
        best_neighbour = max(neighbours, key=lambda x: self.objective_function(*x))
        return best_neighbour

    # medium
    def medium_hill_climbing(self, n_iterations: int = 10000) -> Tuple[int, int]:
        # step3
        initial_point = self.__generate_initial_value()
        current_point = initial_point
        # step4: evaluate the initial point
        eval = self.objective_function(*current_point)
        # step5: repeat
        for i in range(n_iterations):
            # step6: take the best neighbor
            neighbor_x, neighbor_y = self.__get_best_neighbour(current_point)
            # step7: evaluate the neighbor
            neighbor_eval = self.objective_function(neighbor_x, neighbor_y)
            # step8: if the neighbor is better, move to it
            if neighbor_eval > eval:
                eval = neighbor_eval
                current_point = (neighbor_x, neighbor_y)
        return current_point

    # hard
    def hard_gradient_ascent(
        self, n_iterations: int = 10000, learning_rate=0.01
    ) -> Tuple[int, int, float]:
        # step1 Initialize the parameters
        initial_point = self.__generate_initial_value(param_num=3)
        current_point = initial_point
        # Step 2: Loop until convergence or until maximum iterations are reached
        for i in range(n_iterations):
            # Step 3: Get the current point
            toast_duration, wait_duration, power = current_point
            toaster = 1

            # get toaster specific configuration
            hpt = [10, 8, 15, 7, 9, 2, 9, 19, 92, 32][toaster - 1]
            hpw = [1, 4, 19, 3, 20, 3, 1, 4, 1, 62][toaster - 1]
            toaster_utility = [1, 0.9, 0.7, 1.3, 0.3, 0.8, 0.5, 0.8, 3, 0.2][
                toaster - 1
            ]
            toast_utility = -0.1 * (toast_duration - hpt) ** 2 + 1
            wait_utility = -0.01 * (wait_duration - hpw) ** 2 + 1
            power_factor = math.sin(10 * power + math.pi / 2 - 10) + power * 0.2

            # step4 Compute the gradient
            df_toast_duration = (
                -0.2 * (toast_duration - hpt) * toast_utility * power_factor
            )
            df_wait_duration = (
                -0.02 * (wait_duration - hpw) * wait_utility * power_factor
            )
            df_power = (
                toaster_utility
                * ((-0.5) * math.cos(10 * power + math.pi / 2 - 10) + 0.2)
            ) * (10 * math.cos(10 * power + math.pi / 2 - 10) + 0.2)
            # step5 Update the parameters
            toast_duration = max(
                min(toast_duration + learning_rate * df_toast_duration, 100), 1
            )
            wait_duration = max(
                min(wait_duration + learning_rate * df_wait_duration, 100), 1
            )
            power = max(min(power + learning_rate * df_power, 2.0), 0.0)

            current_point = (toast_duration, wait_duration, power)

        return (int(toast_duration), int(wait_duration), float(power))
    
    def very_hard_gradient_ascent(self, epochs:int =10, n_iterations: int = 10000, learning_rate=0.01):
        max_utility = float("-inf")
        for i in range(epochs):
            params = self.hard_gradient_ascent(n_iterations, learning_rate)
            utility = self.objective_function(*params)
            print(f"epoch {i}: {params} {utility}")
            if utility > max_utility:
                max_utility = utility
                max_utility_params = params
        return max_utility_params


def find_maximum():
    # TODO: Implement an optimization algorithm. Tip: (1,1) is not the optimum!
    optimiseAlgo = OptimiseAlgo(utility)
    # easy or simple
    # return optimiseAlgo.simple_exhaustive_search()
    # medium
    # return optimiseAlgo.medium_hill_climbing(n_iterations=100)
    # hard
    # return optimiseAlgo.hard_gradient_ascent(n_iterations=100)
    # very hard
    return optimiseAlgo.very_hard_gradient_ascent(epochs=100, n_iterations=100, learning_rate=0.01)


# use the function and see what it thinks the optimum is
optimum = find_maximum()
print(
    "Optimum:",
    optimum,
)
print("value:", utility(*optimum))
