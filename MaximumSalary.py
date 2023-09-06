def maximumSalay(numbers):
    final = ""
    newNumbers = []
    for number in numbers:
        newNumbers.append(str(number).split(""))
    print(newNumbers)
    newNumbers.sort(reverse = True)
    for number in numbers:
        final += str(number)
    return int(final)

# _ = int(input())
# numbers = input().split()
print(maximumSalay([21,2]))
