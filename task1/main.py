from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
  cache = {}

  def fibonacci(n: int) -> int:
      if n <= 0:
        return 0
      if n == 1:
        return 1
      if n in cache:
        return cache[n]

      cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

      return cache[n]

  return fibonacci


# # Testing
# fib = caching_fibonacci()

# print(fib(10))  # Output 55
# print(fib(15))  # Output 610