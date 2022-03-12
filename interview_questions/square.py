import unittest


# Intervals

# -----3-------6------ base for comparison
# ----------4-----7--- case 1
# --1-----4----------- case 2
# ---2 -----------7--- case 3
# --------4--5-------- case 4
# -------------6--7--- case 5 (matching times)
# ---1--3------------- case 6 (matching times)
# 1-2----------------- case 7
# ----------------7-8- case 8

def is_overlap(interval_base, new_interval):
    return not (interval_base[0] > new_interval[1] or interval_base[1] < new_interval[0])


# class TestOverlapingIntervals(unittest.TestCase):
#
#     def test_case1(self):
#         interval_base, new_interval = [3, 6], [4, 7]
#         self.assertTrue(is_overlap(interval_base, new_interval))
#
#     def test_case2(self):
#         interval_base, new_interval = [3, 6], [1, 4]
#         self.assertTrue(is_overlap(interval_base, new_interval))
#
#     def test_case3(self):
#         interval_base, new_interval = [3, 6], [2, 7]
#         self.assertTrue(is_overlap(interval_base, new_interval))
#
#     def test_case4(self):
#         interval_base, new_interval = [3, 6], [4, 5]
#         self.assertTrue(is_overlap(interval_base, new_interval))
#
#     def test_case5(self):
#         interval_base, new_interval = [3, 6], [3, 7]
#         self.assertTrue(is_overlap(interval_base, new_interval))
#
#     def test_case6(self):
#         interval_base, new_interval = [3, 6], [1, 3]
#         self.assertTrue(is_overlap(interval_base, new_interval))


# Merge intervals

intervals = [[1, 3], [2, 6], [15, 18], [8, 10]]


def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    new_schedule = [intervals[0]]
    for interval in intervals[1:]:
        if is_overlap(new_schedule[-1], interval):
            new_schedule[-1][1] = max(interval[1], new_schedule[-1][1])
        else:
            new_schedule.append(interval)

    return new_schedule
