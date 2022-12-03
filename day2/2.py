scores = {
    "ROCK" : 1, # A Rock
    "PAPER" : 2, # B Paper
    "SCISSORS" : 3, # C Scissors
}

def calculate_round(opponent, me):
    if me == "X": # LOSE 
        if opponent == "A": move = "SCISSORS"
        elif opponent == "B": move = "ROCK"
        else: move = "PAPER"
    elif me == "Y": # DRAW
        if opponent == "A": move = "ROCK"
        elif opponent == "B": move = "PAPER"
        else: move = "SCISSORS"
    elif me == "Z": # WIN
        if opponent == "A": move = "PAPER"
        elif opponent == "B": move = "SCISSORS"
        else: move = "ROCK"

    if me == "Z": score = 6
    elif me == "Y": score = 3
    else: score = 0

    return (score + scores[move])


if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]
        score = 0
        for round in lines:
            moves = round.split(" ")
            score += calculate_round(moves[0], moves[1])

        print(score)