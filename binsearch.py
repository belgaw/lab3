def lul(a):     #O(nlog(n))
  n = len(a)
  print(a)
  if n <= 1:
    return 1
  return lul(a[:n//2]) + lul(a[n//2:])


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubbleSort(arr):                         #O(n^3)
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            for l in range(0,n):
                print(i,j,l)
    return arr

def longsort(a):     #O(3n)
    max_item = a[0]
    for item in a:
        if item > max_item:
            max_item = item
    for item in a:
        if item < max_item:
            max_item = item
    for item in a:
        if item > max_item:
            max_item = item


def heap(a, n):    #O(n!)
    if n == 1:
        print(a)
        return
    for i in range(n):
        heap(a, n - 1)
        if n % 2 == 0:
            a[i], a[n - 1] = a[n - 1], a[i]
        else:
            a[0], a[n - 1] = a[n - 1], a[0]


def binary(arr, x, low, high):        #O(3log(n))
    for i in range(3):
        while low != high:
            mid = (low + high) / 2
            if (x == arr[mid]):
                return mid
            else:
                if (x > arr[mid]):
                    low = mid + 1
                else:
                    high = mid - 1



arr=[654,954,432,8564,5432,96,23,86,3,9,8,234,87,56,]
print(arr)
print(lul(arr))