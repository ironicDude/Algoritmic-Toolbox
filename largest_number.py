from itertools import permutations


def largest_number_naive(numbers):
    final = ""
    newNumbers = []
    for number in numbers:
        newNumbers.append(list(number))
    flattenedNewNumbers = sum(newNumbers, [])
    flattenedNewNumbers.sort(reverse = True)
    for number in flattenedNewNumbers:
        final += str(number)
    return int(final)


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
