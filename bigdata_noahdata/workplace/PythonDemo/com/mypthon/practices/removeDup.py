'''
Created on 04-Sep-2017

@author: bigdata
'''
import itertools
from collections import defaultdict, Counter
from heapq import nlargest
result = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
print "Original:", result
u_value = set(val for dic in result for val in dic.values())
print "Unique dic:", u_value
new_dic = {}
for x in result:
    for a, y in x.items():
        new_dic[a] = y
print new_dic   

d = {'1':['a', 'b'], '2':['c', 'd']} 
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo)) 
my_dict = {'a':500, 'b':5874, 'c': 560, 'd':400, 'e':5874, 'f': 20} 

three_largest = nlargest(3, my_dict, my_dict.get)
print three_largest

dic_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for d in dic_list:
    result[d['item']] += d['amount']
print result   

str = "w3resource"
my_str_dic = {}
for letter in str:
    my_str_dic[letter] = my_str_dic.get(letter, 0) + 1
print my_str_dic    


my_dict_tab = {'C1':[1, 2, 3], 'C2':[5, 6, 7], 'C3':[9, 10, 11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict_tab.items()))):
    print(row)
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
for d in student:
    print d

print(sum(d['success'] for d in student ))    
    
