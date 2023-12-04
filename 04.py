from collections import Counter
from utils import read_data

# General

def count_selected_winning_numbers(card):
    numbers = card.split(": ")[1]
    winning, selected = numbers.split(" | ")
    winning_numbers = {int(x) for x in winning.split() if x}
    selected_numbers = {int(x) for x in selected.split() if x}
    return len(winning_numbers & selected_numbers)

data = read_data(4)

# Part 1
points_sum = 0
for card in data:
    common_numbers_count = count_selected_winning_numbers(card)
    if 0 < common_numbers_count:
        points_sum += 2**(common_numbers_count - 1)
print(points_sum) 

# Part 2

copies_count = Counter()
for index, card in enumerate(data):
    common_numbers_count = count_selected_winning_numbers(card)
    for i in range(common_numbers_count):
        copies_count[index + i + 1] += copies_count[index] + 1

print(len(data) + sum(copies_count.values()))
