def pascal_triangle(n):


    triangle = []
    for p in range(n):
        row = [1]
        if triangle:
            last_rows = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_rows, last_rows[1:])])
            row.append(1)
        triangle.append(row)
    return triangle
