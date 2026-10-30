def input_error(func):
  def inner(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except ValueError:
      return "Give me name and phone please."
    except IndexError:
      return "Enter user name."
    except KeyError:
      return "Contact not found."

  return inner

def parse_input(user_input: str) -> tuple[str, ...]:
  """
  Parses the user-entered string into a command and its arguments
  """
  user_input = user_input.strip()

  if not user_input:
    return "", ""

  cmd, *args = user_input.split()
  cmd = cmd.lower()

  return cmd, *args

@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
  name, phone = args

  if name in contacts:
    return "Contact already exists."

  contacts[name] = phone
  return "Contact added."

@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
  name, phone = args

  if name not in contacts:
    raise KeyError

  contacts[name] = phone
  return "Contact updated."

@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
  name = args[0]
  return contacts[name]

def show_all(contacts: dict[str, str]) -> str:
  if not contacts:
    return "The contacts list is empty."

  lines = [f"{name}: {phone}" for name, phone in contacts.items()]
  return "\n".join(lines)

def main():
  print("Welcome to the assistant bot!")

  contacts = {}

  while True:
    user_input = input("Enter a command: ")
    command, *args = parse_input(user_input)

    match command:
      case "hello":
        print("How can I help you?")
      case "close" | "exit":
        print("Good bye!")
        break
      case "add":
        print(add_contact(args, contacts))
      case "change":
        print(change_contact(args, contacts))
      case "phone":
        print(show_phone(args, contacts))
      case "all":
        print(show_all(contacts))
      case _:
        print("Invalid command.")

if __name__ == "__main__":
  main()
