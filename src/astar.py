from map_loader import load_map, get_neighbors
from visualize import draw_path
###曼哈顿距离（到终点距离）

def heuristic(current, goal):
    row1, col1 = current
    row2, col2 = goal
    return abs(row2 - row1) + abs(col2 - col1)


    
###A*(核心)

def astar(grid, start, goal):

    open_set = [start] ###接下来要看的点
    came_from = {} ###怎么走到这里的
    g_score = {start: 0} ###已经走了多远
    f_score = {start: heuristic(start, goal)} ###这条路值不值得继续走

    while open_set:
        current = min(open_set, key = lambda point: f_score[point]) ###选择最小的价值

        if current == goal: ###如果走到goal，就返回current
            return reconstruct_path(came_from, current)
        
        open_set.remove(current) ###每回更新current之后，将之前的旧的current删掉

        for neighbor in get_neighbors(grid, current[0], current[1]): ###寻找近邻，排除不合适的点，作为以后的新current
            new_g_score = g_score[current] + 1

            if neighbor not in g_score or new_g_score < g_score[neighbor]: ###判断这个neighbors是否值得更新（之前没见过的or价值最低的）
                came_from[neighbor] = current

                g_score[neighbor] = new_g_score ###更新已走的代价

                f_score[neighbor] = new_g_score + heuristic(neighbor, goal) ###更新距离目标点的代价

                if neighbor not in open_set: ###加入候选点准备检查
                    open_set.append(neighbor)

    return None


###路径回溯

def reconstruct_path(came_from, current):
    
    path = [current]

    
    while current in came_from:

        current = came_from[current]
        path.append(current)
        

    path.reverse()
    return path
        

###主流程

if __name__ == "__main__":
    grid = load_map("maps/map1.csv")

    start = (0, 0)
    goal = (9, 9)

    path = astar(grid, start, goal)

    if path is None:
        print("No path found.")
    else:
        draw_path(grid, path, start, goal, "outputs/map1_astar.png")
        print("Path found.")
        print("Path length:", len(path))
        print("Image saved to outputs/map1_astar.png")