import random

def simulate_ant_movement(matrix_size):
    matrix = [[0] * matrix_size for _ in range(matrix_size)]
    x, y = random.randint(0, matrix_size - 1), random.randint(0, matrix_size - 1)
    direction = "N"
    steps = 0

    while 0 <= x < matrix_size and 0 <= y < matrix_size:
        if matrix[y][x] == 0:
            matrix[y][x] = 1
            direction = {"N": "W", "W": "S", "S": "E", "E": "N"}[direction]
            x, y = {"N": (x, y - 1), "W": (x - 1, y), "S": (x, y + 1), "E": (x + 1, y)}[direction]
        else:
            matrix[y][x] = 0
            direction = {"N": "E", "E": "S", "S": "W", "W": "N"}[direction]
            x, y = {"N": (x, y - 1), "E": (x + 1, y), "S": (x, y + 1), "W": (x - 1, y)}[direction]
        steps += 1

    ones = sum(row.count(1) for row in matrix)
    return steps, ones

def main():
    matrix_size = int(input("Enter dimension of the matrix: "))
    iterations = 1000

    total_steps = 0
    total_ones = 0

    for _ in range(iterations):
        steps, ones = simulate_ant_movement(matrix_size)
        total_steps += steps
        total_ones += ones

    avg_steps = total_steps / iterations
    avg_ones_percent = (total_ones / iterations) / (matrix_size ** 2) * 100

    print(f"Average number of steps is {avg_steps:.2f}")
    print(f"Average percent of ones at the end is {avg_ones_percent:.2f}")

main()
