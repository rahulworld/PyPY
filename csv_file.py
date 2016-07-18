filename='Test.csv'
WRITE='w'
READ='r'
APPEND='a'
WRITEREAD='w+'
#error occuring when use of input from users so try to correct why did thid mistake happen
#dar=input('this is file')
file=open(filename,WRITEREAD)
file.write(dar)
file.write('Rahul Chauhan, 21\n')
file.write('Rohit Chauhan, 19\n')
file.write('Vishwdeep Chauhan,21')
file.close()
print('file written successfully')