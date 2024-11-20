# Brute Force
def max_sub_array_of_size(k, arr):
    max_sum = 0

    for i in range(len(arr) - k + 1):
        window_sum = 0
        for j in range(i, i + k):
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)
    return max_sum


# Sliding Window
def max_sub_array_of_size(k, arr):
    l, r = 0, k - 1

    max_sum, cur_sum = 0, sum(arr[0:k])

    while r < len(arr) - 1:  # I prefer to use 'r' because of the r + 1 below. Make sure it won't go beyond len(arr)
        cur_sum = cur_sum - arr[l] + arr[r + 1]
        l += 1
        r += 1
        max_sum = max(max_sum, cur_sum)

    return max_sum


def max_sub_array_of_size(k, arr):
    max_sum, cur_sum = 0, 0
    left = 0

    for right in range(len(arr)):
        cur_sum += arr[right]  # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size 'k'
        if right >= k - 1:
            max_sum = max(max_sum, cur_sum)
            cur_sum -= arr[left]
            left += 1
    return max_sum


def main():
    print(max_sub_array_of_size(3, [2, 1, 5, 1, 3, 2]))
    print(max_sub_array_of_size(2, [2, 3, 4, 1, 5]))


main()
