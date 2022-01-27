# DFS recursive
def dfs(tree):
    if tree is not None:
        print(tree)
        dfs(tree.left)
        dfs(tree.right)


# DFS interactive
def dfs(tree, stack):
    stack.append(tree)
    while len(stack):
        node = stack.pop()
        if node:
            print(node)
            stack.append(node.left)
            stack.append(node.right)


# Binary Search
def binary_search(mylist, target):
    left, right = 0, len(mylist) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if mylist[mid] == target:
            return mid

        elif mylist[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return -1


class ParkRides:

    def solve(self, rides, k):
        def dfs(rides, cur_cost, count):
            if cur_cost + rides[0] > k or self.max_count_ride > len(rides):
                return

            for i in range(len(rides)):
                cur_cost += rides[i]
                count += 1
                self.max_count_ride += 1
                dfs(rides[i:], cur_cost, count)
                self.max_rides = max(self.max_rides, count)
                self.max_count_ride = 0



        self.max_rides = 0
        self.max_count_ride = 0
        dfs(rides, 0, 0)
        return self.max_rides

x = ParkRides()
print(x.solve([3, 4, 8], 10))
print(x.solve([5, 2, 1], 4))