def draw_board(rows, columns):
    max_rows = 19
    max_columns = 140
    rows = int(rows)
    columns = int(columns)
    if rows <= max_rows and columns <= max_columns:
        for row in range(rows):
            if row % 2 == 0:
                for col in range(1, columns):
                    if col % 2 == 1:
                        if col != columns - 1:
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print("-" * columns)
        return True
    elif rows > max_rows:
        print("Sorry, too many rows, I can't draw that")
        return False
    elif columns > max_columns:
        print("Sorry, too many columns, I can't draw that")
        return False
    elif rows > max_rows and columns > max_columns:
        print("Sorry, too many rows and columns, I can't draw that")

draw_board(19, 140)

