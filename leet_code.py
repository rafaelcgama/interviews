import bisect
import json

from drawtree import draw_level_order  # '{2,#,3,#,4,#,5,#,6}')
from collections import deque, Counter
import math
from itertools import groupby


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Implement Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.is_word = True

    def search(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.is_word

    def startsWith(self, prefix):
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True


class ListNode:
    def __init__(self, item=None, next_=None, random_=None):
        self.item = item
        self.next = next_
        self.random = random_

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
        myset = set()
        while head:
            if head.item not in myset:
                tail.next = head
                tail = tail.next
                myset.add(head.val)

            else:
                tail.next = None

            head = head.next

        return dummy_head.next

        # NO EXTRA MEMORY
        # if not head:
        #     return head
        #
        # dummy_head = tail = ListNode(val=head.val)
        # head = head.next
        #
        # while head:
        #     if tail.val != head.val:
        #         tail.next = ListNode(val=head.val)
        #         tail = tail.next
        #
        #     head = head.next
        #
        # return dummy_head

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
            if letters[mid] == target:
                left = mid
                break
            if letters[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        idx = left if target < letters[left] else left + 1
        return letters[idx % len(letters)]

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

    def climbStairs(self, n: int) -> int:
        # Dynamic Programming
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        p_counter, cur_counter = {}, {}
        for i in range(len(p)):
            p_counter[p[i]] = p_counter.get(p[i], 0) + 1
            cur_counter[s[i]] = cur_counter.get(s[i], 0) + 1

        result = [0] if p_counter == cur_counter else []

        l, r = 0, len(p)
        while r < len(s):
            cur_counter[s[l]] -= 1
            if not cur_counter[s[l]]:
                del cur_counter[s[l]]
            cur_counter[s[r]] = cur_counter.get(s[r], 0) + 1

            l += 1
            r += 1
            if cur_counter == p_counter:
                result.append(l)

        return result

    def findMaxLength(self, nums):
        cur_count = 1
        cum_sum = 0
        max_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cum_sum -= 1
            else:
                cum_sum += 1

            if cum_sum == 0:
                max_length += cur_count
                cur_count = 0

            cur_count += 1

        return max_length

    def removeDuplicates(self, nums):
        previous, count, idx, = nums[0], 1, 1

        while idx <= len(nums) - 1:
            if previous == nums[idx]:
                if count >= 2:
                    nums[idx:] = nums[idx + 1:]
                    continue
                count += 1
            else:
                count = 1

            previous = nums[idx]
            idx += 1

        return nums

    def addDigits(self, num):
        if not num:
            return num
        total = 0
        while True:
            num = total if total else num
            total = 0
            while num:
                total += (num % 10)
                num //= 10

            if int(math.log10(total)) + 1 == 1:
                return total

    def findPairs(self, nums, k):
        look_up = Counter(nums)

        count = 0
        if k == 0:
            for value in look_up.values():
                if value > 1:
                    count += 1
        else:
            for num in nums:
                target = -k + num
                if target in look_up:
                    count += 1

            return count

    def subarraySum(self, nums, k):
        result = 0
        cur_sum = 0
        prefix_sums = {0: 1}

        for num in nums:
            cur_sum += num
            diff = cur_sum - k

            result += prefix_sums.get(diff, 0)
            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1

        return result

    def findMaxLength(self, nums):
        max_length = 0
        lookup = {}
        count = 0
        for i in range(len(nums)):
            current = nums[i]
            if current == 0:
                count -= 1  # decrement our count if our current element is 0
            else:
                # increment our count if current element is 1
                count += 1

            if count == 0:
                # if count is 0, we have a new subarray with length+1
                max_length = i + 1
            if count in lookup:
                max_length = max(max_length, i - lookup[count])
            else:
                lookup[count] = i

        return max_length

    def permute(self, nums):
        result = []

        # base case
        if len(nums) == 1:
            return [list(nums)]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)

        return result

    def subsets(self, nums):
        result = []

        def dfs(i, subset):
            if i >= len(nums):
                result.append(list(subset))
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1, subset)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1, subset)

        dfs(0, [])
        return result

        # def backtrack(first=0, curr=[]):
        #     if len(curr) == k:
        #         output.append(curr[:])
        #         return
        #
        #     for i in range(first, len(nums)):
        #         curr.append((nums[i]))
        #
        #         backtrack(i + 1, curr)
        #         curr.pop()
        #
        # output = []
        # for k in range(len(nums) + 1):
        #     backtrack()
        #
        # return output

    def maxDepth(self, root):
        self.max_level = 0

        def dfs(node, level=0):
            if not node:
                self.max_level = max(self.max_level, level)
            else:
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)

        dfs(root, 0)

        return self.max_level

    def removeCoveredIntervals(self, intervals):
        # idx_removed = set()
        # for i in range(len(intervals)):
        #     a, b = intervals[i]
        #     if i in idx_removed:
        #         continue
        #     for j in range(i + 1, len(intervals)):
        #         c, d = intervals[j]
        #         if j in idx_removed:
        #             continue
        #
        #         if c <= a and d >= b:
        #             idx_removed.add(i)
        #             break
        #
        #         elif a <= c and b >= d:
        #             idx_removed.add(j)
        #
        # return len(intervals) - len(idx_removed)

        for a in reversed(list(intervals)):
            for b in reversed(intervals):
                if a != b:
                    if (b[0] <= a[0]) and (a[1] <= b[1]):
                        intervals.pop()
                        break

        return len(intervals)

    def removeKdigits(self, num, k):
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()

            stack.append(c)

        # If not all k numbers are removed
        stack = stack[:len(stack) - k]
        result = ''.join(stack)

        while len(result) and result[0] == '0':
            result = result[1:]

        return result if result else '0'

    def titleToNumber(self, columnTitle):
        self.total = 0

        def recursion(i=0, j=len(columnTitle) - 1):
            if i == len(columnTitle):
                return

            c_num = ord(columnTitle[j]) - 64
            self.total += (c_num * (26 ** i))

            recursion(i + 1, j - 1)

        recursion()

        return self.total

    def combinationSum(self, candidates, target):
        res = []

        def dfs(i=0, cur=[], total=0):
            if total == target:
                res.append(cur[:])
                return

            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs()
        return res

    def cloneGraph(self, node):
        node_dict = {}

        def dfs(node):
            if node in node_dict:
                return node_dict[node]

            copy = Node(node.val)
            node_dict[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None

    def compareVersion(self, version1: str, version2: str) -> int:
        def normalize_size(version1, version2):
            extra_zero = len(version1) - len(version2)
            if extra_zero != 0:
                update_list = version1 if extra_zero < 0 else version2
                update_list.extend([0] * abs(extra_zero))

            return version1, version2

        new_version1, new_version2 = normalize_size(version1.split("."), version2.split("."))

        for a, b in zip(new_version1, new_version2):
            if int(a) > int(b):
                return 1

            elif int(a) < int(b):
                return -1

            elif int(a) == int(b):
                continue

        return 0

    def widthOfBinaryTree(self, root):
        level_dict = {}

        def dfs(node, level=0, idx=1):
            if node:
                level_dict[level] = level_dict.get(level, list()) + [idx]
                dfs(node.left, level + 1, idx=(idx * 2) - 1)
                dfs(node.right, level + 1, idx=idx * 2)

        dfs(root)

        return max(map(lambda x: x[-1] - x[0] + 1, level_dict.values()))

    def isSubsequence(self, s, t):
        idx = 0
        for c in s:
            idx_t = t.find(c)
            if idx_t >= idx:
                t = t[idx_t + 1:]
                idx = 0

            else:
                return False

        return True

    def minDepth(self, root):
        # # DFS
        # def dfs(root, level=1):
        #     if not root.left and not root.right:
        #         self.min_ = min(self.min_, level) if self.min_ else level
        #         return
        #
        #     if root:
        #         dfs(root.left, level + 1)
        #         dfs(root.right, level + 1)
        #
        # self.min_ = 0
        # dfs(root)
        #
        # return self.min_

        # BFS
        if not root:
            return 0

        queue = deque([(root, 1)])
        while queue:
            node, num = queue.popleft()
            if not node.left and not node.right:
                return num

            if node.left:
                queue.append((node.left, num + 1))

            if node.right:
                queue.append((node.right, num + 1))

    def isSameTree(self, p, q):
        # # DFS
        # def dfs(p, q):
        #     if not p and not q:
        #         return
        #
        #     if (p and not q) or (not p and q) or p.val != q.val:
        #         return False
        #
        #     left = dfs(p.left, q.left)
        #     if isinstance(left, bool):
        #         return left
        #     right = dfs(p.right, q.right)
        #     if isinstance(right, bool):
        #         return right
        #
        # is_same = dfs(p, q)
        # if isinstance(is_same, bool):
        #     return is_same
        #
        # return True

        queue = deque([(p, q)])
        while queue:
            p, q = queue.popleft()
            if not p and not q:
                continue

            elif (p and not q) or (not p and q) or p.val != q.val:
                return False

            queue.append((p.left, q.left))
            queue.append((p.right, q.right))

        return True

    def hasPathSum(self, root, targetSum):
        def dfs(root, cur_sum=0):
            if not root:
                return False

            cur_sum += root.val
            if not root.left and not root.right:
                return cur_sum == targetSum

            return (dfs(root.left, cur_sum) or dfs(root.right, cur_sum))

        return dfs(root)

    def numberOfArithmeticSlices(self, nums):
        if len(nums) < 3:
            return 0

        total = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[j + 1] - nums[j]) == (nums[j] - nums[j - 1]):
                    total += 1

                else:
                    break

        return total

    def champagneTower(self, poured, query_row, query_glass):
        glass_stack = [[0 for _ in range(x)] for x in range(1, query_row + 2)]
        glass_stack[0][0] = poured

        for i in range(query_row):
            for j in range(len(glass_stack[i])):
                temp = (glass_stack[i][j] - 1) / 2
                if temp > 0:
                    glass_stack[i + 1][j] += temp
                    glass_stack[i + 1][j + 1] += temp

        return glass_stack[query_row][query_glass] if glass_stack[query_row][query_glass] <= 1 else 1

    def isValid(self, s: str) -> bool:
        stack = []
        opposite_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for p in s:
            if p in opposite_map.values():
                stack.append(p)

            elif stack and opposite_map[p] == stack[-1]:
                stack.pop()

            else:
                return False

        return True if not len(stack) else False

    def minRemoveToMakeValid(self, s: str) -> str:
        opposite_map = {
            ')': '('
        }
        stack = []
        for i, c in enumerate(s):
            if stack and stack[-1][0] == opposite_map.get(c, False):
                stack.pop()

            elif c == "(" or c == ")":
                stack.append((c, i))

        for c, idx in reversed(stack):
            s = s[:idx] + s[idx + 1:]

        return s

    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c

        return "/" + "/".join(stack)

    def addTwoNumbers(self, l1, l2):
        def reverse_list(head):
            number = 0
            i = 0
            while head:
                number += (head.item * 10 ** i)
                i += 1
                head = head.next

            return number

        def convert_linked_list(num):
            if not num:
                return ListNode(val=num)

            dummy_head = tail = ListNode()
            while num:
                tail.next = ListNode(item=num % 10)
                tail = tail.next
                num //= 10

            return dummy_head.next

        num1, num2 = reverse_list(l1), reverse_list(l2)

        return convert_linked_list(num1 + num2)

    def rotateRight(self, head, k):
        if not head:
            return head

        tail = head
        length = 1
        while tail.next:
            length += 1
            tail = tail.next

        idx = k % length
        if idx == 0:
            return head

        curr = head
        for _ in range(length - idx - 1):
            curr = curr.next

        new_dummy = curr.next
        curr.next = None
        tail.next = head

        return new_dummy

    def validateStackSequences(self, pushed, popped):
        i = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and i < len(popped) and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return not stack

    def scoreOfParentheses(self, s: str) -> int:
        total = 0
        stack = []
        for c in s:
            if "(" == c:
                stack.append(total)
                total = 0

            else:
                total = stack.pop() + max(total * 2, 1)

        return total

    def removeDuplicateLetters(self, s: str) -> str:
        look_up = {}
        for i in range(len(s)):
            look_up[s[i]] = i

        stack = []

        for i in range(len(s)):
            if s[i] in stack:  # letter cannot be repeated
                continue

            while stack and stack[-1] > s[i] and look_up[stack[-1]] > i:
                stack.pop()

            stack.append(s[i])

        return ''.join(stack)

    def copyRandomList(self, head):
        node_map = {}

        cur = head
        while cur:
            copy = ListNode(item=cur.item)
            node_map[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = node_map[cur]
            copy.next = node_map[cur.next]
            copy.random = node_map[copy.random]
            cur = cur.next

        return node_map[head]

    def getSmallestString(self, n: int, k: int) -> str:
        result = ["a"] * n

        k -= n
        i = n - 1

        while k > 0:
            result[i] = chr(ord("a") + min(25, k))
            i -= 1
            k -= 25

        return "".join(result)

    def numRescueBoats(self, people, limit: int) -> int:
        people.sort()

        result = 0
        left, right = 0, len(people) - 1
        while left <= right:
            remainder = limit - people[right]
            right -= 1
            result += 1
            if left <= right and remainder >= people[left]:
                left += 1

        return result

    def searchMatrix(self, matrix, target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return target in matrix[mid]

            elif matrix[mid][-1] < target:
                left = mid + 1

            else:
                right = mid - 1


def to_binary_tree(items):
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


if __name__ == '__main__':
    x = Solution()

    node1 = ListNode(item=7)
    node2 = ListNode(item=13)
    node3 = ListNode(item=11)
    node4 = ListNode(item=10)
    node5 = ListNode(item=1)

    node1.next = node2
    node1.random = None
    node2.next = node3
    node2.random = node1
    node3.next = node4
    node3.random = node5
    node4.next = node5
    node4.random = node3
    node5.random = node1

    # print(x.getSmallestString(node1))
    print(x.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
