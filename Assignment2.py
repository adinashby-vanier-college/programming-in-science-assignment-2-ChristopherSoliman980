# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):

  if len(numbers) == 1:
    return numbers[0], None

  else:
    first = max(numbers)
    numbers.remove(first)
    second = max(numbers)

    if second == first:
      numbers.remove(second)
      second = max(numbers)

  return first, second
# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):

    result = []

    for i in numbers:
        if i not in result:
            result.append(i)

    result.sort()

    return result
# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):

    result = []

    sum = 0

    for i in arr:
        sum += i
        result.append(sum)

    return result

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
  
    rows = len(matrix)
    columns = len(matrix[0])
    
    transposed = [[0] * rows for _ in range(columns)]
    
    for i in range(rows):
      
        for j in range(columns):

            transposed[j][i] = matrix[i][j]
    
    return transposed
# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):

     result = lst[::step]

     return result 

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):

    pair = zip(list1, list2)

    dot_product = 0

    for x , y in pair:
        dot_product += x * y

    return dot_product


# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
 

def matrix_multiplication(matrix1, matrix2):
  
    result = [
        [0 for _ in range(len(matrix2[0]))]
        for _ in range(len(matrix1))
        ]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result 
