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

        pos_knot = [(0,0)]*10
        visited = set()

        for line in lines:
            for i in range(0, int(line[1])):
                pos_knot[0] = move_head(pos_knot[0], line[0]) ## Only the head (or first knot) moves as per the instructions
                for knot in range(1, 10):
                    pos_knot[knot] = move_tail(pos_knot[knot - 1], pos_knot[knot]) ## Move every knot as though the knot before was the head
                    if knot == 9: visited.add(pos_knot[knot]) ## only track the position of the last knot

        sorted_coords = sorted(sorted(list(visited), key=lambda tup: tup[0]), key=lambda tup: tup[1])
        print(sorted_coords)
        print(len(visited))