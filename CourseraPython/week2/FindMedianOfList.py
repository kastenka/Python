import random
import statistics


def create_list(number_size):
    numbers = []
    for _ in range(number_size):
        numbers.append(random.randint(10, 20))
    return sorted(numbers)


def find_median_solution1(number_size):
    numbers = create_list(number_size)
    half_size = number_size // 2
    median = None

    if number_size % 2 == 1:
        median = numbers[half_size]
    else:
        median = sum(numbers[half_size-1:half_size+1]) / 2
    print(f"Median of list {numbers} is {median}")


# модуль statistics для вывода медианы списка
def find_median_solution2(number_size):
    numbers = create_list(number_size)
    median = statistics.median(numbers)
    print(f"Median of list {numbers} is {median}")


size = random.randint(10, 15)
find_median_solution1(size)
find_median_solution2(size)
