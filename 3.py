from itertools import * 
count_putin = 0 
count_baiden = 0  
for x in product('ПУТИН', repeat=5):  
    s = ''.join(x)  
    s_putin = 'ПТН'   
    for i in s_putin:
        s = s.replace(i, '*') 
    if '**' not in s: 
        count_putin += 1
for x in product('БАЙДЕН', repeat=5):  
    s = ''.join(x)   
    s_baiden = 'БЙДН' 
    for i in s_baiden:
        s = s.replace(i, '*')  
    if '**' not in s: 
        count_baiden += 1  
print(max(count_putin, count_baiden))  
