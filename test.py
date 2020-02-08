from collections import defaultdict
import textwrap

tree = defaultdict(list)
list1 = ['s','s','e','w']
counter = 35
res = counter//16
tree[0].extend(list1)

textArray = "3 5 50 110100110".split()

stringgiy = textwrap.wrap(textArray[3], 3)

if isinstance(stringgiy[0], int):
    print("its an int lol")
if isinstance(stringgiy[0], str):
    print("its a string lol")

print(stringgiy[0])
print()
