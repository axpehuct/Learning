import random
def sum_list(numbers):
    sum = 0
    for val in numbers:
        sum += val
    return  sum

def sum_list_recursive(numbers):
    if not numbers:
        return 0
    return numbers[-1] + sum_list_recursive(numbers[:-1])

number_list = []
for val in range(1, 900):
    val = random.randint(0, 100)
    number_list.append(val)

print(sum_list(number_list))
print(sum_list_recursive(number_list))


