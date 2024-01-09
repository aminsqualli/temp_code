def split_into_subtuples(input_list, *subtuple_sizes):
    result = []
    start_index = 0

    for size in subtuple_sizes:
        end_index = start_index + size
        subtuple = tuple(input_list[start_index:end_index])
        result.append(subtuple)
        start_index = end_index

    return tuple(result)

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

⬤
