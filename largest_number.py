from itertools import permutations


def largest_number_naive(numbers):
    final = ""
    numbers.sort(reverse = True)
    for number in numbers:
        final += str(number)
    return int(final)


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
