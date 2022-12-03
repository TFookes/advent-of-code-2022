def compare_rucksack(items):
    pocket_one = set(items[:int(len(items)/2)])
    pocket_two = set(items[int((len(items)/2)):])

    priority = 0
    for item in pocket_one.intersection(pocket_two):
        if item.isupper(): priority += ord(item) - 64 + 26
        else: priority += ord(item) - 96

    return priority


if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [list(line.strip()) for line in lines]
        priority = 0
        for line in lines:
            priority += compare_rucksack(line)
        print(priority)