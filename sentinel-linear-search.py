def sentinel(a, n, x):
    """
    A linear search through an unsorted array
    :param a: array
    :param n: num of elements in a
    :param x: desired value
    :return: index i of x in array a OR "NOT FOUND"
    """
    i = 0
    last = a[n-1]
    a[n-1] = x
    while a[i] != x:
        i += 1
    a[n-1] = last
    if i < n-1 or a[n-1] == x:
        return i
    return "NOT FOUND"


def testSentinel():
    a = ['a','b','c','d','e']
    print(sentinel(a, 5, 'a'))
    print(sentinel(a, 5, 'b'))
    print(sentinel(a, 5, 'c'))
    print(sentinel(a, 5, 'd'))
    print(sentinel(a, 5, 'e'))
    print(sentinel(a, 5, 'f'))
    print(sentinel(a, 5, 1))