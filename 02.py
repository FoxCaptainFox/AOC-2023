from functools import reduce
from utils import read_data

MAX_POSSIBLE_NUMBER = {"red": 12, "green": 13, "blue": 14}

data = read_data(2)
possible_combination_ids_sum, power_sum = 0, 0

for line in data:
    combination_id_str, description = line.split(': ', 1)
    combination_id = int(combination_id_str.split(' ')[-1])

    minimal_element_number = {}

    for combination in description.split("; "):
        for element in combination.split(", "):
            number, color = element.split(" ")
            number = int(number)

            if color not in minimal_element_number or number > minimal_element_number[color]:
                minimal_element_number[color] = number

    if all(color in minimal_element_number and minimal_element_number[color] <= MAX_POSSIBLE_NUMBER[color] for color in MAX_POSSIBLE_NUMBER):
        possible_combination_ids_sum += combination_id

    power_sum += reduce(lambda x, y: x * y, minimal_element_number.values())

print(possible_combination_ids_sum)
print(power_sum)
