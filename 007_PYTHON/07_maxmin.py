list=[1,2,3,4,5,8,6]
list.sort()
print("min element: ", list[0])
print("2nd min element: ", list[1])
list.sort(reverse=True)
print("max element: ",list[0])         
print("2nd max element: ",list[1])   


def find_max(arr):
    max_value = arr[0]  
    for i in range(1, len(arr)):  
        if arr[i] > max_value:
            max_value = arr[i]  
    return max_value  

arr = [2, 3, 4, 8, 1]
print(find_max(arr))  


def find_min(arr):
    min_value = arr[0]  
    for i in range(1, len(arr)): 
        if arr[i] < min_value:
            min_value = arr[i]  
    return min_value 

arr = [2, 3, 4, 8, 1]
print(find_min(arr))  


def find_nth_largest(arr, n):
    for i in range(n):  # Loop for finding nth largest
        largest = float('-inf')  # Start with a very small number
        
        # Loop through the array to find the largest element
        for num in arr:
            if num > largest:
                largest = num
        
        # After finding the largest, remove that number from the array (or mark it)
        arr = [num for num in arr if num != largest]
    
    # After n loops, the largest found in the nth loop is the nth largest
    return largest

# Example usage
arr = [2, 3, 4, 8, 1]
n = 3
print(find_nth_largest(arr, n))  # Output: 4 (3rd largest number)
