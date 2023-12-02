from utils import read_data

DIGIT_NAMES = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9
}

def find_digit_in_string(s, digit_names, from_start=True) -> int:
    """Find the first or last digit in a string."""
    index = 0 if from_start else -1
    while s:
        if s[index].isdigit():
            return int(s[index])
        for name, digit in digit_names.items():
            if (from_start and s.startswith(name)) or (not from_start and s.endswith(name)):
                return digit
        s = s[1:] if from_start else s[:-1]
    return None

data = read_data(1, output_type=int, as_separate_characters=True, filter_none=True)
result = sum([array[0] * 10 + array[-1] for array in data])
print(result)

data = read_data(1)
calibration_values = [find_digit_in_string(line, DIGIT_NAMES) * 10 + find_digit_in_string(line, DIGIT_NAMES, from_start=False) for line in data]
print(sum(calibration_values))
