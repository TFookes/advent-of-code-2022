from collections import defaultdict

if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip().split(" ") for line in lines]

        cycle = 1
        cycles = defaultdict(int)
        register = 1

        for i, line in enumerate(lines):
            match line[0]:
                case "noop": 
                    cycles[cycle] = register
                    cycle += 1
                case "addx":
                    cycles[cycle + 1] = register
                    cycles[cycle] = register
                    register = register + int(line[1])
                    cycle += 2

    for key in sorted(cycles):
        line_pos = key % 40
        if line_pos == 1: print("\n")

        if abs(line_pos - cycles[key] - 1) <= 1: print('#'*4, end='')
        else: print('.'*4, end='')