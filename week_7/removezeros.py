def removezeros(lst):
    found_zero_sum_sublist = True

    while found_zero_sum_sublist:
        found_zero_sum_sublist = False
        prefix_sums = [0]

        for i in range(len(lst)):
            prefix_sums.append(prefix_sums[-1] + lst[i])

        zero_sum_indices = set()
        for i in range(len(prefix_sums)):
            for j in range(i + 1, len(prefix_sums)):
                if prefix_sums[i] == prefix_sums[j]:
                    zero_sum_indices.update(range(i, j))

        if zero_sum_indices:
            found_zero_sum_sublist = True
            lst[:] = [lst[i] for i in range(len(lst)) if i not in zero_sum_indices]
