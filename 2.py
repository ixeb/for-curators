from itertools import *
mz = []
for x in product('ЯРУССКИЙ', repeat=6):
    s = ''.join(x)
    if s[0] != 'У' and s[1] != 'У' and 'ИЙ' in s:
        mz += [s]
print(len(set(mz)))
