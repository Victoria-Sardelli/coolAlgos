def selection(a, n):
    """
    selection sort to sort an array in O(n^2) time
    :param a: array
    :param n: num of elements in a
    """
    for i in range(len(a)):
       smallest = i
       for j in range(i+1, n):
           if a[j] < a[smallest]:
               smallest = j
       a[i], a[smallest] = a[smallest], a[i]


def testSel():
    a = [1,3,4,7,2,8,10,0,5,6,9]
    b = [10,9,8,7,6,5,4,3,2,1,0]
    selection(a, 11)
    selection(b, 11)
    print(a)
    print(b)
