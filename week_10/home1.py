import math

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
def main():
    num_points = int(input("Enter the number of points: "))
    points = []

    for i in range(num_points):
        point_coordinates = input(f"Enter the coordinates of point {i + 1}: ")
        point = tuple(map(int, point_coordinates.strip('()').split(',')))
        points.append(point)

    min_distance = float('inf')
    min_points = (0, 0)

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                min_points = (i + 1, j + 1)

    print(f"Points {min_points[0]} and {min_points[1]} are the closest to each other.")


main()