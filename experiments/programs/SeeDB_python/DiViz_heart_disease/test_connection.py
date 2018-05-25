from config import config_data
import time,math,numpy as np



def normalization(data):
	z,sum_x = tuple(),0
	for x,y in data:
	    sum_x += y
	for x,y in data:
	    z += ( (x , y/sum_x), )
	return z

def distance(x,y):
	deviance = 0
	dd = dict()
	for i, j in x:
	    dd[i] = j
	for i, j in y:
	    if i in dd:
	        dd[i] = math.fabs(dd[i] - j)
	    else:
	        dd[i] = j
	for x, dis in dd.items():
	    deviance += float(dis)
	return deviance

def query():
	query1 = "select cp, avg(oldpeak) from heart_disease where num = 'no disease' group by cp order by cp"
	query2 = "select cp, avg(oldpeak) from heart_disease where num = 'disease' group by cp order by cp"
	#query1 = "select cp, avg(age) from heart_disease where num = 'no disease' group by cp order by cp"
	#query2 = "select cp, avg(age) from heart_disease where num = 'disease' group by cp order by cp"
	cursor = config_data(db)
	cursor.execute(query1)
	data1 = cursor.fetchall()
	cursor.execute(query2)
	data2 = cursor.fetchall()
	return data1,data2



db = "seedb_data"

data1, data2 = query()
n1 = normalization(data1)
n2 = normalization(data2)

d = distance(n1,n2)
print(data1)
print("\n")
print(data2)
print("\n")
print(len(n1))
print(n1)
print("\n")
print(len(n2))
print(n2)
print(d)