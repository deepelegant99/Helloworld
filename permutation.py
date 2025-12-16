from itertools import permutations
from typing import Iterable
import sys


def word_permutations(word: str) -> list[str]:
    """Return all unique permutations of the given word.

    Args:
        word: The input word to permute.

    Returns:
        A list containing each unique permutation of the word.
    """
    seen = set()
    unique_permutations: list[str] = []

    for chars in permutations(word):
        perm = "".join(chars)
        if perm not in seen:
            seen.add(perm)
            unique_permutations.append(perm)

    return unique_permutations


def _print_permutations(words: Iterable[str]) -> None:
    for word in words:
        results = word_permutations(word)
        print(f"Permutations for '{word}':")
        print(results)


if __name__ == "__main__":
    args = sys.argv[1:] or ["Hello"]
    _print_permutations(args)
