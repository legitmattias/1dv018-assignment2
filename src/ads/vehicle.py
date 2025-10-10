from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Vehicle:
    """Vehicle with Swedish registration number.

    Swedish registration format: 3 letters + 2 digits + 1 letter (e.g., "MLB84A")
    """

    registration: str
    brand: str
    model: str
    year: int

    def __hash__(self) -> int:
        """Custom hash function based on registration number.

        The pattern used:
        - Start with prime number 17
        - Multiply by prime 31 for each character
        - Add character's ordinal value

        This ensures:
        - Position matters (order sensitivity)
        - Uses entire registration number
        - Prime numbers break patterns and reduce collisions

        Returns:
            Hash value for this vehicle
        """
        hv = 17
        for char in self.registration:
            hv = 31 * hv + ord(char)
        return hv

    def __eq__(self, other: object) -> bool:
        """Check equality based on registration number.

        Args:
            other: Object to compare with

        Returns:
            True if both are Vehicles with same registration
        """
        if not isinstance(other, Vehicle):
            return False
        return self.registration == other.registration
