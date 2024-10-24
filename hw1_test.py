import data
import hw1
import unittest
import math
from data import Rectangle, Price, Point, Book, Circle, Employee

from hw1 import short_lists, vowel_count, ascending_pairs, add_prices, rectangle_area, books_by_author, circle_bound, below_pay_average


# Write your test cases for each part below.
# Part 1
class TestCases(unittest.TestCase):
    #Part 1
    def test_empty_string(self):
        self.assertEqual(vowel_count(""),0)
    def test_all_vowels(self):
        self.assertEqual(vowel_count("aeiouAEIOU"),10)
    def test_no_vowels(self):
        self.assertEqual(vowel_count("bcDG"), 0)
    def test_mixed_word(self):
        self.assertEqual(vowel_count("Hello World"),3)
    # Part 2
    def test_length_2(self):
        self.assertEqual(short_lists([[1, 2], [3, 4]]), [[1, 2], [3, 4]])
    def test_empty_lists(self):
        self.assertEqual(short_lists([]), [])
    def test_mixed_length_lists(self):
        self.assertEqual(short_lists([[1, 2], [3], [4, 5, 6], [7, 8]]), [[1, 2], [7, 8]])
    def test_single_input_list(self):
        self.assertEqual(short_lists([[1], [2], [3], [4], [5]]), [])
    # Part 3
    def test_sorted_pairs(self):
        self.assertEqual(ascending_pairs([[1, 2], [3, 4]]), [[1, 2], [3, 4]])
    def test_empty_pairs_list(self):
        self.assertEqual(ascending_pairs([]), [])
    # Part 4
    def test_zero_price(self):
        price1 = Price(0,0)
        price2 = Price(0,0)
        result = add_prices(price1, price2)
        self.assertEqual(result, Price(0,0))
    def test_prices1(self):
        price1 = Price(2, 75)
        price2 = Price(3, 50)
        result = add_prices(price1, price2)
        self.assertEqual(result, Price(6, 25))
    # Part 5
    def test_rectangle_one(self):
        rectangle = Rectangle(Point(3,7), Point(3,1))
        result = rectangle_area(rectangle)
        self.assertEqual(result, 0)
    def test_rectangle_two(self):
        rectangle = Rectangle(Point(1,2), Point(5,2))
        result = rectangle_area(rectangle)
        self.assertEqual(result, 0)
    # Part 6
    def test_single_author(self):
        book1 = Book(["J.K. Rowling"], "Harry Potter and the Prisoner of Azkaban")
        book2 = Book(["Rick Riordan"], "The Lightning Thief")
        books = [book1, book2]
        result = books_by_author("J.K. Rowling", books)
        self.assertEqual(result, [book1])
    def test_multiple_books(self):
        book1 = Book(["J.K. Rowling"], "Harry Potter and the Prisoner of Azkaban")
        book2 = Book(["J.K. Rowling"], "Harry Potter and the Chamber of Secrets")
        book3 = Book(["Rick Riordan"], "The Lightning Thief")
        books = [book1, book2, book3]
        result = books_by_author("J.K. Rowling", books)
        self.assertEqual(result, [book1, book2])
    # Part 7
    def test_circle_one(self):
        top_left = Point(0, 2)
        bottom_right = Point(2, 0)
        rectangle = Rectangle(top_left, bottom_right)
        expected_center = Point(1, 1)
        expected_radius = math.sqrt(1 ** 2 + 1 ** 2)
        expected_circle = Circle(expected_center, expected_radius)
        result = circle_bound(rectangle)
        self.assertEqual(result, expected_circle)
    def test_circle_two(self):
        top_left = Point(0, 0)
        bottom_right = Point(0, 2)
        rectangle = Rectangle(top_left, bottom_right)
        expected_center = Point(0, 1)
        expected_radius = 1.0
        expected_circle = Circle(expected_center, expected_radius)
        result = circle_bound(rectangle)
        self.assertEqual(result, expected_circle)
    # Part 8
    def test_no_employees(self):
        employees = []
        result = below_pay_average(employees)
        self.assertEqual(result, [])
    def test_all_below_average(self):
        employees = [Employee('Angelina', 50),Employee("Matthew", 30), Employee("Ana", 40)]
        result = below_pay_average(employees)
        self.assertEqual(result, ["Matthew"])

if __name__ == '__main__':
    unittest.main()
