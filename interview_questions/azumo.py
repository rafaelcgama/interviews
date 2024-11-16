"""
You are a professional boxer planning to make the most money out of your boxing career. Your compensation for each fight

will vary depending on your opponent and the venue in which the fight will take place. However, since boxing is

extremely demanding, you also care about your health. Therefore, you cannot play in two consecutive matches.

Your agent has written a function max_earnings that returns the maximum you can earn without playing in two

consecutive fights. The function takes an array of integers earnings_per_fight representing the amount you’ll earn for

each fight.

You notice that there are some issues with the function. You have to debug the function so you can accurately determine

how much you can earn.

If the max earning is negative, return 0 since you would choose to not participate in any fights.

Note: the initial code in the editor uses tabs for indentation. Don’t mix it with spaces.

Examples:

Input: earnings_per_fight = [1, 2, 5, 2] Output: 6 You'll fight the 1st and 3rd fight, giving you a total earning of 6.

Input: earnings_per_fight = [6, 2, 5, 94] Output: 100 You'll fight the 1st and 4th fight, giving you a total earning of 100.
"""


# FIX the following function
def max_earnings(earnings_per_fight):
    num_fights = len(earnings_per_fight)
    if num_fights == 0:
        return 0
    if num_fights == 1:
        return 0

    dp = [0] * num_fights
    dp[0] = earnings_per_fight[0]
    dp[1] = earnings_per_fight[1]

    for i in range(num_fights):
        dp[i] = max(earnings_per_fight[i] + dp[i - 1], dp[i])

    return dp[num_fights]


# Answer
def max_earnings(earnings_per_fight):
    num_fights = len(earnings_per_fight)

    # Edge case: If there are no fights, return 0
    if num_fights == 0:
        return 0

    # Edge case: If there's only one fight, return its earnings (or 0 if negative)
    if num_fights == 1:
        return max(earnings_per_fight[0], 0)

    # Initialize a DP array to store the max earnings up to each fight
    dp = [0] * num_fights

    # Base cases:
    dp[0] = max(earnings_per_fight[0], 0)  # Fight 0 or skip if negative
    dp[1] = max(earnings_per_fight[1], dp[0])  # Fight 1 or skip if negative

    # Fill the DP table
    for i in range(2, num_fights):
        dp[i] = max(earnings_per_fight[i] + dp[i - 2], dp[i - 1])

    # Final maximum earnings
    max_earning = dp[-1]

    # If the maximum earnings are negative, return 0
    return max(max_earning, 0)


# Example Usage:
# print(max_earnings([1, 2, 5, 2]))  # Output: 6
# print(max_earnings([6, 2, 5, 94]))  # Output: 100


def max_nonconsecutive_sum(nums):
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]

    # Create an array to store the maximum sum at each index
    max_sum = [0] * len(nums)
    max_sum[0] = nums[0]

    if len(nums) > 1:
        max_sum[1] = max(nums[0], nums[1])

    # Fill the array with the maximum sum possible at each index
    for i in range(2, len(nums)):
        max_sum[i] = max(max_sum[i - 1], max_sum[i - 2] + nums[i])

    # The last element in max_sum will contain the maximum sum possible without consecutive sums
    return max_sum[-1]


# Recursive
def max_nonconsecutive_sum_recursive(nums):
    n = len(nums)

    def dfs(i):
        if i == 0:
            return 0
        if i == 1:
            return max(nums[0], nums[i])

        return max(nums[i] + dfs(i - 2), dfs(i - 1))

    return dfs(n - 1)


# Recursive Memoized
def max_nonconsecutive_sum_recursive_memo(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])

    memo = {0: nums[0], 1: max(nums[0], nums[1])}

    def dfs(i):
        if i in memo:
            return memo[i]
        else:
            memo[i] = max(nums[i] + dfs(i - 2), dfs(i - 1))
            return memo[i]

    return dfs(n - 1)


# Example usage
nums = [1, 3, 6, 2]
result = max_non_consecutive_sum(nums)
print(result)  # Output: 7
