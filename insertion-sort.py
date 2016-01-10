def insertion(a, n):
    """
    insertion sort to sort an array in O(n^2) time
    :param a: array
    :param n: num of elements in array
    """
    for i in range(1,n):
        j = i-1
        key = a[i]
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key


def testInsert():
    a = [2,4,1,6,0,3,7,8,5,10,9]
    b = [10,9,8,7,6,5,4,3,2,1,0]
    insertion(a,11)
    insertion(b,11)
    print(a)
    print(b)
