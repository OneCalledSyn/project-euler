# Evaluate the sum of all the amicable numbers under 10000.
# Done jointly with Legman

def get_divisors(n):
  divisor_pairs = [[x, int(n / x)] for x in range(2, int(n / 4) + 1) if n % x == 0]
  return set([divisor for divisor_pair in divisor_pairs for divisor in divisor_pair] + [1])

def get_amicable_numbers(n):
  amicable_numbers = []
  for i in range(1, n + 1):
    sum_of_divisors = sum(get_divisors(i))
    if sum_of_divisors == i:
      continue
    potential_amicable_sum = sum(get_divisors(sum_of_divisors))
    if potential_amicable_sum == i:
      amicable_numbers.append(i)
  return amicable_numbers

print(sum(get_amicable_numbers(10000)))
