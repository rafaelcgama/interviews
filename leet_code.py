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

class ListNode:
    def __init__(self, x=None, next_=None):
        self.item = x
        self.next = next_

    def create_linked_list(self, mylist):
        head = tail = ListNode()
        for item in mylist:
            tail.next = ListNode(x=item)
            tail = tail.next

        return head.next

    def print_linked_list(self, head):
        tail = head
        while tail:
            print(tail.item)
            tail = tail.next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def twoSum(self, nums, target):
        mydict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in mydict:
                mydict[num] = i

            elif (diff in nums) and mydict[diff] != i:
                return [i, mydict[diff]]

    def reverse(self, x):
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

    def maxSubArray(self, nums):
        ans = nums[0]
        curr_sum = nums[0]
        for num in nums[1:]:
            if curr_sum + num > num:
                curr_sum += num

            elif num > curr_sum:
                curr_sum = num

            ans = max(ans, curr_sum)

        return ans

    def hasCycle(self, head):
        tail_fast = tail_slow = head
        while tail_slow and tail_slow.next:
            tail_slow = tail_slow.next
            tail_fast = tail_fast.next.next
            if tail_fast:
                if tail_fast is tail_slow:
                    return True
            else:
                return False

    def middleNode(self, head):
        fast_node = slow_node = head

        while fast_node and fast_node.next:
            fast_node = fast_node.next.next
            slow_node = slow_node.next

        return slow_node

    def removeElements(self, head, val):
        cleaned = tail = ListNode()
        while head:
            if head.item != val:
                tail.next = head
                tail = tail.next

            else:
                tail.next = None

            head = head.next

        return cleaned.next

    def deleteDuplicates(self, head):
        dummy_head = tail = ListNode()
        mydict = {}
        while head:
            mydict[head.item] = mydict.get(head.item, False)
            if not mydict[head.item]:
                tail.next = head
                tail = tail.next
                mydict[head.item] = True

            else:
                tail.next = None

            head = head.next

        return dummy_head.next

    def reverseList(self, head):
        previous = None
        while head:
            next_node = head.next
            head.next = previous
            previous = head
            head = next_node

        return previous

    def mergeTwoLists(self, l1, l2):
        dummy_head = tail = ListNode()
        while l1 and l2:
            if l1.item < l2.item:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next

            tail = tail.next

        tail.next = l1 or l2

        return dummy_head.next

    def nextGreatestLetter(self, letters, target):
        # i = bisect_right(letters, target)
        # return letters[0] if i > len(letters) - 1 else letters[i]
        left, right = 0, len(letters) - 1
        while left < right:
            mid = left + (right - left) // 2
            if letters[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        idx = left if target < letters[left] else left + 1
        return letters[0] if idx > (len(letters) - 1) else letters[idx]

    def peakIndexInMountainArray(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + (right - left)) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1

            else:
                right = mid

        return left

    def averageOfLevels(self, root):
        from statistics import mean

        values = {}

        def dfs(root, level=0):
            if root:
                values[level] = values.get(level, list()) + [root.val]
                dfs(root.left, level + 1)
                dfs(root.right, level + 1)

        dfs(root)

        return [mean(value) for value in values.values()]

    def rob(self, nums):
        pass

    def grid_paths(self, n, m):
        if n == 1 or m == 1:
            return 1
        else:
            left = self.grid_paths(n, m - 1)
            right = self.grid_paths(n - 1, m)
            return left + right


if __name__ == '__main__':
    x = Solution()
    # l1 = ListNode().create_linked_list([1, 2, 4])
    # l2 = ListNode().create_linked_list([1, 3, 4])

    binary_tree = TreeNode(3, TreeNode(9), TreeNode(20))
    binary_tree.right.left = TreeNode(15)
    binary_tree.right.right = TreeNode(7)

    # print(x.averageOfLevels(binary_tree))

    # print(x.rob([2, 1, 1, 2]))

    print(x.grid_paths(3, 3))
