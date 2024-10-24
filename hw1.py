import data
from data import Price, Rectangle, Book, Circle, Point, Employee
import math
# Write your functions for each part in the space below.

# Part 1
def vowel_count(input_str)-> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in input_str if char in vowels)
# Part 2
def short_lists(input_list: list[list[int]]) -> list[list[int]]:
    return [lst for lst in input_list if len(lst) == 2]

# Part 3
def ascending_pairs(pairs_list: list[list[list]]) -> list[list[list]]:
    result = []
    for lst in pairs_list:
        if len(lst) == 2:
            result.append(sorted(lst))
        else:
            result.append(lst)
    return result


#Part 4
def add_prices(price1: Price, price2: Price) -> Price:
    total_cents = price1.cents + price2.cents
    extra_dollars = total_cents // 100
    extra_cents = total_cents % 100
    total_dollars = price1.dollars + price2.dollars + extra_dollars
    return Price(total_dollars, extra_cents)
#Part 5
def rectangle_area(rectangle: Rectangle) -> int:
    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.top_left.y - rectangle.bottom_right.y
    return width * height
# Part 6
def books_by_author(author:str, books: list[Book]) -> list[Book]:
    return [book for book in books if author in book.authors]
# Part 7
def circle_bound(rectangle: Rectangle) -> Circle:
    center_x = (rectangle.top_left.x + rectangle.bottom_right.x) / 2
    center_y = (rectangle.top_left.y + rectangle.bottom_right.y) / 2
    center = Point(center_x, center_y)
    dx = center_x - rectangle.top_left.x
    dy = center_y - rectangle.top_left.y
    radius = math.sqrt(dx ** 2 + dy ** 2)
    return Circle(center, radius)

# Part 8
def below_pay_average(employees: list[Employee]) -> list[str]:
    if not employees:
        return []
    total_pay = sum(employee.pay_rate for employee in employees)
    num_employees = len(employees)
    average_pay = total_pay / num_employees
    below_average_employees = [employee.name for employee in employees if employee.pay_rate < average_pay]
    return below_average_employees

