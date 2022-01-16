

def insertion_sort(arr):

    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1

        while (i >= 0) and (arr[i] > key):
            arr[i+1] = arr[i]
            i -=  1

        arr[i+1] = key

# Test

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
