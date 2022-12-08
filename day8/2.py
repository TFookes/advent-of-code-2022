import pandas as pd

def check_column(column, position): ## AND ALSO ROWS NOW
    score_up = 0
    score_down = 0
    size = column[position]
    for tree in column.iloc[:position][::-1]:
        score_up += 1
        if tree >= size: break

    for tree in column.iloc[position + 1:]:
        score_down += 1
        if tree >= size: break
        
    return score_up * score_down


if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]
        columns = []
        for line in lines:
            columns.append(list(line))

        df = pd.DataFrame(columns)
        visible_trees = []
        current_max = 0
        for i in range(1, len(df) - 1): ## ROWS starting from 1 to N - 1
            for j in range(1, len(df.columns) - 1): ## Columns starting from 1 to N - 1
                buffer = check_column(df.loc[:,i], j)
                buffer = buffer * check_column(df.iloc[j], i)

                if buffer > current_max: current_max = buffer
                
        print(current_max) 
