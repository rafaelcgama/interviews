# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         #faz lookup table
#         lookup = {}
#         for idx, n in enumerate(nums):
#             lookup[n] = idx

#         #procura complemento
#         for idx, n in enumerate(nums):

#             complemento = target - n
#             if complemento in lookup:
#                 resp  = lookup[complemento]
#                 if resp != idx:
#                     return [resp, idx]

class Solution:

    def twoSum(self, nums, target):
        mydict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in mydict:
                mydict[num] = i

            elif (diff in nums) and mydict[diff] != i:
                return [i, mydict[diff]]

    def reverse(self, x: int) -> int:
        new_number = 0
        is_negative = True if x < 0 else False
        x = abs(x)
        while x:
            new_number = (10 * new_number) + (x % 10)
            x //= 10

        new_number = new_number * -1 if is_negative else new_number

        return new_number if (-2 ** 31 <= new_number <= (2 ** 31 - 1)) else 0

    def romanToInt(self, s):
        num_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        special_num_map = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        number = 0
        skip = False
        for i, c in enumerate(s):
            if i < len(s) - 1:
                if skip:
                    skip = False
                    continue

                elif s[i: i + 2] in special_num_map:
                    number += special_num_map[s[i: i + 2]]
                    skip = True

                else:
                    number += num_map[c]

            elif not skip:
                number += num_map[c]

        return number


if __name__ == '__main__':
    x = Solution()
