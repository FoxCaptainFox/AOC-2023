from utils import read_file

def parse_seed_to_soil_mappings(paragraph):
    """Parse mappings from the paragraph and return a list of mapping dictionaries."""
    return [
        {"destination_start": int(parts[0]), "source_start": int(parts[1]), "source_length": int(parts[2])}
        for parts in (line.split(" ") for line in paragraph.split("\n")[1:])
    ]

def apply_mappings(measures, mapping_set):
    """Apply mappings to the given measures."""
    return [
        next((mapping["destination_start"] + measure - mapping["source_start"]
              for mapping in mapping_set
              if mapping["source_start"] <= measure < mapping["source_start"] + mapping["source_length"]),
             measure)
        for measure in measures
    ]


file_content = read_file(5)
paragraphs = file_content.split("\n\n")
mapping_sets = [parse_seed_to_soil_mappings(paragraph) for paragraph in paragraphs[1:]]

# Part 1
seeds = [int(x) for x in paragraphs[0].split("seeds: ")[1].split()]
current_measures = seeds
for mapping_set in mapping_sets:
    current_measures = apply_mappings(current_measures, mapping_set)

print(min(current_measures))

# Part 2
seeds_ranges = [int(x) for x in paragraphs[0].split("seeds: ")[1].split()]
seeds_packed = [list(range(start, start + length)) for start, length in zip(seeds_ranges[::2], seeds_ranges[1::2])]
seeds = [seed for seed_pack in seeds_packed for seed in seed_pack]

current_measures = seeds
for mapping_set in mapping_sets:
    current_measures = apply_mappings(current_measures, mapping_set)

print(min(current_measures))
