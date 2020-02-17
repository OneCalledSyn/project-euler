def summation(n):
  sum = 0;
  for i in range(n):
    if (i % 3 == 0 or i % 5 == 0):
      sum = sum + i
  return sum    
  
  print(summation(1000))
