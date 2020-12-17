
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


def count_occurances(pwd: str, char: str) -> int:
    """Counts the occurances of the letter in the password"""
    return pwd.count(char)


counter = 0
data = load_data(file_name='./day2/data.txt')
for item in data:
    policy, password = split_data_item(data_item=item)
    low, high, char = split_policy(p=policy)
    occurances = count_occurances(pwd=password, char=char)
    if occurances >= low and occurances <= high:
        counter += 1
    
print(f'counter: {counter}')