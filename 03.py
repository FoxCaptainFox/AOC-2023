from collections import defaultdict
import re
from utils import read_data

# General

data = read_data(3)

def find_number_ranges(line):
    """Find all number ranges in a line."""
    return [(match.start(), match.end() - 1) for match in re.finditer(r'\d+', line)]

# Part 1

def should_sum_number(data, line_index, number_range):
    start, end = number_range
    for i in range(max(0, line_index - 1), min(len(data), line_index + 2)):
        for j in range(max(0, start - 1), min(len(data[i]), end + 2)):
            if not(data[i][j].isdigit()) and data[i][j] != ".":
                return True
    return False

result_sum = 0
for line_index, line in enumerate(data):
    for number_range in find_number_ranges(line):
        if should_sum_number(data, line_index, number_range):
            result_sum += int(line[number_range[0]:number_range[1] + 1])
print(result_sum)

# Part 2

def update_gears(data, line_index, number_range, gears):
    start, end = number_range
    for i in range(max(0, line_index - 1), min(len(data), line_index + 2)):
        for j in range(max(0, start - 1), min(len(data[i]), end + 2)):
            if data[i][j] == "*":
                if (i, j) not in gears:
                    gears[(i, j)] = {'connected_numbers': 0, 'ratio': 1}
                gears[(i, j)]['connected_numbers'] += 1
                gears[(i, j)]['ratio'] *= int(data[line_index][start:end + 1])

gears = defaultdict(dict)
for line_index, line in enumerate(data):
    for number_range in find_number_ranges(line):
        update_gears(data, line_index, number_range, gears)

result = sum(gear['ratio'] for gear in gears.values() if gear['connected_numbers'] > 1)
print(result)
