def tuple_sum(pairs, threshold):
    """" generate pairs that exceed a certain threshold
    :param pairs: list of tuples of pairs
    :param threshold: int
    :return: pair if sum is larger than threshold
    >>> [s for s in tuple_sum([(1, 2), (3, 4), (0, 7.3)], 6)]
    [7, 7.3]
    """
    for p in pairs:
        a, b = p
        sum = a + b
        if sum >+ threshold:
            yield sum

print(tuple_sum([(1, 2), (3, 4), (0, 7.3)], 6))