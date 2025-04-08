from permutations import permutation


def test__permutation_can_be_represented_as_an_ordered_list():
    mapping = {
        1: 3,
        2: 1,
        3: 2,
    }
    perm = permutation.Permutation(mapping)

    assert perm.as_list == [1, 3, 2]
