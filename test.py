from collections import defaultdict


tree = defaultdict(list)
list1 = ['s','s','e','w']
tree[0].extend(list1)
print(tree[0])
