# use ordereddict

# a normal dictionary

d = {}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['a'] = 'E'

for k, v in d.items():
    print(k, v)

# an ordered dictionary

from collections import OrderedDict

print('OrderedDict:')

d = OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)
