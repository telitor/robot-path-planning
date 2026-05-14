import numpy as np


###加载地图


def load_map(path):
    grid = np.loadtxt(path, delimiter = ",", dtype = int)
    return grid


###判断障碍


def obstacle_judge(grid, row, cols):
    return grid[row,cols] == 1

if __name__ == "__main__":
    grid = load_map("maps/map1.csv")

    print(grid)
    print("Map shape:", grid.shape)

    print("Cell (0, 0):", obstacle_judge(grid, 0, 0))
    print("Cell (1, 1):", obstacle_judge(grid, 1, 1))


###判断所在位置的四周是否是边界或者障碍


def get_neighbors(grid, row, col):
    neighbors = []

    directions = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
    ]

    rows, cols = grid.shape

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row, new_col] == 0:
                neighbors.append((new_row, new_col))

    return neighbors