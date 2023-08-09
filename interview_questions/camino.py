import unittest

# func (+ integer)

# odd: multiply 3 + 1

# even: //2

input = 3
output = [3, 10, 5, 16, 8, 4, 2, 1]


def reduce_to_one(num):
    assert num > 0, "input not valid"
    output = [num]
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = (3 * num) + 1

        output.append(num)

    return output


# class Test(unittest.TestCase):
#     def test_output1(self):
#         self.assertEqual(reduce_to_one(3), [3, 10, 5, 16, 8, 4, 2, 1])
#
#     def test_assertion(self):
#         with self.assertRaises(AssertionError):
#             reduce_to_one(-1)


print(reduce_to_one(7))
