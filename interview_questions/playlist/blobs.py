# Example grid containing 3 blobs (labels are for ease of reading only)
#
grid = [
    "00010", # | | | |A| |
    "01101", # | |B|B| |B|
    "00111", # | | |B|B|B|
    "11010", # |C|C| |B| |
    "11000"  # |C|C| | | |
]
#
# def solution(grid, minimumSize):
#     n = 0
#
#     visits = set()
#
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if f(grid, i, j, visits):
#                 n += 1
#     return n
#
# def f(grid, i, j, visits):
#     if i <= 0 or i >= len(grid) or j <= 0 or j >= len(grid[0]):
#         return False
#
#     f(grid, i - 1, j,     visits)
#     f(grid, i + 1, j,     visits)
#     f(grid, i,     j - 1, visits)
#     f(grid, i,     j + 1, visits)
#
#     visits.add((i,j))
#
#     return True

def solution(grid):
    if not grid:
        return 0
    n = 0
    visits = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1' and (i, j) not in visits:
                f(grid, i, j, visits)
                n += 1
    return n

def f(grid, i, j, visits):
    # Check if it is outside the grid
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return
    if (i, j) in visits or grid[i][j] != '1':
        return
    visits.add((i, j))

    f(grid, i - 1, j, visits)
    f(grid, i + 1, j, visits)
    f(grid, i, j - 1, visits)
    f(grid, i, j + 1, visits)

print(solution(grid))