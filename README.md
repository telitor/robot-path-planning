<div align="center">

# 🤖 Robot Path Planning with A* Algorithm

### 基于 A* 算法的二维栅格地图路径规划系统

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Algorithm-A* Search-FF9800?style=for-the-badge">
  <img src="https://img.shields.io/badge/Map-CSV Grid-4CAF50?style=for-the-badge">
  <img src="https://img.shields.io/badge/Visualization-Matplotlib-2196F3?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-2ECC71?style=for-the-badge">
</p>

<p>
  A lightweight grid-based robot path planning project using the A* search algorithm.<br>
  支持 CSV 地图读取、障碍物避让、路径搜索、路径回溯与可视化展示。
</p>

</div>

---

## 📌 Project Overview | 项目简介

本项目实现了一个基于 **A* Search Algorithm** 的二维栅格地图路径规划系统。

项目使用 CSV 文件构建二维栅格地图，其中 `0` 表示可通行区域，`1` 表示障碍物。程序能够自动读取地图数据，基于 A* 算法搜索从起点到终点的可行路径，并将路径规划结果以图片和 GIF 动图的形式进行展示。

该项目面向 **机器人路径规划、无人系统基础算法、栅格地图搜索与智能体导航** 等方向，完整体现了从地图建模、算法搜索、路径回溯到结果可视化的基础工程流程。

---

## ✨ Highlights | 项目亮点

- 实现 A* 路径规划算法核心流程
- 支持从 CSV 文件读取二维栅格地图
- 支持障碍物判断与四邻域节点搜索
- 使用曼哈顿距离作为启发式函数
- 实现路径回溯，输出完整路径坐标
- 支持多张地图批量路径规划
- 支持 PNG 静态结果图与 GIF 动态路径演示
- 项目结构清晰，便于阅读、运行与展示

---

## 🎬 Path Search Animation | 路径搜索动图演示

<table>
  <tr>
    <td align="center"><b>Map 1</b></td>
    <td align="center"><b>Map 2</b></td>
    <td align="center"><b>Random Map</b></td>
  </tr>
  <tr>
    <td align="center">
      <img src="outputs/map1_path_demo.gif" width="260" alt="Map 1 A* Path Demo">
    </td>
    <td align="center">
      <img src="outputs/map2_path_demo.gif" width="260" alt="Map 2 A* Path Demo">
    </td>
    <td align="center">
      <img src="outputs/random_map_path_demo.gif" width="260" alt="Random Map A* Path Demo">
    </td>
  </tr>
</table>

<p align="center">
  <sub>
    The animation shows how the final A* path is progressively drawn from the start point to the goal point.
  </sub>
</p>

---

## 🖼️ Result Preview | 路径规划结果展示

<table>
  <tr>
    <td align="center"><b>Map 1 Result</b></td>
    <td align="center"><b>Map 2 Result</b></td>
    <td align="center"><b>Random Map Result</b></td>
  </tr>
  <tr>
    <td align="center">
      <img src="outputs/map1_astar.png" width="260" alt="Map 1 A* Result">
    </td>
    <td align="center">
      <img src="outputs/map2_astar.png" width="260" alt="Map 2 A* Result">
    </td>
    <td align="center">
      <img src="outputs/random_map_astar.png" width="260" alt="Random Map A* Result">
    </td>
  </tr>
</table>

图中：

- `Start` 表示起点
- `Goal` 表示终点
- 蓝色路径表示 A* 算法搜索得到的可行路径
- 深色区域表示障碍物
- 浅色区域表示可通行区域
- 路径会自动绕开障碍物区域

---

## 🗂️ Project Structure | 项目结构

```text
robot-path-planning/
│
├── maps/
│   ├── map1.csv                    # 固定测试地图 1
│   ├── map2.csv                    # 固定测试地图 2
│   └── random_map.csv              # 随机生成地图
│
├── outputs/
│   ├── map1_astar.png              # Map 1 静态路径规划结果
│   ├── map2_astar.png              # Map 2 静态路径规划结果
│   ├── random_map_astar.png        # Random Map 静态路径规划结果
│   ├── map1_path_demo.gif          # Map 1 动态路径演示
│   ├── map2_path_demo.gif          # Map 2 动态路径演示
│   └── random_map_path_demo.gif    # Random Map 动态路径演示
│
├── src/
│   ├── astar.py                    # A* 主算法与批量运行流程
│   ├── generate_map.py             # 随机地图生成器
│   ├── map_loader.py               # 地图读取、障碍物判断与邻居节点搜索
│   └── visualize.py                # 路径可视化模块
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🧩 Map Representation | 地图表示方式

本项目使用 CSV 文件表示二维栅格地图：

```text
0 = 可通行区域
1 = 障碍物
```

示例地图：

```text
0,0,0,0,0
1,1,1,1,0
0,0,0,0,0
0,1,1,1,1
0,0,0,0,0
```

程序会将 CSV 地图读取为 NumPy 二维数组，并在此基础上执行路径搜索。

---

## 🧠 Algorithm Principle | 算法原理

A* 算法是一种经典的启发式图搜索算法。它会综合考虑当前已经走过的实际代价和到目标点的估计代价，从而优先扩展更有可能到达终点的节点。

核心评价函数为：

```text
f(n) = g(n) + h(n)
```

其中：

- `g(n)`：从起点到当前节点的实际路径代价
- `h(n)`：从当前节点到终点的启发式估计代价
- `f(n)`：当前节点的综合评价分数

本项目采用 **Manhattan Distance 曼哈顿距离** 作为启发式函数：

```text
h(n) = |x1 - x2| + |y1 - y2|
```

该启发式函数适用于只能进行上下左右移动的二维栅格地图。

---

## 🔁 Core Workflow | 核心流程

A* 搜索过程主要包括：

```text
1. 读取 CSV 地图并转换为二维数组
2. 将起点加入 open_set
3. 从 open_set 中选择 f_score 最小的节点作为 current
4. 判断 current 是否到达终点
5. 若未到达终点，则扩展 current 周围可通行的邻居节点
6. 更新 came_from、g_score 和 f_score
7. 将新的候选节点加入 open_set
8. 重复搜索，直到找到终点或无路可走
9. 根据 came_from 回溯完整路径
10. 将路径结果保存为 PNG 图片并制作 GIF 展示
```

---

## 🚀 How to Run | 如何运行

### 1. 克隆项目

```bash
git clone https://github.com/telitor/robot-path-planning.git
cd robot-path-planning
```

### 2. 创建虚拟环境

Windows PowerShell：

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 运行 A* 路径规划

```bash
python src/astar.py
```

运行成功后，程序会自动处理多张地图，并将结果保存到：

```text
outputs/
```

生成的主要结果包括：

```text
map1_astar.png
map2_astar.png
random_map_astar.png
```

---

## ✅ Features Implemented | 已实现功能

- [x] CSV 栅格地图读取
- [x] 障碍物判断
- [x] 四邻域节点搜索
- [x] 曼哈顿距离启发式函数
- [x] A* 主循环
- [x] 路径回溯
- [x] 多地图批量运行
- [x] PNG 静态路径结果保存
- [x] GIF 动态路径过程展示
- [x] GitHub README 项目展示整理

---

## 🧱 Main Modules | 核心模块说明

| Module | Description |
|---|---|
| `map_loader.py` | 负责读取 CSV 地图，并提供障碍物判断与邻居节点搜索功能 |
| `astar.py` | 实现 A* 算法核心逻辑，包括路径搜索、代价更新与路径回溯 |
| `visualize.py` | 使用 Matplotlib 绘制地图、障碍物、起点、终点与最终路径 |
| `generate_map.py` | 生成随机栅格地图，用于测试路径规划算法的泛化能力 |

---

## 🎯 Project Significance | 项目意义

本项目不仅实现了 A* 算法的基础功能，也体现了一个完整算法工程项目应具备的基本结构：

```text
数据输入 → 地图建模 → 算法搜索 → 路径回溯 → 可视化输出 → GitHub 展示
```

通过该项目，可以进一步理解路径规划算法在移动机器人、无人系统、自动驾驶与智能体导航等方向中的基础作用。

---

## 👤 Author

Created by **telitor**

This project is part of my learning process in robotics path planning, algorithm implementation, and applied artificial intelligence.

---