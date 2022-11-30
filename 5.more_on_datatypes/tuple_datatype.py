'''
tuple
=====
1)It is collection of dissimilar datatype elements.
2)Elements in the tuple are enclosed in round brackets [parenthesis]
3)They are immutable.
'''

t=(10,20,'itveant',89.9,'eclass')
print(t)
print(type(t))

#len()

n=len(t)
print('total number of elements in tuple:',n)



#accessing tuple element with index
'''
                        t
          (10,20,'Itvedant',89.9,'Eclass')
           0  1      2       3       4
           -5-4     -3      -2      -1

     syntax:

            tuple_variable[index_pos]

            
'''



'''
Two methods or function supported in tuple.
1)count():It is  used to count occurance of the element in the
          tuple.
2)index():This method or function returns index of the
          elements given.

'''

n=t.count(20)
print('total number of count:',n)


ipos=t.index(89.9)
print('index position is:',ipos)

'''
for i in range(0,len(t)):

    if t[i]==20:

        print(i)

'''

del t

print(t)































