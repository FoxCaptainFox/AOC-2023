from math import inf
from utils import read_data

# General 

data = read_data(6)

# Part 1

time_array = [int(x) for x in data[0].split(":")[1].split(" ") if x]
record_distance_array = [int(x) for x in data[1].split(":")[1].split(" ") if x]

result = 1
for index, time in enumerate(time_array):
    record_distance = record_distance_array[index]
    ways_to_beat_record = 0
    for button_time in range(time + 1):
        speed = button_time
        distance = speed * (time - button_time)
        if record_distance < distance:
            ways_to_beat_record += 1
    result *= ways_to_beat_record
print(result)

# Part 2

time = int("".join(data[0].split(":")[1].split(" ")))
record_distance = int("".join(data[1].split(":")[1].split(" ")))

min_button_time_to_win = None
for button_time in range(time + 1):
    speed = button_time
    distance = speed * (time - button_time)
    if record_distance < distance:
        min_button_time_to_win = button_time
        break

max_button_time_to_win = None
for button_time in range(time + 1, 0, -1):
    speed = button_time
    distance = speed * (time - button_time)
    if record_distance < distance:
        max_button_time_to_win = button_time
        break

print(max_button_time_to_win - min_button_time_to_win + 1)
