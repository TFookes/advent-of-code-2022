def count_calories_per_elf(snacklist):
    elves = []
    total_calories = 0
    for snack in snacklist:
        if snack == "":
            elves.append(total_calories)
            total_calories = 0
            continue

        total_calories += int(snack)

    print(elves)
    print(max(elves))

if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]
        count_calories_per_elf(lines)
