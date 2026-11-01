
# Number of cache lines
number_of_lines = 8

# Memory block access sequence
access_sequence = [3, 11, 3, 19, 11, 27, 3]

# Initially empty cache
cache = [None] * number_of_lines

hits = 0
misses = 0

print("Block  Line  Result  Cache contents (line: block)")
print("-" * 58)

for block in access_sequence:

    # Calculate cache line
    line = block % number_of_lines

    # Check HIT or MISS
    if cache[line] == block:
        result = "HIT"
        hits += 1
    else:
        result = "MISS"
        misses += 1
        cache[line] = block

    # Display cache contents
    contents = ", ".join(
        f"{i}: {value}"
        for i, value in enumerate(cache)
        if value is not None
    )

    if not contents:
        contents = "Empty"

    print(f"{block:<6} {line:<5} {result:<7} {contents}")

# Calculate hit ratio
total_accesses = len(access_sequence)
hit_ratio = hits / total_accesses

print("\nTotal hits:", hits)
print("Total misses:", misses)
print(f"Hit ratio: {hits}/{total_accesses} = "
      f"{hit_ratio:.2f} ({hit_ratio * 100:.1f}%)")
