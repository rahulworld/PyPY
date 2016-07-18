filename='demo.txt'
WRITE='w'
READ='r'
APPEND='a'
WRITEREAD='w+'
file=open(filename,WRITEREAD)
file.write('this is python file making in sublime text\n')
file.write('this is a second line in which we write the code')
file.close()
print('thid is correct in w plus mode we can write and read both')