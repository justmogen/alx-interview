def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for p in range(1, n):
        row = [1]
        for q in range(1, p):
            row.append(triangle[p - 1][q - 1] + triangle[p - 1][q])
        row.append(1)
        triangle.append(row)

    return triangle