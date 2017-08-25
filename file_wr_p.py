import fileinput

f = open('my_file.txt', mode='w')

data = ['hello world!\n','yes!']
data*=100
#f.write('hello world!')
#f.seek(2)
#f.write("xxxxxxxxxx")
f.writelines(data)
f.close()


for line in fileinput.input('my_file.txt'):
    print(line)
#f = open('my_file.txt', mode='r')
#print(f.read()+'\n')
#f.close()

#f = open('my_file.txt', mode='r')
#print(f.readline()+'\n')
#f.close()

#f=open('my_file.txt',mode = 'r')
#print(f.readlines())
#f.close()
