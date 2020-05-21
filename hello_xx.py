print('hello')
import time

def hello_func(n, t):
	for i in range(n):
		print('sleep in %d' % (i) )
		time.sleep(t)
hello_func(10,20)
