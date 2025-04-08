"""
Concepts related to permutations.
"""


class Permutation:
    """
    A _permutation_ is a bijective map from a set to itself.
    """

    def __init__(self, mapping: dict[int, int]):
        self.mapping = mapping

    @property
    def as_list(self) -> list:
        k = next(iter(self.mapping))
        l, v = [k], k
        while True:
            if (v := self.mapping[v]) == k:
                break
            if v is None:
                # this should be guaranteed in the constructor
                raise ValueError("not a valid permutation")

            l.append(v)

        return l
