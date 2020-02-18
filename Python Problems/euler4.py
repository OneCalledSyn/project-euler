# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


max = 0
  for i in range(101, 1000):
    for j in range(101, 1000):
      candidate = i * j
      if str(candidate) == str(candidate)[::-1]:
        if candidate > max :
          max = candidate

print(max)    
