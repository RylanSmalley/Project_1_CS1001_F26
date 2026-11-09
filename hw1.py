"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data


 #Part 1: vowel_count
def vowel_count(text: str) -> int:
    # Purpose: count how many vowels (a, e, i, o, u) appear in a string,
    #   ignoring upper/lower case.
    # Input(s): text - the string to examine.
    # Output: the number of vowel characters in text, as an int.
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count += 1
    return count
 
 
# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # Purpose: pick out the inner lists that have exactly two elements.
    # Input(s): items - a list of lists of integers.
    # Output: a new list containing only the length-2 lists from items,
    #   in their original order.
    result = []
    for lst in items:
        if len(lst) == 2:
            result.append(lst)
    return result
 
 
# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # Purpose: put every length-2 list into ascending order, leaving
    #   lists of any other length unchanged.
    # Input(s): items - a list of lists of integers.
    # Output: a new list where each two-element list is sorted
    #   (smaller value first) and all other lists are kept as they were.
    result = []
    for lst in items:
        if len(lst) == 2:
            result.append([min(lst[0], lst[1]), max(lst[0], lst[1])])
        else:
            result.append(lst)
    return result
 
 
# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # Purpose: add two prices together, carrying extra cents into dollars
    #   so the result always has fewer than 100 cents.
    # Input(s): first, second - the two Price values to add.
    # Output: a new Price equal to first + second.
    total_cents = (first.dollars + second.dollars) * 100 + first.cents + second.cents
    return data.Price(total_cents // 100, total_cents % 100)
 
 
# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # Purpose: compute the area of an axis-aligned rectangle.
    # Input(s): rectangle - a Rectangle given by its top-left and
    #   bottom-right corner Points.
    # Output: the area (width * height) as a float.
    width = abs(rectangle.bottom_right.x - rectangle.top_left.x)
    height = abs(rectangle.top_left.y - rectangle.bottom_right.y)
    return float(width * height)
 
 
# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # Purpose: find every book written (or co-written) by a given author.
    # Input(s): author - the author's name to search for;
    #   books - the list of Book objects to search.
    # Output: a list of the Books whose authors include author,
    #   in their original order.
    result = []
    for book in books:
        if author in book.authors:
            result.append(book)
    return result
 
 
# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # Purpose: build the smallest circle that fully contains a rectangle.
    # Input(s): rectangle - a Rectangle given by its top-left and
    #   bottom-right corner Points.
    # Output: a Circle centered at the rectangle's center whose radius
    #   reaches the corners (half the rectangle's diagonal).
    tl = rectangle.top_left
    br = rectangle.bottom_right
    center = data.Point((tl.x + br.x) / 2, (tl.y + br.y) / 2)
    radius = math.sqrt((tl.x - center.x) ** 2 + (tl.y - center.y) ** 2)
    return data.Circle(center, radius)
 
 
# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # Purpose: find the employees who are paid less than the group's
    #   average pay rate.
    # Input(s): employees - a list of Employee objects.
    # Output: a list of the names of employees whose pay_rate is below
    #   the average, in their original order (empty if the list is empty).
    if len(employees) == 0:
        return []
    total = 0.0
    for emp in employees:
        total += emp.pay_rate
    average = total / len(employees)
    result = []
    for emp in employees:
        if emp.pay_rate < average:
            result.append(emp.name)
    return result
    
