import subprocess
mylist = ['carrier = "US"', 'carrier = "AA"']

for i in mylist:
	subprocess.run('python main.py {}'.format(i))
