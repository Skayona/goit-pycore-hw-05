from collections.abc import Generator
from typing import Callable
import re

def generator_numbers(text: str) -> Generator[float, None, None]:
  """
  Accepts a string as an argument and yields all real numbers found in the text, separated by spaces.

  Parameters:
     text (str): string to process

  Returns: all real numbers found in the text as a generator
  """
  pattern = r"\s\d+\.\d+\s"
  matches = re.findall(pattern, text)

  for match in matches:
    yield float(match.strip())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
  """
  Calculates the total sum of numbers in the text using the provided generator function.

  Parameters:
      text (str): string to process
      func (Callable): generator function that yields numbers from the text

  Returns:
      float: total sum of all extracted numbers
    """
  return sum(func(text), 0.0)


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}") #Загальний дохід: 1351.46
