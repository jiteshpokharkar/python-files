'''
A character is entered by user,write a program to check
whether that character is equal to a or b or c.

'''
#q==a or q==b or q==c => F or F or F => F
#A==a or A==b or A==c => F or F or F => F


ch=input('enter character:')
if ch=='a' or ch=='b' or ch=='c':
    print('character found!!!')

else:
    print("not found")
