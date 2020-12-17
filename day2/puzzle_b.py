def load_data(file_name: str) -> list:
    """Read all the lines from the data file and return as a list"""
    items = []
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        items.append(line)
    return items


def split_data_item(data_item: str) -> str:
    """Split the data item into policy and password"""
    policy, password = data_item.split(': ', maxsplit=2)
    return policy, password


def split_policy(p: str) -> str:
    """Split the policy into low, high and char"""
    range, char = p.split(' ', maxsplit=2)
    l, h = range.split('-', maxsplit=2)
    return int(l), int(h), char

def find_char_in_poistion(my_string: str, positon: int) -> str:
    """Find the char in the string by position

    Args:
        my_string (str): the string I have
        positon (int): the position where the char should be

    Returns:
        str: the char in the position of the string
    """
    index = positon - 1
    char = my_string[index]
    return char


counter = 0
data = load_data(file_name='./day2/data.txt')
for item in data:
    policy, password = split_data_item(data_item=item)
    low, high, char = split_policy(p=policy)
    char_low = find_char_in_poistion(my_string=password, positon=low)
    char_high = find_char_in_poistion(my_string=password, positon=high)
    if (char_low == char and char_high != char) or (char_low != char and char_high == char):
        counter += 1

print(f'counter: {counter}')