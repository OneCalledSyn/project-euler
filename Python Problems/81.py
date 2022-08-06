def minimal_path_sum(file_name):

  with open(file_name) as file:
    matrix = file.readlines()

  n = len(matrix)

  for row in range(n):
    matrix[row] = list(map(int, matrix[row].replace('\n', '').split(",")))
  
  for i in range(n - 2, -1, -1):
    matrix[n - 1][i] += matrix[n - 1][i + 1] #bottom row
    matrix[i][n - 1] += matrix[i + 1][n - 1] # right column

  # Reverse greedynamic 
  for j in range(n - 2, -1, -1):
    for k in range(n - 2, -1, -1):
      matrix[j][k] += min(matrix[j + 1][k], matrix[j][k + 1])

  return matrix[0][0]

print(minimal_path_sum('../Desktop/p081_matrix.txt'))