from leet_code import ListNode


#### RECURSIVE FUNCTIONS ####

### STRINGS ###
def reverse_string(mystring):
    if not mystring:
        return ""

    return reverse_string(mystring[1:]) + mystring[0]


def is_palindrome(mystring):
    if (not len(mystring)) or (len(mystring) == 1):
        return True

    if mystring[0] == mystring[len(mystring) - 1]:
        return is_palindrome(mystring[1: len(mystring) - 1])

    return False


### NUMBERS ###
def decimal_to_binary(mydecimal, result):
    if not mydecimal:
        return result

    result = str(mydecimal % 2) + result

    return decimal_to_binary(mydecimal // 2, result)


def recursiveSummation(number):
    if number <= 1:
        return number

    return number + recursiveSummation(number - 1)


### DIVIDE AND CONQUER ###

## BINARY SEARCH ##
def binary_search(A, left, right, target):
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if target == A[mid]:
        return mid

    if target < A[mid]:
        return binary_search(A, left, mid - 1, target)

    return binary_search(A, mid + 1, right, target)


## FIBONACCI (Non-Optimized) ##
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


## MERGE SORT ##


## LINKED LIST REVERSAL ##'
def reverse_linked_list(head):
    if not head or not head.next:
        return head

    p = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None

    return p


def sorted_merge(l1, l2):
    if not l1:
        return l2

    if not l2:
        return l1

    if l1.item < l2.item:
        l1.next = sorted_merge(l1.next, l2)
        return l1
    else:
        l2.next = sorted_merge(l1, l2.next)
        return l2


if __name__ == "__main__":
    linked_list = ListNode()
    l1 = linked_list.create_linked_list([2, 5, 8])
    l2 = linked_list.create_linked_list([1, 3, 4, 6, 8])
    merged_linked_list = sorted_merge(l1, l2)
    linked_list.print_linked_list(merged_linked_list)
