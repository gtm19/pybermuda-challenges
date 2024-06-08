"""
SORTING

There are many different ways to sort a list. Some are more efficient than others.

Python provides a couple of ways to sort a list. The most common way is to use the built-in `sort` method on
the list directly. This method sorts the list in place. You can also use the `sorted` function which returns a new
sorted list without modifying the original list.

The purpose of this exercise, however, is to have you write your own sorting algorithm. The algorithm should take a list
and an order parameter. The order parameter can be either "asc" for ascending order or "desc" for descending order.

Here are some good places to look for sorting algorithms:
- Bubble sort
- Selection sort
- Insertion sort
- Merge sort

Google is your friend. Look up these algorithms and try to implement one of them.

You cannot use the built-in `sort` method or the `sorted` function. You must write your own sorting algorithm.

This excercise will introduce the concept of unit tests, and algorithm complexity.

The unit tests can be found in the file 003/test_sort.py

To run the tests simply run `pytest` in the terminal (after having done `pip install -r requirements.txt`)
"""


def quicksort(list_to_sort: list) -> list:
    """Implementation of quicksort https://en.wikipedia.org/wiki/Quicksort"""
    if len(list_to_sort) <= 1:
        return list_to_sort
    anchor = list_to_sort[-1]
    lower = [item for item in list_to_sort[:-1] if item <= anchor]
    higher = [item for item in list_to_sort[:-1] if item > anchor]
    return quicksort(lower) + [anchor] + quicksort(higher)


def manual_sort(list_to_sort: list, *, order: str) -> int:
    """
    Sorts a list in ascending or descending order based on the given order parameter.

    Args:
        list_to_sort[list]: The list to be sorted.
        order[str]: The order in which to sort the list. Can be either "asc" for ascending order or "desc" for descending order.

    Returns:
        The sorted list.

    """
    # WRITE YOUR CODE HERE 👇👇
    sorted_list = quicksort(list_to_sort)
    if order == "desc":
        sorted_list = sorted_list[::-1]
    return sorted_list
    # WRITE YOUR CODE HERE 👆👆


if __name__ == "__main__":
    test_list = ["a", "B", "d", "C"]
    print(manual_sort(test_list, order="desc"))
