def ACTSEL(segments):

    segments.sort(key=lambda segment: segment[1])
    solution = []

    last_end = float('-inf')
    for segment in segments:
        if segment[0] > last_end:
            solution.append(segment)
            last_end = segment[1]
    return solution

segments = [(1, 3), (2, 5), (4, 7), (6, 9)]
selected_segments = ACTSEL(segments)
print("Selected segments:")
for segment in selected_segments:
    print(segment)
