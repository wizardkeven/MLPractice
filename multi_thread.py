import os
from multiprocessing import Queue, Process,Pool
import time,random

#create queue, no arg means no size limitation

global lst
lst = []

q = Queue()
#for i in range(10):
#	q.put(i)

def run_q(name,v):
	#while True:
		try:
			#global lst
			#lst.append(v)
			#print(lst)
			#p_v = q.get_nowait()
			#print("I am process %s, get value: %d"%(name,p_v))
			q.put(v)
			time.sleep(random.random())
		except Exception as e:
			print(e)
			#break
pool = Pool(2)

def run_proc(process_name):
	print('Child process name is %s, process ID is %s'%(process_name, os.getpid()))
	start = time.time()
	time.sleep(random.random()*5)
	end = time.time()
	print('Task is %s runs %0.2f seconds.'%(process_name,(end - start)))
	print('Child process work end')

#print('Parent process ID is %s'% os.getpid())
#print('Parent process start working')

#target: the specific function which the process execute, args: the arguments of the function(tuple)
#p = Process(target=run_proc, args=('child_thread1',))
#p = Pool()

for i in range(4):
#	p.apply_async(run_proc,args=(i,))
	pool.apply_async(run_q,(i,i,))

#print('Child process start working')
#p.start()
pool.close()
pool.join()

#print(lst)
v = q.get()
try:
	while v is not None:
		print(v)
		v=q.get(block=False)
except Exception as e:
	pass
#print("Parent process work end")

