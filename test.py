from collections import defaultdict


tree = defaultdict(list)
list1 = ['s','s','e','w']
counter = 35
res = counter//16
tree[0].extend(list1)
print(tree[0][2])
print()
