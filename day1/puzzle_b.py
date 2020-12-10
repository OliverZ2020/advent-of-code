
def load_data(file_name):
    numbers = []
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        numbers.append(int(line))
    return numbers

SUM_VALUE = 2020

#number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_list = load_data(file_name='./day1/data.txt')
total_numbers = len(number_list)
print(f"Total numbers: {total_numbers}")
counter = 0
for i in range(total_numbers - 2):
    # print(f"index i: {i} - value {number_list[i]}")
    for j in range(i + 1, total_numbers - 1):
        # print(f"index j: {j} - value {number_list[j]}")
        for k in range(j + 1, total_numbers):
            counter = counter + 1
            a = number_list[i]
            b = number_list[j]
            c = number_list[k]
            if a + b + c == SUM_VALUE:
                print(f"Found {a}, {b} and {c}")
                print(f"a * b * c = {a * b * c}")
                print(f"counter:{counter}")
                exit()