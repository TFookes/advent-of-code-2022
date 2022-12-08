import pandas as pd

def check_column(column, position):
    return (max(column.iloc[:position]) < column[position]) or (max(column.iloc[position + 1:]) < column[position])


def check_row(row, position):
    return (max(row.iloc[:position]) < row[position]) or (max(row.iloc[position + 1:]) < row[position])


if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]
        columns = []
        for line in lines:
            columns.append(list(line))

        df = pd.DataFrame(columns)
        visible_trees = []
        for i in range(1, len(df) - 1): ## ROWS starting from 1 to N - 1
            for j in range(1, len(df.columns) - 1): ## Columns starting from 1 to N - 1
                if check_column(df.loc[:,i], j): 
                    visible_trees += [(i, j)]
                    continue

                if check_row(df.iloc[j], i):
                    visible_trees += [(i, j)]

                    
        print(len(visible_trees) + len(df) * 2 + (len(df.columns) - 2) * 2) 
