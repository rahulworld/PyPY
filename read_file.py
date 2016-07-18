filename='Test.csv'
WRITE='w'
READ='r'
APPEND='a'
WRITEREAD='w+'
#error occuring when use of input from users so try to correct why did thid mistake happen
#dar=input('this is file')
file=open(filename,mode=READ)
allFileContent=filename.read()
print(allFileContent)
print('file written successfully')