def binary(a, n, x):
    """
    binary search through a sorted array; takes O(lgn) time
    :param a: sorted array
    :param n: num of elements in a
    :param x: desired element
    :return: index i of x in a OR "NOT FOUND"
    """
    p = 0
    r = n-1
    while p <= r:
        q = (p+r)//2
        if a[q] == x:
            return q
        if a[q] > x:
            r = q-1
        else:
            p = q+1
    return "NOT FOUND"


def testBinary():
    a = [0,1,2,3,4,5,6,7,8,9,10]
    print(binary(a,11,11))
    print(binary(a,11,0))
    print(binary(a,11,10))
    print(binary(a,11,2))
    print(binary(a,11,5))


def recursive_binary(a, p, r, x):
    """
    recursive binary search through sorted array
    :param a: sorted array
    :param p: start index
    :param r: end index
    :param x: desired element
    :return: index i of x in a OR "NOT FOUND"
    """
    if p > r:
        return "NOT FOUND"
    q = (p+r)//2
    if a[q] == x:
        return q
    if a[q] > x:
        return recursive_binary(a, p, q-1, x)
    else:
        return recursive_binary(a, q+1, r, x)


def testRecBin():
    a = [0,1,2,3,4,5,6,7,8,9,10]
    n = len(a)-1
    print(recursive_binary(a,0,n,11))
    print(recursive_binary(a,0,n,0))
    print(recursive_binary(a,0,n,10))
    print(recursive_binary(a,0,n,2))
    print(recursive_binary(a,0,n,5))