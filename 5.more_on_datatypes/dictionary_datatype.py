'''
1)Dictionary is also a collection of dissimilar elements.
2)Elements in dictionary are arranged in key:value format.
3)They are mutable.
4)keys are unique and values can be duplicated.
5)Elements are enclosed in curly braces.

'''


d={'a':'apple','b':'ball',2:'two',10:100}
print(d)
print(type(d))



#len()
n=len(d)
print('total number of element in dictionary:',n)

#indexing or accessing with index=no since there is no index.
#But since there is key which is unique we can access element
#value using key
'''
   dictionary_variable[keyname]
'''

print(d['b'])
print(d[10])


#slicing not possible as it require index.

#for loop
#for loop using index is not possible.

for x in d:
    
    print(d[x])#d['a'],d['b'],d[2],d[10]


#add element in dictionary.
    
d['c']='Cat'
print(d)

#update dictionary.
d['b']='bat'
print(d)

# to remove dictionary element
d.pop(2)
print(d)

del d

print(d)




























