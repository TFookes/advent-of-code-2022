def count_calories_per_elf(snacklist):
    elves = []
    total_calories = 0
    for snack in snacklist:
        if snack == "":
            elves.append(total_calories)
            total_calories = 0
            continue

        total_calories += int(snack)

    if total_calories != 0: elves.append(total_calories)

    elves.sort(reverse=True)
    print(elves)
    print(sum(elves[:3]))

if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]
        count_calories_per_elf(lines)
