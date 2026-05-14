import matplotlib.pyplot as plt


def draw_path(grid, path, start, goal, save_path):
    plt.figure(figsize=(6, 6))

    plt.imshow(grid)

    if path:
        path_rows = []
        path_cols = []

        for row, col in path:
            path_rows.append(row)
            path_cols.append(col)

        plt.plot(path_cols, path_rows, linewidth=2)

    start_row, start_col = start
    goal_row, goal_col = goal

    plt.scatter(start_col, start_row, s=80, marker="o", label="Start")
    plt.scatter(goal_col, goal_row, s=80, marker="x", label="Goal")

    plt.title("A* Path Planning Result")
    plt.legend()
    plt.savefig(save_path, dpi=300)
    plt.close()
  