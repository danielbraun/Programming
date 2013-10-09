def bubble_sort(numbers):
    nums = list(numbers)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if numbers[j] < numbers[i]:
                numbers[j], numbers[i] = numbers[i], numbers[j]
    return numbers


def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)
