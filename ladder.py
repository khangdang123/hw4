def my_steps(n):
  if n < 1 or n > 25:
    raise Error("Out of bounds")
    
  if n <= 1:
    return n
  return my_steps(n-1) + my_steps(n-2)

def count_ways(s):
  return my_steps(s+1)
