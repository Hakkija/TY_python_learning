def more_than_three(basket_counts):
    result = []
    for i, count in enumerate(basket_counts):
        num_greater = sum(1 for j in range(i) if basket_counts[j] > 3)
        result.append(num_greater)
    return result
