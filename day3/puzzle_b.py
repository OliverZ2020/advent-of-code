
def load_data(file_name):
    """Read all the lines from the data file and return as a list"""
    items = []
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        items.append(line)
    return items


def move_right(column, width, steps=3):
    new_col = column + steps
    if new_col > width - 1:
        new_col = new_col - width
    return new_col


def move_down(row, steps=1):
    new_row = row + steps
    return new_row


def count_trees(data, cur_row, cur_col, right_steps, down_steps):
    width = len(data[0]) - 1
    total_rows = len(data)
    counter = 0
    while(True):
        # cur_row does not change when moving right
        cur_col = move_right(column=cur_col, width=width, steps=right_steps)
        # move down
        cur_row = move_down(row=cur_row, steps=down_steps)

        if cur_row > total_rows - 1:
            # print(f'row: {cur_row}  col: {cur_col}')
            break

        char = data[cur_row][cur_col]
        # print(f'row: {cur_row}  col: {cur_col}  char: {char}')
        if char == "#":
            counter += 1
    return counter

map = load_data(file_name='./day3/data.txt')

product = 1
methods = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for method in methods:
    right, down = method
    cur_row = 0
    cur_col = 0
    trees = count_trees(map, cur_row, cur_col, right, down)
    print(f'right: {right}  down: {down}  trees: {trees}')
    product = product * trees

print(f'result: {product}')