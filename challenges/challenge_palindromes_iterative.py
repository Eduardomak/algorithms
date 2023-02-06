def is_palindrome_iterative(word: str) -> bool:
    """Faça o código aqui."""
    return len(word) > 0 and word == word[::-1]
