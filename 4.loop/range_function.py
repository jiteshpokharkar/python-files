'''
range():This function generate list of numbers in a sequence.
syntax:

     range(start,stop,step)

     start=> initialization
     stop => conditon
     step => increment/decrement [positive or negative]
     
'''
'''
x=list(range(1,15,1))
print(x)
'''

'''
#no step
x=list(range(2,20))
print(x)
'''

'''
#no step and start
x=list(range(20))
print(x)
'''

'''
x=list(range())# erroe as range() require atleast one ergument.
print(x)
'''
'''
Traceback (most recent call last):
  File "C:/python730/loop/range_function.py", line 29, in <module>
    x=list(range())
TypeError: range expected at least 1 argument, got 0
'''


x=list(range(15,5,-2))
print(x)





