from typing import Union


def quick_sort_recursive(list_string: Union[str, list]) -> list:
    if len(list_string) <= 1:
        return list_string
    pivot = list_string[0]
    left = [letter for letter in list_string if letter < pivot]
    middle = [letter for letter in list_string if letter == pivot]
    right = [letter for letter in list_string if letter > pivot]
    return quick_sort_recursive(left) + middle + quick_sort_recursive(right)


def is_anagram(first_string: str, second_string: str) -> tuple:
    """Faça o código aqui."""
    if not isinstance(first_string, str) or not isinstance(second_string, str):
        raise TypeError
    first_string = first_string.lower()
    second_string = second_string.lower()
    sorted_str1 = quick_sort_recursive(first_string)
    sorted_str2 = quick_sort_recursive(second_string)
    return (
        "".join(sorted_str1),
        "".join(sorted_str2),
        sorted_str1 == sorted_str2 and len(sorted_str1) > 0,
    )
