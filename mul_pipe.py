from multiprocessing import Queue,Process,Pool,Pipe,Manager
import os,time,random

def proc_one(lst):#():
	s = 'Hello, I am proc_one'
	#pipe.send(s)
	lst.append(s)
	print("proc_one add data :%s"%s)

def proc_two(lst):#(pipe):
	#if pipe.poll():
	#	print('proc_two receives: {}'.format(pipe.recv()))
	#else: return
	s = 'Hello, I am proc_two!'
	lst.append(s)
	print("proc_two add data: %s"%s)

#if name == "main":
#pipe = Pipe()
m = Manager()
lst = m.list()
#p1 = Process(target = proc_one, args = (pipe[0],))
p1 = Process(target = proc_one, args = (lst,))
#p2 = Process(target = proc_two, args = (pipe[1],))
p2 = Process(target = proc_two, args = (lst,))
p1.start()
p2.start()
p1.join()
p2.join(2)
print("run ends")
print(lst)
