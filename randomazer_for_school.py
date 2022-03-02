import random
list_1 = []
list_2 = []
ready = {}
inp_peop = ''.split(',')
inp_exes = ''.split(';')
for i in inp_peop:
	try:
		a = str(random.choice(inp_exes))
		i = str(i)
		ready[i] = a
		inp_exes.remove(a)

	except IndexError:
		ready = str(ready)
		ready_ready = ready.replace('{', '')
		ready_ready = ready_ready.replace('}', '')
		ready_ready = ready_ready.replace("'", '')
		print(ready_ready)

ready = str(ready)
ready_ready = ready.replace('{', '')
ready_ready = ready_ready.replace('}', '')
ready_ready = ready_ready.replace("'", '')
print(ready_ready)
