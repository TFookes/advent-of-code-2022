scores = {
    "X" : 1, # A Rock
    "Y" : 2, # B Paper
    "Z" : 3, # C Scissors
}

def calculate_round(opponent, me):
    if me == "X":     
        win = (opponent == "C")
        draw = (opponent == "A")
    elif me == "Y":
        win = (opponent == "A")
        draw = (opponent == "B")
    elif me == "Z":
        win = (opponent == "B")
        draw = (opponent == "C")

    if win: score = 6
    elif draw: score = 3
    else: score = 0

    return (score + scores[me])


if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]
        score = 0
        for round in lines:
            moves = round.split(" ")
            score += calculate_round(moves[0], moves[1])

        print(score)