'''
A three digit number is enetered through keyboard. Write a
program to
a) reverse that digit.
b) Sum of digits.

a)
     input                      output 
    n=675  -----> logic ------>  576
b)  n=675 ------> logic ------>  6+7+5=18

    675=6*100+7*10+5*1

    576=5*100+7*10+6*1

    sum=6+7+5

    digit separation => % and // with divisor 10
    reverse number formation
'''

print('enter three digit number:') #234
x=input()

n=int(x)
a=n%10    #a=234%10=4
b=n//10   #b=234//10=23
c=b%10    #c=23%10=3
d=b//10   #d=23//10=2

rev=a*100+c*10+d*1
print('original value:',n)
print('reverse value:',rev)


#summation of the digits
s=a+c+d
print('summation is value:',s)












