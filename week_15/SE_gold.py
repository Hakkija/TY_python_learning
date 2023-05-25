def gold(n):
    if n == 1:
        return 1
    else:
        return 2 * gold(n - 1) + 1
