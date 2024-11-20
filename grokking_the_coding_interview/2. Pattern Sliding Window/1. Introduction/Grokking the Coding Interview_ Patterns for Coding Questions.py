from time import time

# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5


# Brute Force
def find_avg_subarrays1(k, arr):
    """
    Time Complexity: O(n * k)
    Space Complexity: O(n)
    """
    res = []
    for i in range(len(arr) - k + 1):
        sum_ = 0.0
        for j in range(i, i + k):
            sum_ += arr[j]
        res.append(sum_ / k)

    return res


# Sliding Window
def find_avg_subarrays2(k, arr):
    res = []
    l, r = 0, k

    mysum = sum(arr[0:k])
    res.append(mysum / k)

    while l < k - 1:
        mysum -= arr[l]
        mysum += arr[r]
        l += 1
        r += 1
        res.append(mysum / k)

    return res


def find_avg_subarrays3(k, arr):
    res = []
    window_sum, window_start = 0.0, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k - 1:
            res.append(window_sum / k)
            window_sum -= arr[window_start]
            window_start += 1

    return res


if __name__ == "__main__":
    start = 0
    print(find_avg_subarrays2(k, arr))
    end = time()
    print(end - start)
    print("")
    start = 0
    print(find_avg_subarrays3(k, arr))
    end = time()
    print(end - start)