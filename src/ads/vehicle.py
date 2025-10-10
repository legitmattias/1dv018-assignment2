from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Vehicle:
    """Vehicle with Swedish registration number.

    Swedish registration format: 3 letters + 2 digits + 1 letter (e.g., "ABC12D")
    """

    registration: str
    brand: str
    model: str
    year: int

    def __hash__(self) -> int:
        """Hash based on registration using polynomial rolling hash."""
        hv = 17
        for char in self.registration:
            hv = 31 * hv + ord(char)
        return hv

    def __eq__(self, other: object) -> bool:
        """Compare vehicles by registration number."""
        if not isinstance(other, Vehicle):
            return False
        return self.registration == other.registration
