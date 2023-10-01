def draw_line(m):
    x, y = 0, 0
    end_y = 5
    end_x = int(end_y * m)
    grid_size = 20 + 20 * (abs(m) // 4)
    print(grid_size)

    # Bresenham's line algorithm
    dx = abs(end_x - x)
    dy = abs(end_y - y)
    sx = 1 if x < end_x else -1
    sy = 1 if y < end_y else -1
    err = dx - dy

    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    while True:
        if x == end_x and y == end_y:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

        grid[y][x] = '*'

    # Print the grid in reverse order
    for row in reversed(grid):
        print(''.join(row))

m = int(input("M: "))
draw_line(m)
