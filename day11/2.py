import math
from dataclasses import dataclass

@dataclass
class Monkey:
    monkey_number: int
    items: list
    worry_operation_value: int
    worry_operation: str
    test_operation_value: int
    monkey1: int 
    monkey2: int
    checks_done: int

    def __init__(self, monkey_number):
        self.monkey_number = monkey_number
        self.items = []
        self.worry_operation_value = None
        self.worry_operation = None
        self.test_operation_value = None
        self.monkey1 = None
        self.monkey2 = None
        self.checks_done = 0

    def _inspect_item(self, item):
        if self.worry_operation_value == "old": x = self.items[item]
        else: x = int(self.worry_operation_value)
        
        match self.worry_operation:
            case "*":
                self.items[item] = (self.items[item] * x) % N
            case "+":
                self.items[item] = (self.items[item] + x) % N

        #self.items[item] = int(math.floor(self.items[item] / 3))
        self.checks_done += 1

    def _test_item(self, item):
        return self.items[item] % self.test_operation_value == 0

    def add_item(self, item):
        self.items += [item]

    def throw_item(self, item, monkeys):
        self._inspect_item(item)
        if self._test_item(item): monkeys[self.monkey1].add_item(self.items[item])
        else: monkeys[self.monkey2].add_item(self.items[item])

        return monkeys

    def remove_items(self):
        self.items = []

monkeys = []
N = 1

def do_round():
    global monkeys 
    for monkey in monkeys:
        for i, item in enumerate(monkey.items):
            monkeys = monkey.throw_item(i, monkeys)

        monkey.remove_items()


def find_monkeys():
    throwiest_monkeys = []
    for i, monkey in enumerate(monkeys):
        if i == 0 or i == 1: throwiest_monkeys.append(monkey.checks_done)
        elif monkey.checks_done > min(throwiest_monkeys): 
            throwiest_monkeys.remove(min(throwiest_monkeys))
            throwiest_monkeys.append(monkey.checks_done)

    total = 1
    for i, monkey in enumerate(throwiest_monkeys):
        total = total * monkey

    print(total)


if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip().split(" ") for line in lines]

        current_monkey = None

        for line in lines:
            match line[0]:
                case "Monkey": #Monkey 0:
                    current_monkey = Monkey(int(line[1].replace(":", "")))
                    monkeys.append(current_monkey)
                case "Starting": #Starting items: 79, 60, 97
                    for item in " ".join(line).replace(',', '').split(" ")[2:]:
                        current_monkey.add_item(int(item))
                case "Operation:": #Operation: new = old * old
                    current_monkey.worry_operation = line[4]
                    current_monkey.worry_operation_value = line[5]
                case "Test:": #Test: divisible by 13
                    current_monkey.test_operation_value = int(line[3])
                    N = N * int(line[3])
                case "If": #If true: throw to monkey 0
                    if line[1] == "true:": current_monkey.monkey1 = int(line[5])
                    else: current_monkey.monkey2 = int(line[5])

        for i in range(0, 10000):
            print("ROUND: ", i)
            do_round()

        find_monkeys()