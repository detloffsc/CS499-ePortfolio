import json
import numpy as np

#set_maze = [[ 1,  0,  1,  1,  1,  1,  1,  1],
#            [ 1,  0,  1,  1,  1,  0,  1,  1],
#            [ 1,  1,  1,  1,  0,  1,  0,  1],
#            [ 1,  1,  1,  0,  1,  1,  1,  1],
#            [ 1,  1,  0,  1,  1,  1,  1,  1],
#            [ 1,  1,  1,  0,  1,  0,  0,  0],
#            [ 1,  1,  1,  0,  1,  1,  1,  1],
#            [ 1,  1,  1,  1,  0,  1,  1,  1]]

# Function to generate a solvable maze using backtracking algorithm
def generate_solvable_maze(size):
    maze = np.ones(size, dtype=np.int8)
    start = (0, 0)
    end = (size[0] - 1, size[1] - 1)
    stack = [start]
    maze[start] = 0

    while stack:
        current = stack[-1]
        if current == end:
            break
        neighbors = []
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_cell = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= next_cell[0] < size[0] and 0 <= next_cell[1] < size[1] and maze[next_cell] == 1:
                neighbors.append(next_cell)

        if neighbors:
            next_cell = neighbors[np.random.randint(0, len(neighbors))]
            stack.append(next_cell)
            maze[next_cell] = 0
        else:
            stack.pop()

    return maze

size = (25, 25)

rand_maze = generate_solvable_maze(size)
#print(rand_maze)

rand_maze_list = rand_maze.tolist()
json_object = json.dumps(rand_maze_list, indent=4)

with open("maze.json", "w") as outfile:
    outfile.write(json_object)