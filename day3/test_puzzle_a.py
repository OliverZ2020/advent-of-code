from puzzle_a import move_right, move_down

def test_move_down():
    # given
    row = 5
    step = 1
    # when
    cur_row = move_down(row=row, steps=step)
    # then
    assert cur_row == 6
    # given
    row = 5
    step = 2
    # when
    cur_row = move_down(row=row, steps=step)
    # then
    assert cur_row == 7


def test_move_right():
    map_row = "..#..#......###.#...#......#..#\n"
    width = len(map_row) - 1

    # given
    start_col = 0
    # when
    cur_col = move_right(column=start_col, width=width, steps=3)
    # then
    assert cur_col == 3

    # given
    start_col = 29
    # when
    cur_col = move_right(column=start_col, width=width, steps=3)
    # then
    assert cur_col == 1

    # given
    start_col = 30
    # when
    cur_col = move_right(column=start_col, width=width, steps=3)
    # then
    assert cur_col == 2