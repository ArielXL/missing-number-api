from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class First100NaturalNumbers:
    """
    Represents the set of the first 100 natural numbers. Allows extracting a
    number and calculating the missing one.
    """

    numbers: List[int] = field(default_factory=lambda: list(range(1, 101)))
    extracted: Optional[int] = None

    def Extract(self, n: int) -> None:
        """
        SUMMARY
        -------
            Extracts the number n from the set.

        PARAMETERS
        ----------
            n : int
                The number to extract from the set.
        """
        if not isinstance(n, int):
            raise TypeError("The number to extract must be an integer.")

        if n < 1 or n > 100:
            raise ValueError("The number to extract must be between 1 and 100.")

        if self.extracted is not None:
            raise ValueError(f"A number has already been extracted: {self.extracted}.")

        if n not in self.numbers:
            raise ValueError("The specified number is not available for extraction.")

        self.numbers.remove(n)
        self.extracted = n

    def missing_number(self) -> int:
        """
        SUMMARY
        -------
            Calculates the missing number by comparing the expected sum vs
            the current sum.

        RETURNS
        -------
            int
                The missing number.
        """
        expected_sum = 100 * 101 // 2
        current_sum = sum(self.numbers)
        missing = expected_sum - current_sum

        if missing < 1 or missing > 100:
            raise RuntimeError(
                "The calculation of the missing number resulted in an invalid value."
            )

        return missing
