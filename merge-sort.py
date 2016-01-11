def mergeSort(a, p, r):
    """
    sorts subarray a[p...r] into increasing order
    :param a: array
    :param p: start index
    :param r: end index
    """
    if p >= r:
        return
    q = (p+r)//2
    mergeSort(a, p, q)
    mergeSort(a, q+1, r)
    merge(a, p, q, r)


def merge(a, p, q, r):
    """
    merges two sorted subarrays (a[p:q+1] and a[q+1:r+1])
    :param a: array
    :param p: start index
    :param q: halfway index
    :param r: end index
    """
    b = a[p:q+1]
    c = a[q+1:r+1]
    b.append(float("inf"))
    c.append(float("inf"))
    i = 0
    j = 0
    for k in range(p,r+1):
        if b[i] <= c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1


def testMerge():
    a = [1,0,3,2,6,4,7,5,9,8]
    mergeSort(a, 0, 9)
    print(a)