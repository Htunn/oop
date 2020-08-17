# use defaultdic from collections

from collections import defaultdict

d = {}
d = defaultdict(object)
print(d['one'])

for item in d:
    print(item)

# initialize with default value

d = defaultdict(lambda: 0)
print(d['one'])