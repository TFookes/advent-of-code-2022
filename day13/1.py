import ast
import math

def convertToList(packet):
    if not type(packet) == list: return [packet]
    return packet

def compare(packet1, packet2):
    try:
        for i in range(0, max(len(packet1), len(packet2))):
            if not (type(packet1[i]) is int and type(packet2[i]) is int): ## If theyre both numbers, just do the comparison
                p1 = packet1[i]
                p2 = packet2[i]

                if type(packet1[i]) is list and type(packet2[i]) is not list: ## If just the left is a list, make the right a list
                    p2 = convertToList(packet2[i])
                elif type(packet1[i]) is not list and type(packet2[i]) is list: ## if just the right is a list, make the left a list 
                    p1 = convertToList(packet1[i])
                    
                done = compare(p1, p2) 
                if not done == None: return done
                else: continue
            
            order = int(packet1[i]) - int(packet2[i])
            if order == 0: # Packets are equal
                continue
            if order < 0: # Packets are in the correct order
                return True
            if order > 0: # Packets are in the incorrect order
                return False

        return None
        
    except IndexError:
        if len(packet1) < len(packet2): return True
        return False

    
if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]

        packet1 = None
        packet2 = None

        sum = 0

        for i, line in enumerate(lines):
            match(i % 3):
                case 0:
                    packet1 = ast.literal_eval(line)
                case 1:
                    packet2 = ast.literal_eval(line)
                    print(i, compare(packet1, packet2))
                    if compare(packet1, packet2): sum += math.ceil(i/3)
                case 2:
                    packet1 = None
                    packet2 = None

        print(sum)
