"""
Concepts related to permutations.
"""


class Permutation:
    """
    A _permutation_ is a bijective map from a set to itself.
    """

    def __init__(self, mapping: dict):
        self.mapping = mapping
        self.set = list(mapping.keys())
