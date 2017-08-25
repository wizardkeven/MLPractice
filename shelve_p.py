import shelve

s = shelve.open('test.db',writeback = True)
s.clear()

#t=s['x']
#t.append(5)
#s['x'] =t
try:
    s['x'] = [1,2,3,4]
    s['x'].append(5)
except Exception as e:
    print('Exception msg is %s :'%e)
finally:
    s.close()

s=shelve.open('test.db',writeback=True)
print(s['x'])
