import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def draw_path(grid, path, start, goal, save_path):
    plt.figure(figsize=(4, 4))

    # 0 = 可走区域，1 = 障碍物
    cmap = ListedColormap(["#f8f9fa", "#2f3542"])
    plt.imshow(grid, cmap=cmap)

    # 画网格线
    rows, cols = grid.shape
    plt.xticks(range(cols))
    plt.yticks(range(rows))
    plt.grid(color="#dcdde1", linewidth=0.5)

    # 画路径
    if path:
        path_rows = []
        path_cols = []

        for row, col in path:
            path_rows.append(row)
            path_cols.append(col)

        plt.plot(
            path_cols,
            path_rows,
            color="#0984e3",
            linewidth=2.5,
            label="A* Path"
        )

    # 起点和终点
    start_row, start_col = start
    goal_row, goal_col = goal

    plt.scatter(
        start_col,
        start_row,
        s=90,
        color="#00b894",
        marker="o",
        edgecolors="black",
        linewidths=0.8,
        label="Start"
    )

    plt.scatter(
        goal_col,
        goal_row,
        s=100,
        color="#d63031",
        marker="X",
        edgecolors="black",
        linewidths=0.8,
        label="Goal"
    )

    plt.title("A* Path Planning Result", fontsize=11)
    plt.legend(loc="upper right", fontsize=8)
    plt.tight_layout()

    plt.savefig(save_path, dpi=180, bbox_inches="tight")
    plt.close()