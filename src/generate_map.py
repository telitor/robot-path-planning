import numpy as np


###创建随机地图


def generate_random_map(rows=10, cols=10, obstacle_ratio=0.2):

    random_values = np.random.rand(rows,cols)
    grid = (random_values < obstacle_ratio).astype(int)
    grid[0,0] = 0
    grid[rows-1,cols-1] = 0
    np.savetxt("maps/random_map.csv", grid, delimiter = ",", fmt = "%d")

    print(grid)

generate_random_map()
