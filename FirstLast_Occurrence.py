def binary_search(arr, target):
    """Standard Binary Search: Returns any index where target is found."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def first_occurrence(arr, target):
    """Find the first (leftmost) occurrence of the target."""
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1  # keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def last_occurrence(arr, target):
    """Find the last (rightmost) occurrence of the target."""
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1  # keep searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


# Example usage
if __name__ == '__main__':
    arr = [1, 2, 4, 4, 4, 5, 6]
    target = 4

    print("Array:", arr)
    print("Target:", target)

    index = binary_search(arr, target)
    first = first_occurrence(arr, target)
    last = last_occurrence(arr, target)

    print("\Standard Binary Search Index:", index)
    print("First Occurrence Index:", first)
    print("Last Occurrence Index:", last)
