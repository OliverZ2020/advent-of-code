from puzzle_b import move_right, move_down, count_trees

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

def test_count_trees():
    # given
    map_row1 = "..#..#......###.#...#......#..#\n"
    map_row2 = "...#.....#...#...#..........#..\n"
    map_row3 = "....#.#...............#.#.#....\n"
    map_row4 = ".........#.......##............\n"
    map_row5 = "#.#....#.#####.##.#........#..#\n"
    map_row6 = ".....#...##.#..#.##...#.#..#...\n"
    map = [map_row1, map_row2, map_row3, map_row4, map_row5, map_row6]
    cur_row = 0
    cur_col = 0
    right = 4
    down = 2
    # when
    trees = count_trees(map, cur_row, cur_col, right, down)
    # then
    assert trees == 1