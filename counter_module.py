# use counter from collection module

from collections import Counter

lst = [1,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4]
print(Counter(lst))

# counter with string
print(Counter('aaaaabbbbbbccccc'))

# counter with words in a sentence

s = 'How many time does each word show up in this sentence word times each word'

words = s.split()

print(Counter(words))

# methods with counter()

c = Counter(words)

print(c.most_common(2))