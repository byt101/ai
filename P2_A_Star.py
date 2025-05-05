# Implement A star Algorithm for any game search problem.

# Simple Implementation of A* 

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 5},
    'D': {'G': 2},
    'E': {'G': 2},
    'F': {'G': 1},
    'G': {}
}

heuristic = {
    'A': 6, 'B': 4, 'C': 4, 'D': 2, 'E': 2, 'F': 1, 'G': 0
}

def a_star(start, goal):
    open_list = {start}
    g = {start: 0}
    parents = {start: None}

    while open_list:
        current = min(open_list, key=lambda x: g[x] + heuristic[x])  # Get node with lowest cost
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]  # Return the path from start to goal

        open_list.remove(current)
        for neighbor, cost in graph[current].items():
            temp_g = g[current] + cost
            if neighbor not in g or temp_g < g[neighbor]:
                g[neighbor] = temp_g
                parents[neighbor] = current
                open_list.add(neighbor)

    return None

# Run A* from A to G
print("Path:", a_star('A', 'G'))


# ---------------------------------------Use Only One-------------------------------------------------


# Implemented A* using game

# Maze: 0 = open, 1 = wall
maze = [
    [0, 0, 0, 0],
    [1, 1, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 1, 0]
]

start = (0, 0)
goal = (3, 1)

rows = len(maze)
cols = len(maze[0])

# Heuristic: Manhattan distance to goal
def h(cell):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

def a_star():
    open_list = [start]
    came_from = {}
    cost = {start: 0}

    while open_list:
        current = min(open_list, key=lambda c: cost[c] + h(c))

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        open_list.remove(current)

        x, y = current
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            next_cell = (nx, ny)

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                new_cost = cost[current] + 1
                if next_cell not in cost or new_cost < cost[next_cell]:
                    cost[next_cell] = new_cost
                    came_from[next_cell] = current
                    if next_cell not in open_list:
                        open_list.append(next_cell)

    return None

# Run the A* algorithm
path = a_star()
print("Path from start to goal:", path)


# ---------------------------------------Use Only One-------------------------------------------------

# Maze problem using heapq and A* 

maze = [
    [0, 0, 0, 0],
    [1, 1, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 1, 0]
]

start = (0, 0)
goal = (3, 1)

def h(cell):
    x, y = cell
    gx, gy = goal
    return abs(x - gx) + abs(y - gy)

def a_star():
    from heapq import heappush, heappop

    open_set = []
    heappush(open_set, (h(start), 0, start))
    
    came = {}
    cost = {start: 0}

    while open_set:
        _, g, current = heappop(open_set)

        if current == goal:
            path = [current]
            while current in came:
                current = came[current]
                path.append(current)
            return path[::-1]

        x, y = current
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            next = (nx, ny)

            if 0 <= nx < 4 and 0 <= ny < 4 and maze[nx][ny] == 0:
                new_g = g + 1
                if next not in cost or new_g < cost[next]:
                    cost[next] = new_g
                    came[next] = current
                    f = new_g + h(next)
                    heappush(open_set, (f, new_g, next))

    return None

path = a_star()
print("Path:", path)
