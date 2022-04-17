from typing import List


strings: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

my_zip: List[tuple] = list(map(lambda x, y: (x, y), strings, numbers))
print(my_zip)