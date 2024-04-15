from itertools import * 
n = 0 
count = 0 
for x in product('ТАЙМИНГ', repeat=8): 
    s = ''.join(x) 
    n += 1 
    count_gl = sum([1 for i in s if i in 'АИ']) 
    count_sgl = sum([1 for i in s if i in 'ТЙМНГ']) 
    if count_gl < count_sgl and n % 2 == 0 and n % 3 != 0: 
        count += 1 
print(count) 
