"""
Test file for CSP_6_01_Library_Basics.py
Tests all functions with various test cases
"""

import CSP_6_01_Library_Basics as functions

def test_process_expenses():
    """Test the process_expenses function"""
    print("=" * 50)
    print("Testing process_expenses()...")
    print("=" * 50)
    
    # Test case 1: Normal prices
    prices1 = [100, 200, 50]
    result1 = functions.process_expenses(prices1)
    expected1 = [115.0, 230.0, 57.5]
    print(f"Test 1 - Input: {[100, 200, 50]}")
    print(f"Expected: {expected1}")
    print(f"Got: {result1}")
    # Allow small floating point differences
    pass1 = all(abs(result1[i] - expected1[i]) < 0.01 for i in range(len(result1)))
    print(f"PASS: {pass1}\n")
    
    # Test case 2: Empty list
    prices2 = []
    result2 = functions.process_expenses(prices2)
    expected2 = []
    print(f"Test 2 - Input: {[]}")
    print(f"Expected: {expected2}")
    print(f"Got: {result2}")
    print(f"PASS: {result2 == expected2}\n")
    
    # Test case 3: Single price
    prices3 = [1000]
    result3 = functions.process_expenses(prices3)
    expected3 = [1150.0]
    print(f"Test 3 - Input: {[1000]}")
    print(f"Expected: {expected3}")
    print(f"Got: {result3}")
    pass3 = abs(result3[0] - expected3[0]) < 0.01
    print(f"PASS: {pass3}\n")


def test_sanitize_usernames():
    """Test the sanitize_usernames function"""
    print("=" * 50)
    print("Testing sanitize_usernames()...")
    print("=" * 50)
    
    # Test case 1: Mixed case with spaces
    usernames1 = [" Apple", "Banana ", " CHERRY ", " date "]
    result1 = functions.sanitize_usernames(usernames1)
    expected1 = ["apple", "banana", "cherry", "date"]
    print(f"Test 1 - Input: {usernames1}")
    print(f"Expected: {expected1}")
    print(f"Got: {result1}")
    print(f"PASS: {result1 == expected1}\n")
    
    # Test case 2: Already clean
    usernames2 = ["user1", "user2"]
    result2 = functions.sanitize_usernames(usernames2)
    expected2 = ["user1", "user2"]
    print(f"Test 2 - Input: {usernames2}")
    print(f"Expected: {expected2}")
    print(f"Got: {result2}")
    print(f"PASS: {result2 == expected2}\n")
    
    # Test case 3: Multiple spaces at edges
    usernames3 = ["  john  ", " mary "]
    result3 = functions.sanitize_usernames(usernames3)
    expected3 = ["john", "mary"]
    print(f"Test 3 - Input: {usernames3}")
    print(f"Expected: {expected3}")
    print(f"Got: {result3}")
    print(f"PASS: {result3 == expected3}\n")


def test_identify_outliers():
    """Test the identify_outliers function"""
    print("=" * 50)
    print("Testing identify_outliers()...")
    print("=" * 50)
    
    # Test case 1: Mix of values
    values1 = [50, 150, 75, 200, 100, 300, 25]
    result1 = functions.identify_outliers(values1)
    expected1 = [150, 200, 300]
    print(f"Test 1 - Input: {values1}")
    print(f"Expected (values > 100): {expected1}")
    print(f"Got: {result1}")
    print(f"PASS: {result1 == expected1}\n")
    
    # Test case 2: No outliers
    values2 = [10, 20, 30, 50, 100]
    result2 = functions.identify_outliers(values2)
    expected2 = []
    print(f"Test 2 - Input: {values2}")
    print(f"Expected (values > 100): {expected2}")
    print(f"Got: {result2}")
    print(f"PASS: {result2 == expected2}\n")
    
    # Test case 3: All outliers
    values3 = [101, 150, 200, 500]
    result3 = functions.identify_outliers(values3)
    expected3 = [101, 150, 200, 500]
    print(f"Test 3 - Input: {values3}")
    print(f"Expected (values > 100): {expected3}")
    print(f"Got: {result3}")
    print(f"PASS: {result3 == expected3}\n")


def test_search_helper_functions():
    """Test the linear and binary search helper functions"""
    print("=" * 50)
    print("Testing search helper functions...")
    print("=" * 50)
    
    # Test linear search
    items1 = ["apple", "cherry", "banana", "date"]
    target1 = "cherry"
    result1 = functions.linear_search(items1, target1)
    expected1 = 1
    print(f"Linear Search Test 1:")
    print(f"  Items: {items1}")
    print(f"  Target: '{target1}'")
    print(f"  Expected index: {expected1}")
    print(f"  Got: {result1}")
    print(f"  PASS: {result1 == expected1}\n")
    
    # Test linear search - not found
    result2 = functions.linear_search(items1, "grape")
    expected2 = -1
    print(f"Linear Search Test 2 (not found):")
    print(f"  Target: 'grape'")
    print(f"  Expected: {expected2}")
    print(f"  Got: {result2}")
    print(f"  PASS: {result2 == expected2}\n")
    
    # Test binary search
    items2 = ["apple", "banana", "cherry", "date"]
    target2 = "banana"
    result3 = functions.binary_search(items2, target2)
    expected3 = 1
    print(f"Binary Search Test 1:")
    print(f"  Items: {items2}")
    print(f"  Target: '{target2}'")
    print(f"  Expected index: {expected3}")
    print(f"  Got: {result3}")
    print(f"  PASS: {result3 == expected3}\n")
    
    # Test binary search - not found
    result4 = functions.binary_search(items2, "elderberry")
    expected4 = -1
    print(f"Binary Search Test 2 (not found):")
    print(f"  Target: 'elderberry'")
    print(f"  Expected: {expected4}")
    print(f"  Got: {result4}")
    print(f"  PASS: {result4 == expected4}\n")


def test_search_and_report_logic():
    """Test search_and_report logic without user input"""
    print("=" * 50)
    print("Testing search_and_report() logic...")
    print("=" * 50)
    
    print("Note: search_and_report() requires user input.")
    print("The function will:")
    print("1. Ask for a search term")
    print("2. Sanitize both the search term and the list")
    print("3. Use binary search if sorted, linear search if not\n")
    
    # Demonstrate the logic
    print("Example 1 - Unsorted list:")
    items1 = [" Apple", "Banana ", " CHERRY ", " date "]
    print(f"  Original list: {items1}")
    sanitized1 = functions.sanitize_usernames(items1)
    print(f"  Sanitized list: {sanitized1}")
    is_sorted1 = all(sanitized1[i] <= sanitized1[i+1] for i in range(len(sanitized1)-1))
    print(f"  Is sorted: {is_sorted1}")
    print(f"  Will use: Linear Search")
    index1 = functions.linear_search(sanitized1, "cherry")
    print(f"  Finding 'cherry': Index = {index1}\n")
    
    print("Example 2 - Sorted list:")
    items2 = ["apple", "banana", "cherry", "date"]
    print(f"  Original list: {items2}")
    is_sorted2 = all(items2[i] <= items2[i+1] for i in range(len(items2)-1))
    print(f"  Is sorted: {is_sorted2}")
    print(f"  Will use: Binary Search")
    index2 = functions.binary_search(items2, "banana")
    print(f"  Finding 'banana': Index = {index2}\n")
    
    print("To manually test search_and_report(), run:")
    print("  python3 -c 'import CSP_6_01_Library_Basics as f; print(f.search_and_report([\" Apple\", \"Banana \", \" CHERRY \"]))'")
    print()


def main():
    """Run all tests"""
    print("\n" + "=" * 50)
    print("RUNNING ALL TESTS")
    print("=" * 50 + "\n")
    
    test_process_expenses()
    test_sanitize_usernames()
    test_identify_outliers()
    test_search_helper_functions()
    test_search_and_report_logic()
    
    print("=" * 50)
    print("NOTE: analyze_scores() requires interactive input")
    print("To test it manually, run:")
    print("  python3 -c 'import CSP_6_01_Library_Basics as f; print(f.analyze_scores(3))'")
    print("  Then enter 3 scores when prompted.")
    print("=" * 50)


if __name__ == "__main__":
    main()
