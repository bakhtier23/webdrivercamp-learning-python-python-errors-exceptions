#!/usr/bin/python3
def list_int_print(lst=[], i=0):
  count = 0
  for element in lst[:i]:
    try:
      if isinstance(element, int):
        print(f"{element:d}", end=" ")
        count += 1
    except Exception:
      pass
  print()
  return count

list_ = [1, 2, 3, 4, 5, 6, 7]

count = list_int_print(list_, 4)
print(f"Count: {count:d}")

list_ = [1, 2, "Camp", 5, [3, 4]]
count = list_int_print(list_, len(list_))
print(f"Count: {count:d}")
count = list_int_print(list_, len(list_) + 2)
print(f"Count: {count:d}")
