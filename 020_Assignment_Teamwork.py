# *  Time to put your newly learned skills to work!

# *  This is an interview question asked by Google.drawing

# *  Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.


def print_max(arr, k):
    if k >= 1 and k <= len(arr):
        my_list = []
        max = 0
        for i in range(len(arr)-k+1):
            max = arr[i]
            for j in range(1, k):
                if arr[i+j] > max:
                    max = arr[i+j]
            my_list.append(max)
    print(my_list)


# new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = 3
# print('first')
# print_max(new_list, k)

# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# l = 3
# print('second')
# print_max(nums, l)

list_new = [22, 5, 23, 12, 52, 2, 14, 23]
num = 4
print('third')
print_max(list_new, num)
