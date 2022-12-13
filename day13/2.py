import ast

def merge(array, left_index, right_index, middle, comparison_function):
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        if comparison_function(left_copy[left_copy_index], right_copy[right_copy_index]):
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


def merge_sort(array, left_index, right_index, comparison_function):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle, comparison_function)
    merge_sort(array, middle + 1, right_index, comparison_function)
    merge(array, left_index, right_index, middle, comparison_function)


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
        lines = [ast.literal_eval(line.strip()) for line in lines if line.strip() != ""]

        lines = lines + [[[2]], [[6]]]

        merge_sort(lines, 0, len(lines), compare)

        product = (lines.index([[2]]) + 1) * (lines.index([[6]]) + 1)
        print(product)

