
def load_data(file_name):
    numbers = []
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        numbers.append(int(line))
    return numbers

SUM_VALUE = 2020

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number_list = load_data(file_name='./day1a/data.txt')
total_numbers = len(number_list)
print(f"Total numbers: {total_numbers}")
for i in range(total_numbers - 1):
    # print(f"index i: {i} - value {number_list[i]}")
    for j in range(i + 1, total_numbers):
        # print(f"index j: {j} - value {number_list[j]}")
        a = number_list[i]
        b = number_list[j]
        if a + b == SUM_VALUE:
            print(f"Found {a} and {b}")
            print(f"a * b = {a * b}")
            exit()
        