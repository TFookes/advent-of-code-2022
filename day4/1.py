def check_for_containment(ranges):
    elf1 = set([x for x in range(int(ranges[0].split("-")[0]), int(ranges[0].split("-")[1]) + 1)])
    elf2 = set([x for x in range(int(ranges[1].split("-")[0]), int(ranges[1].split("-")[1]) + 1)])
    
    return (elf1.issubset(elf2) or elf2.issubset(elf1))


if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip().split(",") for line in lines]
        count = 0
        for line in lines:
            if check_for_containment(line): 
                print(line, "TRUE")
                count += 1

        print(count)
