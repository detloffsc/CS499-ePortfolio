epoch = 10
num_mazes = 500
size = (10, 10)

data = [
    (epoch, num_mazes, size[0], size[1])
]

print("Epochs: " + str(data[0][0]) + "\nNumber of mazes: " + str(data[0][1]) + "\nSize of mazes: " + str(data[0][2]) + "x" + str(data[0][3]))