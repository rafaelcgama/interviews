import bisect
from collections import deque
import math
from itertools import groupby


class ListNode:
    def __init__(self, item=None, next_=None):
        self.item = item
        self.next = next_

    def create_linked_list(self, mylist):
        head = tail = ListNode()
        for item in mylist:
            tail.next = ListNode(item=item)
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

    def insertionSortList(self, head):
        def insertInSortedList(node, head):
            """
            sub problem:
                - place given node in correct place of the sorted list head
            """
            cur = head.next
            prev = head
            while cur and cur.item < node.item:
                prev = cur
                cur = cur.next
            prev.next = node
            node.next = cur

        ################ Start of the solution #############
        sortedListHead = ListNode()
        cur = head

        while cur:
            # Important to save the next ptr here because insertInSortedList will modify cur.next
            nextPos = cur.next
            insertInSortedList(cur, sortedListHead)
            # Reset the next position so our iteration works as usual
            cur = nextPos

        return sortedListHead.next

    def numPairsDivisibleBy60(self, time):
        """
        the trick is that if ((a % 60) + (b % 60)) % 60 == 0 then (a + b) % 60 will also be 0.
        :param time:
        :return:
        """
        lookup = {}
        total = 0
        for num in time:
            rem = num % 60
            lookup_num = 60 - rem if rem else rem  # If rem is 0 then the lookup number has to be zero for the 60 % 60 = 0 case
            if lookup_num in lookup:
                total += lookup[lookup_num]
            lookup[rem] = lookup.get(rem, 0) + 1

        return total

    def findJudge(self, n, trust):
        if n == 1 and not trust:
            return -1
        all_ppl = set(list(range(1, n + 1)))
        ppl_who_trust = set()
        ppl_trusted = {}
        for person in trust:
            ppl_who_trust.add(person[0])
            ppl_trusted[person[1]] = ppl_trusted.get(person[1], 0) + 1

        judge = list(all_ppl - ppl_who_trust)

        if len(judge) == 1 and ppl_trusted[judge[0]] == n - 1:
            return judge[0]

        else:
            return -1

        # if not trust and n == 1:
        #     return 1
        #
        # cands = [0] * (n + 1)
        # for elem1, elem2 in trust:
        #     cands[elem2] += 1
        #     cands[elem1] -= 1
        #
        # return cands.index(n - 1) if n - 1 in cands else -1

    def carPooling(self, trips, capacity):
        road_east = [0]
        for trip in trips:
            # Add units to the road
            add_miles = trip[2] - (len(road_east) - 1)
            if add_miles > 0:
                road_east += (add_miles * [0])

            # Add new capacity to the units in the road
            for i in range(trip[1], trip[2] + 1):
                road_east[i] += trip[0]

            # Check if any unit is above capacity
            if max(road_east) > capacity:
                return False

        return True

    def countPrimes(self, n):
        def is_prime(num):
            for i in range(3, num + 1, 2):
                if num / i == 1 and num == i:
                    return True

            return False

        if n == 0 or n == 1:
            return 0

        elif n == 2:
            return 1

        target = 3
        primes = 1  # includes 2
        while target <= n:
            if is_prime(target):
                primes += 1

            target += 2

        return primes

    def maxDistToClosest(self, seats):
        grouped = [(a, len(list(b))) for a, b in groupby(seats)]
        right = grouped[0][1] if not grouped[0][0] else 0
        left = grouped[len(grouped) - 1][1] if not grouped[len(grouped) - 1][0] else 0

        middle = 0
        for a, b in grouped[1:-1]:
            if a == 0 and b > middle:
                middle = b

        return max(right, left, math.ceil(middle / 2))

    def sumRootToLeaf(self, root):
        def dfs(root, value=''):
            if root:
                value += str(root.val)
                if not (root.left or root.right):
                    self.total += int(value, 2)
                    return
                dfs(root.left, value)
                dfs(root.right, value)

        self.total = 0
        dfs(root)

        return self.total

    def validMountainArray(self, arr):
        if len(arr) < 3 or arr[0] >= arr[1] or arr[len(arr) - 2] <= arr[len(arr) - 1]:
            return False
        is_increasing = True
        previous = arr[0]
        for num in arr[1:]:
            if (is_increasing and num > previous) or (not is_increasing and num < previous):
                pass

            elif num < previous:
                is_increasing = False

            else:
                return False

            previous = num

        return True

    def sequentialDigits(self, low, high):
        result = []

        # scan all possible first digit
        for first_digit in range(1, 10):

            cur_num = first_digit

            # growing based on first digit
            for next_digit in range(first_digit + 1, 10):

                # growing with sequential digit
                cur_num = cur_num * 10 + next_digit

                if low <= cur_num <= high:
                    # check current number is in range or not
                    result.append(cur_num)

        return sorted(result)

    def canCompleteCircuit(self, gas, cost):
        ## Brute force
        # for i in range(len(gas)):
        #     tank = gas[i]
        #     start = i
        #     while True:
        #         tank -= cost[start % len(gas)]
        #         if tank >= 0:
        #             start += 1
        #             if start % len(gas) == i:
        #                 return start % len(gas)
        #             tank += gas[start % len(gas)]
        #
        #         else:
        #             break
        #
        # return -1

        # if sum(gas) < sum(cost):
        #     return -1
        #
        # total = 0
        # start = 0
        # for i in range(len(gas)):
        #     total += (gas[i] - cost[i])
        #
        #     if total < 0:
        #         total = 0
        #         start = i + 1
        #
        # return start
        if sum(gas) < sum(cost):
            return -1
        tank = [0] * len(gas)  # If starting from station 0, tank after arriving at each station
        for i in range(1, len(gas)):
            tank[i] = tank[i - 1] + gas[i - 1] - cost[i - 1]

        return tank.index(min(tank))  # the smallest negative number reflects the largest gap, we start from it greedily

    def minEatingSpeed(self, piles, h):
        # # Brute force
        # cur_hours = 0
        # for i in range(1, max(piles) + 1):
        #     curr_piles = list(piles)
        #     j = 0
        #     while j < len(curr_piles):
        #         if i >= curr_piles[j]:
        #             curr_piles[j] = 0
        #             j += 1
        #         else:
        #             curr_piles[j] = curr_piles[j] - i
        #
        #         cur_hours += 1
        #         if cur_hours > h:
        #             cur_hours = 0
        #             break
        #
        #     if cur_hours:
        #         return i

        left, right = 0, max(piles)
        min_rate = right
        while left < right:
            mid = left + (right - left) // 2
            cur_hours = sum(map(lambda x: math.ceil(x / mid), piles))
            if cur_hours <= h:
                min_rate = min(min_rate, mid)
                right = mid - 1
            else:
                left = mid + 1

        return min_rate

    def getAllElements(self, root1, root2):
        def dfs(root, mylist):
            if root:
                mylist.append(root.val)
                dfs(root.left, mylist)
                dfs(root.right, mylist)

            return mylist

        mylist1 = dfs(root1, [])
        mylist2 = dfs(root2, [])

        return sorted(mylist1 + mylist2)

    def detectCycle(self, head):
        tail_fast = tail_slow = head
        while tail_fast and tail_fast.next:
            tail_slow = tail_slow.next
            tail_fast = tail_fast.next.next
            if tail_fast is tail_slow:
                break
        else:
            return None

        tail = head
        while tail_fast:
            if tail is tail_fast:
                return tail
            tail = tail.next
            tail_fast = tail_fast.next


if __name__ == '__main__':
    x = Solution()
    l1 = ListNode().create_linked_list([5, 6, 3, 4, 2, 7])
    # l2 = ListNode().create_linked_list([1, 3, 4])

    # print(x.rob([2, 1, 1, 2]))

    # print(x.insertionSortList(l1))

    # tree = TreeNode(val=1)
    # tree.left = TreeNode(val=0)
    # tree.left.left = TreeNode(val=0)
    # tree.left.right = TreeNode(val=1)
    # tree.right = TreeNode(val=1)
    # tree.right.left = TreeNode(val=0)
    # tree.right.right = TreeNode(val=1)

    # print(x.sumRootToLeaf(tree))

    node1 = ListNode(item=3)
    node2 = ListNode(item=2)
    node3 = ListNode(item=0)
    node4 = ListNode(item=-4, next_=node2)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    print(x.detectCycle(node1))
