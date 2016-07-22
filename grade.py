print('**this is your result**\n')
print('===========================')
math=int(input('enter number of math'))
phy=int(input('enter number of physics'))
chem=int(input('enter number of chemistry'))
hindi=int(input('enter number of hindi'))
eng=int(input('enter number of english'))
print('your math marks      %d\n'%math)
print('your physics marks       %d\n'%phy)
print('your chemistry marks       %d\n'%chem)
print('your hindi marks       %d\n'%hindi)
print('your english marks       %d\n'%eng)
tot=math+phy+chem+hindi+eng
per=tot/5
print('your total marks is       %d\n'%tot)
print('your percentage is       %d\n'%per)
if per<40:
	print('you are fail')
elif per<75:
	print('your grade is B')
elif
	print('your is first division')
else
	print('your result not found')