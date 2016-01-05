def rls(a, n, i, x):
    """
    a recursive linear search through unsorted array
    :param a: array
    :param n: num of elements in array a
    :param i: index to check
    :param x: desired value
    :return: index i of x in array a OR "NOT FOUND"
    """
    if i > n-1:
        return "NOT FOUND"
    if a[i] == x:
        return i
    return rls(a, n, i+1, x)


def testRls():
    a = ['a','b','c','d','e']
    print(rls(a,5,0,'a'))
    print(rls(a,5,0,'b'))
    print(rls(a,5,0,'c'))
    print(rls(a,5,0,'d'))
    print(rls(a,5,0,'e'))
    print(rls(a,5,0,'f'))
    print(rls(a,5,-1,'a'))


testRls()