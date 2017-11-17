'''
Created on 12-Sep-2017

@author: bigdata
'''
from heapq import nlargest
ls=[1,2,3,1,2,10,45,4,77]
def match_words(words):
    ctr = 0
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
    return ctr
print(match_words(['abc', 'xyz', 'aba', '1221']))

tup=(1,3,4,5,6,4)

lsoftu=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def last(n): return n[-1]

def sort_list_last(tuples):
    return sorted(tuples, key=last)
print sort_list_last(lsoftu)
a = [10,20,30,20,10,50,60,40,80,50,40]

dup_item=set()
uni_item=[]
for c in a:
    if c not in dup_item:
        uni_item.append(c)
        dup_item.add(c)
        
print uni_item        

word_str ="The quick brown fox jumps over the lazy dog"
word_ls= word_str.split(" ")
new_ls=[]
for l in word_ls:
    if len(l)>3:
        new_ls.append(l)

print new_ls
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color=[x for (i,x) in enumerate(color) if i not in (0,2,4)]
print color
for (i,x) in enumerate(color):
    print i,x

con=[1,3,7,6,18,9,32,50,60]
oddlsn=[x for x in con if (x%2!=0)]
print oddlsn
oddls=[]
for e in con:
    if (e%2!=0):
        oddls.append(e)
print oddls             
