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
                    if (cycle - 20) % 40 == 0: cycles[cycle] = register
                    cycle += 1
                case "addx":
                    if (cycle - 20) % 40 == 39: cycles[cycle + 1] = register
                    elif (cycle - 20) % 40 == 0: cycles[cycle] = register
                    register = register + int(line[1])
                    cycle += 2

    sum = 0
    for value in cycles:
        print(value, cycles[value], value * cycles[value])
        sum += value * cycles[value]

    print(sum)