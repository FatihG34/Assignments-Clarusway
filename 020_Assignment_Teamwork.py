def print_max(arr, k):
    if k >= 1 and k <= len(arr):
        my_list = []
        max = 0
        i = 0
        for i in range(len(arr)-k+1):
            max = arr[i]
            i += 1
            j = 1
            while (j < k):
                if arr[i+j] > max:
                    max = arr[i+j]
                    j += 1
                my_list.append(max)
                break
    print(my_list)


new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print_max(new_list, k)

nums = [1, 3, -1, -3, 5, 3, 6, 7]
l = 3
print_max(nums, l)

list_new = [22, 5, 23, 12, 52, 2, 14, 23]
num = 4
print_max(list_new, num)
