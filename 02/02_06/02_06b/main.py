# Tuples are immutable array-like structures

my_list = [8, 5, 0, 3, 9, 7]
ITEM = 8

def search(item, listy):
  for element in listy:
    if element == item:
      return True
  else:
    return False


ITEM_INDEX = my_list.index(ITEM)
print(ITEM_INDEX)