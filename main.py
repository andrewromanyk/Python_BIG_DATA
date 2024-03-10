print("Andrii Romaniuk, KN-3")


def compare_equality(left: int, right: int, *args, **kwargs):
    """
    Check if two objects are mathematically equal.

    Examples:
        >>> compare_equality(1, 1)
        True
        >>> compare_equality("1", 1)
        False
        >>> compare_equality("1", "1")
        True

    Args:
        left (int): first number
        right (int): second number
        *args (list): positional arguments
        **kwargs (dict): keyword arguments

    Returns:
        bool: true if both objects are equal, false otherwise.
    """
    return left == right


"""
Calculates the sum of 2 integers.

Args:
    number_1 (int): first number
    number_2 (int): second number
    
Returns:
    int: sum of the two numbers.
"""


def sum_numbers(number_1, number_2):
    return number_1 + number_2