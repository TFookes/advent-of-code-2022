import numpy as np

grid = None

def dropSand(starting_x, starting_y):
    global grid
    try:
        if grid[starting_y + 1][starting_x] == 0: return dropSand(starting_x, starting_y + 1)
        elif grid[starting_y + 1][starting_x - 1] == 0: return dropSand(starting_x - 1, starting_y + 1)
        elif grid[starting_y + 1][starting_x + 1] == 0: return dropSand(starting_x + 1, starting_y + 1)
        elif grid[starting_y][starting_x] == 2: return False
        else: grid[starting_y][starting_x] = 2
    except IndexError:
        return False
        
    return True


if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]

        max_x = 0
        max_y = 0

        for line in lines:
            for coord in line.split(" -> "):
                if int(coord.split(",")[0]) > max_x: max_x = int(coord.split(",")[0])
                if int(coord.split(",")[1]) > max_y: max_y = int(coord.split(",")[1])

        grid = np.zeros((max_y + 3, max_x * 2))
        grid[max_y + 2] = 1
        
        for line in lines:
            line = line.split(" -> ")
            for i in range(len(line) - 1):
                coord1 = [int(x) for x in line[i].split(",")]
                coord2 = [int(x) for x in line[i + 1].split(",")]
                if coord1[0] == coord2[0]: ## Vertical Line
                    if coord1[1] < coord2[1]: grid[coord1[1]:coord2[1] + 1, coord1[0]] = 1
                    else: grid[coord2[1]:coord1[1] + 1, coord1[0]] = 1
                elif coord1[1] == coord2[1]: ## Horizontal Line
                    if coord1[0] < coord2[0]: grid[coord1[1], coord1[0]:coord2[0] + 1] = 1
                    else: grid[coord1[1], coord2[0]:coord1[0] + 1] = 1

        canDrop = True
        counter = 0

        while canDrop:
            canDrop = dropSand(500, 0)
            counter += 1

        print(counter - 1)