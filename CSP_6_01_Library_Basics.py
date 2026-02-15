"""
Corrected functions for data processing assignment
Each function uses at least one function from analytics.py
"""

import analytics


# Modify the below function such that it takes in a list of prices and returns that list with 15% added value
def process_expenses(rawPrices):
    """Add 15% to each price in the list"""
    # Use analytics.apply_markup to add 15% (0.15) to each price
    for i in range(len(rawPrices)):
        rawPrices[i] = analytics.apply_markup(rawPrices[i], 0.15)
    return rawPrices


# Modify the below function such that it asks the user for n scores and then returns the highest score and the average score of the list.
def analyze_scores(n):
    """Ask user for n scores and return the max and average"""
    scores = []
    for i in range(n):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)

    # Use analytics functions
    max_score = analytics.get_highest(scores)
    average_score = analytics.get_average(scores)

    return max_score, average_score


# Modify the below function such that it takes in a list of strings and returns that list with all spaces removed
# and all letters lower case.
def sanitize_usernames(list):
    """Remove spaces and convert to lowercase for all strings in list"""
    # Use analytics.clean_text which strips whitespace and converts to lowercase
    return analytics.clean_text(list)


# Modify the list such that it takes in a list as an argument and returns a version of the list with all values over 100.
def identify_outliers(list):
    """Return only values over 100 from the list"""
    # Use analytics.filter_threshold to get values over 100
    return analytics.filter_threshold(list, 100)


# Modify the below function such that it takes in a list of items and asks the user for an item to search for.
# Sanitize the list to only be lower case words with no extra spaces
# Then return the location of the word using binary search if the list is in order and linear search if it is not.
# example items = [" Apple", "Banana ", " CHERRY ", " date "]
def search_and_report(list):
    """Search for user-specified item using appropriate search algorithm"""
    target = input("What am I searching for?: ")

    # Sanitize the target (strip whitespace and lowercase)
    target = target.strip().lower()

    # Sanitize the list using analytics.clean_text
    sanitized_list = analytics.clean_text(list)

    # Check if list is sorted
    is_sorted = all(sanitized_list[i] <= sanitized_list[i + 1] for i in range(len(sanitized_list) - 1))

    # Use appropriate search algorithm
    if is_sorted:
        # Binary search
        index = binary_search(sanitized_list, target)
    else:
        # Linear search
        index = linear_search(sanitized_list, target)

    return index


def linear_search(items, target):
    """Perform linear search and return index of target, or -1 if not found"""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


def binary_search(items, target):
    """Perform binary search on sorted list and return index of target, or -1 if not found"""
    left, right = 0, len(items) - 1

    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1