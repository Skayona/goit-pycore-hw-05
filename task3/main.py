import sys
from collections import Counter
from colorama import Fore, Back, Style

def log_error_message(message: str):
  print(f"{Fore.WHITE}{Back.RED}ERROR{Style.RESET_ALL}{Fore.RED}: {message}{Style.RESET_ALL}")

def parse_log_line(line: str) -> dict | None:
  parsed_line = line.strip().split(' ', 3)
  if (parsed_line and len(parsed_line) == 4):
    return {
      "date": parsed_line[0],
      "time": parsed_line[1],
      "level": parsed_line[2].upper(),
      "message": parsed_line[3]
    }

def load_logs(file_path: str) -> list | None:
  try:
    with open(file_path, "r", encoding="utf-8") as file:
      parsed_logs = []
      for log in file.readlines():
        parsed_line = parse_log_line(log)

        if (parsed_line):
          parsed_logs.append(parsed_line)

      return parsed_logs

  except FileNotFoundError:
    log_error_message("The file is missing.")
    return

  except ValueError:
    log_error_message("The file has incorrect data.")
    return

def filter_logs_by_level(logs: list, level: str) -> list:
  return list(filter(lambda log: log["level"].lower() == level.lower(), logs))

def count_logs_by_level(logs: list) -> dict:
  return Counter(log["level"] for log in logs)

def display_log_counts(counts: dict):
  print(f"\n{'Log level':<9} | {'Count':<9}")
  print("-" * 10 + "|" + "-" * 9)

  for level, count in counts.items():
      print(f"{level:<9} | {count:<9}")

def display_logs_by_level(logs: list):
  for log in logs:
    print(f"{log['date']} {log['time']} - {log['message']}")


def main():
  args = sys.argv

  if len(args) < 2:
    log_error_message("Please provide a path to a log file for further work.")
    return

  path = args[1]
  level = args[2] if len(args) > 2 else None

  logs = load_logs(path)

  if (logs == None):
    return

  if (not logs):
    print("There is not logs in the file.")
    return


  display_log_counts(count_logs_by_level(logs))

  if (level):
    print(f"\nDetails for logs with level '{level.upper()}':")
    display_logs_by_level(filter_logs_by_level(logs, level))

if __name__ == "__main__":
  main()