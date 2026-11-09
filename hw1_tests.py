"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        # Upper- and lower-case vowels should both be counted.
        self.assertEqual(hw1.vowel_count("hEllO WOrld"), 3)
 
    def test_vowel_count_empty_string(self):
        # An empty string has no vowels.
        self.assertEqual(hw1.vowel_count(""), 0)
 
    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        # Only the lists of length 2 are kept, in order.
        items = [[1, 2], [3], [4, 5, 6], [7, 8], []]
        self.assertEqual(hw1.short_lists(items), [[1, 2], [7, 8]])
 
    def test_short_lists_no_matching_lengths(self):
        # No list has length 2, so the result is empty.
        items = [[1], [2, 3, 4], []]
        self.assertEqual(hw1.short_lists(items), [])
 
    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        # Reversed pairs get flipped; already-ascending pairs stay the same.
        items = [[5, 2], [1, 9], [8, 3]]
        self.assertEqual(hw1.ascending_pairs(items), [[2, 5], [1, 9], [3, 8]])
 
    def test_ascending_pairs_other_lengths_unchanged(self):
        # Lists that are not length 2 are left exactly as they were.
        items = [[3, 2, 1], [7], [4, 1], []]
        self.assertEqual(hw1.ascending_pairs(items), [[3, 2, 1], [7], [1, 4], []])
 
    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        # 2.30 + 1.45 = 3.75, no carry needed.
        result = hw1.add_prices(data.Price(2, 30), data.Price(1, 45))
        self.assertEqual(result.dollars, 3)
        self.assertEqual(result.cents, 75)
 
    def test_add_prices_with_cents_carry(self):
        # 4.80 + 2.65 = 7.45, so 145 cents carries into one extra dollar.
        result = hw1.add_prices(data.Price(4, 80), data.Price(2, 65))
        self.assertEqual(result.dollars, 7)
        self.assertEqual(result.cents, 45)
 
    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        # Width 4, height 3 -> area 12.
        rect = data.Rectangle(data.Point(0, 3), data.Point(4, 0))
        self.assertAlmostEqual(hw1.rectangle_area(rect), 12.0)
 
    def test_rectangle_area_negative_coordinates(self):
        # Corners in negative space: width 3, height 2 -> area 6.
        rect = data.Rectangle(data.Point(-5, -1), data.Point(-2, -3))
        self.assertAlmostEqual(hw1.rectangle_area(rect), 6.0)
 
    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        # Returns every book the author wrote or co-wrote, in order.
        b1 = data.Book(["Ann Lee"], "Python Basics")
        b2 = data.Book(["Bo Chen", "Ann Lee"], "Data Structures")
        b3 = data.Book(["Cal Diaz"], "Algorithms")
        self.assertEqual(hw1.books_by_author("Ann Lee", [b1, b2, b3]), [b1, b2])
 
    def test_books_by_author_no_matches(self):
        # Author not found anywhere -> empty list.
        b1 = data.Book(["Ann Lee"], "Python Basics")
        b2 = data.Book(["Bo Chen"], "Data Structures")
        self.assertEqual(hw1.books_by_author("Dee Evans", [b1, b2]), [])
 
    # Part 7: circle_bound
    def test_circle_bound_square(self):
        # 2x2 square centered at (1, 1): radius is half the diagonal, sqrt(2).
        rect = data.Rectangle(data.Point(0, 2), data.Point(2, 0))
        circle = hw1.circle_bound(rect)
        self.assertAlmostEqual(circle.center.x, 1.0)
        self.assertAlmostEqual(circle.center.y, 1.0)
        self.assertAlmostEqual(circle.radius, 2 ** 0.5)
 
    def test_circle_bound_non_square_rectangle(self):
        # 6x8 rectangle: center (3, 4), diagonal 10, so radius 5.
        rect = data.Rectangle(data.Point(0, 8), data.Point(6, 0))
        circle = hw1.circle_bound(rect)
        self.assertAlmostEqual(circle.center.x, 3.0)
        self.assertAlmostEqual(circle.center.y, 4.0)
        self.assertAlmostEqual(circle.radius, 5.0)
 
    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        # Average pay is 20.0, so everyone except Ben is below it.
        employees = [
            data.Employee("Ana", "Cashier", 15.0),
            data.Employee("Ben", "Manager", 30.0),
            data.Employee("Cy", "Stocker", 18.0),
            data.Employee("Dot", "Cook", 17.0),
        ]
        self.assertEqual(hw1.below_pay_average(employees), ["Ana", "Cy", "Dot"])
 
    def test_below_pay_average_empty_list(self):
        # No employees -> no names.
        self.assertEqual(hw1.below_pay_average([]), [])
 
 
if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
