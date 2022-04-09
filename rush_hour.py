import copy
import re
import time
# import _pickle as pickle
import ujson as pickle

# n =  problem number

CARS = ['A', 'X', 'K', 'C', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
CARS_LOWER = ['a', 'x', 'k', 'c', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
CAR_LENGTH = 2
TRUCKS = ['O', 'P', 'Q', 'R']
TRUCK_LOWER = ['o', 'p', 'q', 'r']
ALL_VEHICLES = ['A', 'X', 'K', 'C', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'a', 'x', 'k', 'c', 'b', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'O', 'P', 'Q', 'R', 'o', 'p', 'q', 'r']
TRUCK_LENGTH = 3


def text_load():
    text = open("rh.txt", "r")
    parsed_strings = []

    file = text.readlines()
    count = 0
    for line in file:
        count += 1
        parsed_strings.append("{}".format(line.strip()))
    remove_blanks(parsed_strings)
    return parsed_strings


def remove_blanks(list):
    """
    Takes in a list of strings and removes those that are blank
    :param list: List of strings in which the blanks have to removed.
    :return: none
    """
    for i in list:
        if i == "":
            list.remove(i)


def retrieve_problem(number, problem_list):
    """
    Returns the specified problem as a string
    :param number: The problem number to be retrieved
    :param problem_list:
    :return: str: problem
    """
    return problem_list[number]


def display_problem(problem):
    """
    Take in a 36 character string representing the board in rush hour and then represents it in a 6x6 array(list)
    :param problem: str: representation of the game board
    :return: list: 6x6 representation of the game board
    """
    array = []
    for i in range(1, 7):
        for z in range(1, 7):
            if z == 1:
                x = []
            x.append(problem[0])
            problem = problem[1:]
            if z == 6:
                array.append(x)

    return array


# for i in display_problem(x):
#     print(i)


# print(x)


# How to check if the

def convert_toLower_if_horizontal(array):
    """
    Takes in the rush hour array and returns an array with cares that are horizontal converted to lower case.
    :param array: list with character all in uppercase
    :return: list with horizontal characters are lower case.
    """
    for i in array:
        for x in range(1, 7):
            if i.count(i[x - 1]) > 1:
                indices = [index for (index, item) in enumerate(i) if item == i[x - 1]]
                for t in range(1, indices.__len__() + 1):
                    i[indices[t - 1]] = i[x - 1].lower()


def gen_next_states(array):
    """
    Take in a 6x6 game board that has been processed by convert to lower and returns a list of the next possible states

    :param array: The current state or state from which future states would like to be generated from.
    :return: list containing the next possible states from the current state
    """
    possible_states = []

    processed_vehicles_right = []
    processed_vehicles_left = []
    processed_vehicles_up = []
    processed_vehicles_down = []
    temp_array_copy = [None] * len(array)
    for y in range(1, 7):
        # Iterate through every square on the board and find the next letter
        for x in range(1, 7):
            # temp_array_copy = copy.deepcopy(array)
            # temp_array_copy = pickle.loads(pickle.dumps(array))

            vehicle = array[y - 1][x - 1]
            if vehicle in (processed_vehicles_right, processed_vehicles_down, processed_vehicles_left,
                           processed_vehicles_up):
                continue
            if vehicle.isalpha():
                # If horizontal
                if vehicle.islower():

                    if vehicle in CARS_LOWER:
                        # check if movement is possible with in bounds
                        # Right from second position

                        if (x - 1 + 1) <= 5 and vehicle not in processed_vehicles_right:
                            if array[y - 1][x - 1 + 1] == '.' and array[y - 1][x - 1 + 1] not in ALL_VEHICLES:
                                temp_array_copy = pickle.loads(pickle.dumps(array))
                                temp_array_copy[y - 1][x - 1 - 1] = '.'
                                temp_array_copy[y - 1][x - 1 + 1] = vehicle
                                processed_vehicles_right.append(vehicle)
                                possible_states.append(temp_array_copy)
                                # temp_array_copy = copy.deepcopy(array)

                        # Left from first postition
                        if x - 1 - 1 >= 0 and vehicle not in processed_vehicles_left:
                            if array[y - 1][x - 1 - 1] == '.' and array[y - 1][x - 1 - 1] not in ALL_VEHICLES:
                                temp_array_copy = pickle.loads(pickle.dumps(array))
                                temp_array_copy[y - 1][x - 1 - 1] = vehicle
                                temp_array_copy[y - 1][x - 1 + 1] = '.'
                                processed_vehicles_left.append(vehicle)
                                possible_states.append(temp_array_copy)
                                # temp_array_copy = copy.deepcopy(array)

                    if vehicle in TRUCK_LOWER:
                        # Right movement
                        if (x - 1 + 1) <= 5 and vehicle not in processed_vehicles_right:
                            if array[y - 1][x - 1 + 1] == '.' and array[y - 1][x - 1 + 1] not in ALL_VEHICLES:
                                temp_array_copy = pickle.loads(pickle.dumps(array))
                                temp_array_copy[y - 1][x - 1 - 2] = '.'
                                temp_array_copy[y - 1][x - 1 + 1] = vehicle
                                processed_vehicles_right.append(vehicle)
                                possible_states.append(temp_array_copy)
                                # temp_array_copy = copy.deepcopy(array)

                        if x - 1 - 1 >= 0 and vehicle not in processed_vehicles_left:
                            if array[y - 1][x - 1 - 1] == '.' and array[y - 1][x - 1 - 1] not in ALL_VEHICLES:
                                temp_array_copy = pickle.loads(pickle.dumps(array))
                                temp_array_copy[y - 1][x - 1 - 1] = vehicle
                                temp_array_copy[y - 1][x - 1 + 2] = '.'
                                processed_vehicles_left.append(vehicle)
                                possible_states.append(temp_array_copy)
                                # temp_array_copy = copy.deepcopy(array)

                # If vertical
                if vehicle.isupper():
                    if vehicle in CARS:
                        # check if movement is possible with in bounds
                        # Down movement

                        if (y - 1 + 1) <= 5 and vehicle not in processed_vehicles_down:
                            if array[y - 1 + 1][x - 1] == '.' and array[y - 1 + 1][x - 1] not in ALL_VEHICLES:
                                temp_array_copy = pickle.loads(pickle.dumps(array))
                                temp_array_copy[y - 1 - 1][x - 1] = '.'
                                temp_array_copy[y - 1 + 1][x - 1] = vehicle
                                processed_vehicles_down.append(vehicle)
                                possible_states.append(temp_array_copy)

                                # temp_array_copy = copy.deepcopy(array)
                        # UP Movement
                        if (y - 1 - 1) >= 0 and vehicle not in processed_vehicles_up:
                            if array[y - 1 - 1][x - 1] == '.' and array[y - 1 - 1][x - 1] not in ALL_VEHICLES:
                                temp_array_copy = pickle.loads(pickle.dumps(array))
                                temp_array_copy[y - 1 + 1][x - 1] = '.'
                                temp_array_copy[y - 1 - 1][x - 1] = vehicle
                                processed_vehicles_up.append(vehicle)
                                possible_states.append(temp_array_copy)

                                # temp_array_copy = copy.deepcopy(array)

                    if vehicle in TRUCKS:
                        # Down
                        if (y - 1 + 1) <= 5 and vehicle not in processed_vehicles_down:
                            if array[y - 1 + 1][x - 1] == '.' and array[y - 1 + 1][x - 1] not in ALL_VEHICLES:
                                temp_array_copy = pickle.loads(pickle.dumps(array))
                                temp_array_copy[y - 1 - 2][x - 1] = '.'
                                temp_array_copy[y - 1 + 1][x - 1] = vehicle
                                processed_vehicles_right.append(vehicle)
                                possible_states.append(temp_array_copy)

                                # temp_array_copy = copy.deepcopy(array)
                        # UP movement
                        if (y - 1 - 1) >= 0 and vehicle not in processed_vehicles_up:
                            if array[y - 1 - 1][x - 1] == '.' and array[y - 1 - 1][x - 1] not in ALL_VEHICLES:
                                temp_array_copy = pickle.loads(pickle.dumps(array))
                                temp_array_copy[y - 1 - 1][x - 1] = vehicle
                                temp_array_copy[y - 1 + 2][x - 1] = '.'
                                processed_vehicles_up.append(vehicle)
                                possible_states.append(temp_array_copy)

                                # temp_array_copy = copy.deepcopy(array)

    return possible_states


test = [['a', 'a', '.', '.', '.', 'O'],
        ['P', '.', '.', 'Q', '.', 'O'],
        ['P', 'x', 'x', 'Q', '.', 'O'],
        ['P', '.', '.', 'Q', '.', '.'],
        ['B', '.', '.', '.', 'c', 'c'],
        ['B', '.', 'r', 'r', 'r', '.']]


def bfs_search(start_state):
    queue = [[start_state]]
    seen_states = []

    while queue:

        path = queue.pop(0)
        if path[-1][2][5] == 'x':

            steps = 1
            for line in path:
                print('\n')
                print("Step {}".format(steps))
                steps += 1
                for item in line:
                    print(item)

            print('Total Steps:' + str(path.__len__()))
            return True

        for next_state in gen_next_states(path[-1]):

            if next_state not in seen_states:
                seen_states.append(next_state)
                queue.append(path + [next_state])



    else:
        return False


def display_solution(problem_number):
    search_string = 'Problem ' + str(problem_number)
    pattern = re.compile(".*{}".format(search_string))
    string_pattern = list(filter(pattern.match, temp))[0]
    solution_start = int(temp.index(string_pattern))
    print(solution_start)

    if problem_number == 40:
        solution_end = 565
    else:
        search_string = 'Problem ' + str(problem_number + 1)
        pattern = re.compile(".*{}".format(search_string))
        string_pattern = list(filter(pattern.match, temp))[0]
        solution_end = int(temp.index(string_pattern)) - 1
        print(solution_end)

    for j in range(solution_start, solution_end + 1):
        print(temp[j])


if __name__ == '__main__':

    failing_problems = [2, 13, 14]
    temp = text_load()
    while True:
        print("1.BFS")
        search_selection = int(input("What number algorithm would you like to run?"))
        print("1.Would you like to run this for a specific problem?")
        print("2. Would you like to run this for all problems?")
        problem_selection = int(input())
        # Load specific problem and then
        if problem_selection == 1:
            problem = int(input("Which problem would you like to load?"))
            # if problem in failing_problems:


            x = retrieve_problem(problem, temp)
            # Prints the problem before it is processed into the array
            display_solution(problem)
            print('Would you like to generate a solution for this problem?')
            answer = input('Y or N?')
            if answer == 'Y':
                x = display_problem(x)
                convert_toLower_if_horizontal(x)
                if search_selection == 1:
                    print('BFS Solution for problem {}'.format(problem))
                    start_time = time.time()
                    print(bfs_search(x))
                    executionTime = (time.time() - start_time)
                    print('Execution time in seconds: ' + str(executionTime))
            if answer == 'N':
                pass
        if problem_selection == 2:
            for i in range(1, 41):
                print('BFS Solution for problem {}'.format(i))

                x = retrieve_problem(i, temp)
                x = display_problem(x)
                convert_toLower_if_horizontal(x)
                print(bfs_search(x))

# Commented code bellow is for de
# temp = text_load()

# x = retrieve_problem(1, temp)
# # Prints the problem before it is processed into the array
# print(x)
# x = display_problem(x)
# print(x)
# convert_toLower_if_horizontal(x)
# bfs_search(x)
# # for p in x:
# #     print('\n')
# #     print(p)
# #
# #
# # for item in gen_next_states(x):
# #     print("\n")
# #     for z in item:
# #         print(z)


# TO DO
# Can compare two different heuristic designs.
