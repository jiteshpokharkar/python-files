'''

greatest of three using logical operator

'''


a=int(input('enter first number:'))
b=int(input('enter second number:'))
c=int(input('enter third number:'))

if a>b and a>c:
    print(a,'is greater.')

if b>a and b>c:
    print(b,'is greater.')

if c>a and c>b:
    print(c,'is greater.')


'''
In user input of a=70,b=50,c=20
First if condition is evaluated to be True and we
got the result of greatest of three numbers.

If we got the result in first if condition, then
ideally there is no need to check further if conditions.
Since in above program its checking other two condition,
there is waster of interpreter time in code execution
which is not  going to give us output.



'''































