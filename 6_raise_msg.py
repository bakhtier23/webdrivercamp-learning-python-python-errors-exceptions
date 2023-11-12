#!/usr/bin/python3

def raise_message(message=""):
  """Raises a name exception with a message.

  Args:
    message: The message to include in the exception.
  """
  raise NameError(message)

if __name__ == "__main__":
    try:
        raise_message("I love Python!")
    except NameError as ne:
        print(ne)
