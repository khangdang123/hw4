def my_steps(n):
  if n < 1 or n > 25:
        raise Error("Out of bounds.")
    
  def count_ways(n):
    if n <= 1:
      return 1
    return count_ways(n-1) + count_ways(n-2)

  return count_ways(n)

