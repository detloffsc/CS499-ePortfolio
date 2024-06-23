import json
import numpy as np

with open('test.json') as mazes:
    maze = json.load(mazes)

maze = np.array(maze)
size = maze.size

print(size)