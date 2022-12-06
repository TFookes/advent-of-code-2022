def find_marker_pos(chars):
    buffer = []

    for pos, char in enumerate(chars):
        if check_ahead(3, pos, chars): return pos + 4


def check_ahead(num_to_look, pos, chars):
    buffer = [chars[pos]]
    for i in range(1, num_to_look + 1):
        if chars[pos + i] in buffer: return False
        buffer.append(chars[pos + i])

    print(buffer)
    return True


if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]
        for line in lines:
            print(find_marker_pos(line))