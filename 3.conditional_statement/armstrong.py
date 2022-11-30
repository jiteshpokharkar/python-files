'''
A three digit number is entered by user.Write a program
to find whether number is armstrong number.

n=153


sum of cube of digit=original number

1**3+5**3+3**3=1+125+27=153
step1:start
step2:digit separation => %,// 10
step3:cube and add or summation.
step4:check summation is equal to number entered by user.
step5:if it found same then it is armstrong number
step6:otherwise it is not an armstrong number.
step7:stop.
'''
#153


print('enter three digit number:')
n=int(input())  #234

a=n%10   #a=234%10=4
b=n//10  #b=234//10=23
c=b%10   #c=23%10=3
d=b//10  #d=23//10=2

s=a**3+c**3+d**3

if s==n:
    print('armstrong number')

else:
    print('not armstrong number')
