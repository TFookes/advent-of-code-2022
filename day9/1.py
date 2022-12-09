def move_head(head, direction): # head = (x, y), direction = U, D, L, R
    match direction:
        case "U":
            head = (head[0], head[1] + 1)
        case "D":
            head = (head[0], head[1] - 1)
        case "L":
            head = (head[0] - 1, head[1])
        case "R":
            head = (head[0] + 1, head[1])
        
    return head


def move_tail(head, tail): # head, tail = (x, y)
    hx, hy = head
    tx, ty = tail

    if check_adjacent(hx, hy, tx, ty): return tail

    if hx == tx:
        if hy == ty: ## Head on top of tail
            pass
        elif hy > ty: ## Head directly above tail
            tail = (tx, ty + 1)
        elif hy < ty: ## Head directly below tail
            tail = (tx, ty - 1)
    elif hx > tx:
        if hy == ty: ## Head to the right of tail
            tail = (tx + 1, ty)
        elif hy > ty: ## Head to the right and above tail
            tail = (tx + 1, ty + 1)
        elif hy < ty: ## Head to the right and below tail
            tail = (tx + 1, ty - 1)
    elif hx < tx:
        if hy == ty: ## Head to the left of tail
            tail = (tx - 1, ty)
        elif hy > ty: ## Head to the left and above tail
            tail = (tx - 1, ty + 1)
        elif hy < ty: ## Head to the left and below tail
            tail = (tx - 1, ty - 1)

    return tail


def check_adjacent(hx, hy, tx, ty):
    return (abs(hx - tx) <= 1) and (abs(hy - ty) <= 1)


if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip().split(" ") for line in lines]

        pos_head = (0,0)
        pos_tail = (0,0)

        visited = set()

        for line in lines:
            for i in range(0, int(line[1])):
                pos_head = move_head(pos_head, line[0])
                pos_tail = move_tail(pos_head, pos_tail)
            
                visited.add(pos_tail)

        sorted_coords = sorted(sorted(list(visited), key=lambda tup: tup[0]), key=lambda tup: tup[1])
        print(sorted_coords)
        print(len(visited))