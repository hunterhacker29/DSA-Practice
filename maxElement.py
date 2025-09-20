def find_max(arr):
    largest = float('-inf')
    n = len(arr)

    for i in range(n):
        largest = max(largest, arr[i])  # This works now since function name is not "max"

    print(largest)


if __name__ == '__main__':
    arr = [55, 32, -97, 99, 3, 67]
    find_max(arr)
