import re

def do_instruction(instruction, stacks):
    for i in range(0, int(instruction["move"])):
        stacks[instruction["to"] - 1].insert(i, stacks[instruction["from"] - 1].pop(0))

    return stacks

if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [re.sub("\s{3,5}", " [.] ", line).replace("  ", " ").strip().split(" ") for line in lines]
        stacks = [[]] * len(lines[0])
        instructions = []
        instructions_flag = False

        for line in lines:
            if (len(line) == 1) or (line[0][0] != "[") and instructions_flag == False: 
                instructions_flag = True
                continue
            
            if not instructions_flag:
                print(line)
                for i, object in enumerate(line):
                    if object != "[.]":
                        stacks[i] = stacks[i] + [object]
            else:
                instructions += [{"move": int(line[1]), "from": int(line[3]), "to": int(line[5])}]

        #print(stacks)
        #print(instructions)

        for instruction in instructions:
            #print("\n")
            #print(stacks)
            #print("="*20)
            stacks = do_instruction(instruction, stacks)

        final_string = ""
        for stack in stacks: final_string += stack[0][1]

        print(final_string)