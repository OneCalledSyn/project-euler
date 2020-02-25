# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

filename = 'euler13.txt'
with open(filename, "r") as bignum:
  summands = []
  for line in bignum:
    summands.append(int(line))
    
total = sum(summands)
print(str(total)[:10])
