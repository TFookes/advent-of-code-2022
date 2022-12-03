def compare_rucksack(bag_one, bag_two, bag_three):
    priority = 0
    for item in bag_one.intersection(bag_two.intersection(bag_three)):
        if item.isupper(): priority += ord(item) - 64 + 26
        else: priority += ord(item) - 96

    return priority


if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [list(line.strip()) for line in lines]
        priority = 0
        while len(lines) > 0:
            priority += compare_rucksack(set(lines.pop()), set(lines.pop()), set(lines.pop()))
        
        print(priority)