def POINTS_COVER(points):

    solution = []
    points.sort()

    while points:
        Xm = points[0]
        l, r = Xm, Xm + 1
        solution.append((l, r))
        points = [point for point in points if point < l or point > r]
    return solution

points = [1, 2, 3, 6, 7, 8, 9, 11, 13, 15]
solution = POINTS_COVER(points)
print("Solution segments:")
for segment in solution:
    print(segment)
