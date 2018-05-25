import time
import pandas as pd 
from itertools import product
from itertools import combinations
import functions_collection as fc 



def random_selection(df,k, output):
	# set time before running the function
	timebefore =  time.time()
	df_random = df.sample(k)

	sum_util = sum(df_random['Utility'])/k
	df_random = df_random.drop(['Utility'],axis=1)
	series_set = df_random.apply(lambda row: set(row), axis=1)
	new_df = series_set.apply(lambda a: series_set.apply(lambda b: fc.diversity(a,b)))

	new_df['tot'] = new_df.sum(axis=1)
	sum_div = (sum(new_df['tot'])/2)/(k*(k-1))
	objf = sum_util+sum_div
	timeafter = time.time()    
	procesing_time = str(timeafter - timebefore)
	print("Random,{0},{1}".format(k,procesing_time), file=open(output, "a"))


def seedb(df, k, output):
	# set time before running the function
	timebefore =  time.time()
	df_seedb = df.sort_values(by=['Utility'], ascending=[False]).head(k)
	sum_util = sum(df_seedb['Utility'])/k
	#print(df_seedb, file=open(output, "a"))

	df_seedb = df_seedb.drop(['Utility'],axis=1)
	series_set = df_seedb.apply(lambda row: set(row), axis=1)
	new_df = series_set.apply(lambda a: series_set.apply(lambda b: fc.diversity(a,b)))

	# Adding new column for the sum value by rows
	new_df['tot'] = new_df.sum(axis=1)
	sum_div = (sum(new_df['tot'])/2)/(k*(k-1))
	objf = sum_util+sum_div
	timeafter = time.time()    
	procesing_time = str(timeafter - timebefore)
	print("SBI,{0},{1}".format(k,procesing_time), file=open(output, "a"))


def Greedy_Return_df(df, k):	
	df_greedy = df.drop(['Utility'],axis=1)
	dataset = df_greedy.reset_index(drop=True)
	data = dataset.values.tolist()
	X = data.copy()
	S = fc.most_distant_two_views(data)
	X.remove(S[0])
	X.remove(S[1])
	i = len(S)


	while i < k:    
	    item = fc.dist(X, S)
	    #print(item)
	    if item not in S:
	        S.append(item)
	        X.remove(item)
	    else:
	        pass
	                
	    i = i + 1  

	df_gh = pd.DataFrame(S, columns=['Attributes', 'Meassure', 'Function'])
	df_maxdiv = df_gh.merge(df, how='left')
	
	return df_maxdiv


def Greedy_Heuristic(df, k, output):
	
	timebefore =  time.time()
	
	df_greedy = df.drop(['Utility'],axis=1)
	dataset = df_greedy.reset_index(drop=True)
	data = dataset.values.tolist()
	X = data.copy()
	S = fc.most_distant_two_views(data)
	X.remove(S[0])
	X.remove(S[1])
	i = len(S)

	while i < k:    
	    item = fc.dist(X, S)
	    #print(item)
	    if item not in S:
	        S.append(item)
	        X.remove(item)
	    else:
	        pass
	                
	    i = i + 1  

	df_gh = pd.DataFrame(S, columns=['Attributes', 'Meassure', 'Function'])
	df_maxdiv = df_gh.merge(df, how='left')

	sum_util = sum(df_maxdiv['Utility'])/k
	#print(df_maxdiv, file=open(output, "a"))

	df_maxdiv = df_maxdiv.drop(['Utility'],axis=1)
	series_set2 = df_maxdiv.apply(lambda row: set(row), axis=1)
	new_df2 = series_set2.apply(lambda a: series_set2.apply(lambda b: fc.diversity(a,b)))
	# Adding new column for the sum value by rows
	new_df2['tot'] = new_df2.sum(axis=1)
	sum_div = (sum(new_df2['tot'])/2)/(k*(k-1))
	
	objf = sum_util+sum_div
	timeafter = time.time()    
	procesing_time = str(timeafter - timebefore)
	print("SBD,{0},{1}".format(k,procesing_time), file=open(output, "a"))

def SBDI(df, k, output):
	timebefore =  time.time()
	df_greedy = df.drop(['Utility'],axis=1)
	dataset = df_greedy.reset_index(drop=True)
	data = dataset.values.tolist()
	X = data.copy()
	S = df_greedy.sample(1).values.tolist()
	X.remove(S[0])
	i = len(S)
	while i < k:    
	    item = fc.dist(X, S)
	    #print(item)
	    if item not in S:
	        S.append(item)
	        X.remove(item)
	    else:
	        pass
	                
	    i = i + 1  

	df_gh = pd.DataFrame(S, columns=['Attributes', 'Meassure', 'Function'])
	df_maxdiv = df_gh.merge(df, how='left')

	sum_util = sum(df_maxdiv['Utility'])/k
	#print(df_maxdiv, file=open(output, "a"))

	df_maxdiv = df_maxdiv.drop(['Utility'],axis=1)
	series_set2 = df_maxdiv.apply(lambda row: set(row), axis=1)
	new_df2 = series_set2.apply(lambda a: series_set2.apply(lambda b: fc.diversity(a,b)))
	# Adding new column for the sum value by rows
	new_df2['tot'] = new_df2.sum(axis=1)
	sum_div = (sum(new_df2['tot'])/2)/(k*(k-1))
	
	objf = sum_util+sum_div
	timeafter = time.time()    
	procesing_time = str(timeafter - timebefore)
	print("SBID-Greedy,{0},{1}".format(k,procesing_time), file=open(output, "a"))


def SwapU(df, k, output):
	timebefore =  time.time()
	# Get the N items with the highest utility from dataset as the set X
	SortedRecItems = fc.swap_get_highest_utility(df).reset_index(drop=False)
	# Get the topk from set X with the highest utility
	Retlist = SortedRecItems.head(k).values.tolist()

	X = SortedRecItems.values.tolist()

	# get the original X = X -S
	Retlist_X = Retlist.copy()

	for i in range(0,len(Retlist_X)):
	    X.remove(Retlist_X[i])


	S = Retlist.copy()
	for i in range(0,len(X)):
	    S_ = S.copy()
	    for j in range(0,len(S)):
	        if fc.objf_func(S_) < fc.objf_func_new_set(S, S[j], X[i]):
	            new_S = fc.create_S(S, S[j], X[i])
	            S_ = new_S.copy()
	            #print(S_)
	    if fc.objf_func(S_) > fc.objf_func(S):
	        S = S_.copy()

	df_swapU = pd.DataFrame(S, columns=['index','Attributes', 'Meassure', 'Function','Utility'])

	#print("SwapU Algorithm ------ k = {}".format(k), file=open(output, "a"))

	sum_util = sum(df_swapU['Utility'])/k
	#print(df_swapU, file=open(output, "a"))
	df_swapU = df_swapU.drop(['Utility'],axis=1)
	series_set = df_swapU.apply(lambda row: set(row), axis=1)
	new_df = series_set.apply(lambda a: series_set.apply(lambda b: fc.diversity(a,b)))
	# Adding new column for the sum value by rows
	new_df['tot'] = new_df.sum(axis=1)
	sum_div = (sum(new_df['tot'])/2)/(k*(k-1))

	objf = sum_util+sum_div
	timeafter = time.time()    
	procesing_time = str(timeafter - timebefore)
	print("SBID-SwapI,{0},{1}".format(k,procesing_time), file=open(output, "a"))


def SwapD(df, k, output):
	timebefore =  time.time()
	df_greedy = Greedy_Return_df(df,k)
	Xdf = df.reset_index(drop=True)
	Retlist = df_greedy.values.tolist()

	X = Xdf.values.tolist()


	
	#get the original X = X -S
	Retlist_X = Retlist.copy()

	for i in range(0,len(Retlist_X)):
	    X.remove(Retlist_X[i])

	S = Retlist.copy()
	for i in range(0,len(X)):
	    S_ = S.copy()
	    for j in range(0,len(S)):
	        if fc.objf_func_d(S_) < fc.objf_func_new_set_d(S, S[j], X[i]):
	            new_S = fc.create_S_d(S, S[j], X[i])
	            S_ = new_S.copy()
	            #print(S_)
	    if fc.objf_func_d(S_) > fc.objf_func_d(S):
	        S = S_.copy()

	df_swapD = pd.DataFrame(S, columns=['Attributes', 'Meassure', 'Function','Utility'])

	#print("SwapD Algorithm ------ k = {}".format(k), file=open(output, "a"))

	sum_util = sum(df_swapD['Utility'])/k
	#print(df_swapD, file=open(output, "a"))
	df_swapD = df_swapD.drop(['Utility'],axis=1)
	series_set = df_swapD.apply(lambda row: set(row), axis=1)
	new_df = series_set.apply(lambda a: series_set.apply(lambda b: fc.diversity(a,b)))
	# Adding new column for the sum value by rows
	new_df['tot'] = new_df.sum(axis=1)
	sum_div = (sum(new_df['tot'])/2)/(k*(k-1))

	objf = sum_util+sum_div
	timeafter = time.time()    
	procesing_time = str(timeafter - timebefore)
	print("SBID-SwapD,{0},{1}".format(k,procesing_time), file=open(output, "a"))


# x_df = pd.DataFrame(X, columns=['Attributes', 'Meassure', 'Function']) 
# x_df['div'] = x_df[['Attributes', 'Meassure', 'Function']].apply(lambda row: fc.div_compute(row,S), axis=1)
# x_df['max'] = x_df['div'].apply(lambda row: fc.max_compute(row))
# x_df['min'] = x_df['div'].apply(lambda row: fc.min_compute(row))
# min_max = min(x_df['max'])
# max_min = max(x_df['min'])
# new_df = x_df[x_df['max'] > max_min]
# df_good = new_df.merge(df, how='left')
# df_good['objf'] = df_good['div'] + df_good['Utility']
# best_view_id = df_good['objf'].argmax()
# best_view = df_good.iloc[best_view_id]
# best_view = list([best_view[0], best_view[1], best_view[2]])
# item = best_view

# def pGreedyPruning(df, k, output):
# 	timebefore =  time.time()
# 	df_greedy = df.drop(['Utility'],axis=1)
# 	dataset = df_greedy.reset_index(drop=True)
# 	data = dataset.values.tolist()
# 	X = data.copy()
# 	S = df_greedy.sample(1).values.tolist()
# 	X.remove(S[0])
# 	i = len(S)
# 	while i < k:
# 		x_df = pd.DataFrame(X, columns=['Attributes', 'Meassure', 'Function']) 
# 		x_df['div'] = x_df[['Attributes', 'Meassure', 'Function']].apply(lambda row: fc.div_compute(row,S), axis=1)
# 		x_df = x_df.merge(df, how='left')
# 		x_df['objf'] = x_df['div'] + x_df['Utility']
# 		x_df = x_df.sort_values(by=['objf'], ascending=[False])   
# 		top = x_df.head(1).values.tolist()
# 		top_item = list([top[0][0],top[0][1],top[0][2]])
# 		item = top_item
# 		#print(item)
# 		if item not in S:
# 			S.append(item)
# 			X.remove(item)
# 		else:
# 			pass

# 		i = i + 1  

# 	df_pg = pd.DataFrame(S, columns=['Attributes', 'Meassure', 'Function'])
# 	df_pg_result = df_pg.merge(df, how='left')
# 	sum_util = sum(df_pg_result['Utility'])/k
# 	#print(df_maxdiv, file=open(output, "a"))

# 	df_pg_result = df_pg_result.drop(['Utility'],axis=1)
# 	series_set2 = df_pg_result.apply(lambda row: set(row), axis=1)
# 	new_df2 = series_set2.apply(lambda a: series_set2.apply(lambda b: fc.diversity(a,b)))
# 	# Adding new column for the sum value by rows
# 	new_df2['tot'] = new_df2.sum(axis=1)
# 	sum_div = (sum(new_df2['tot'])/2)/(k*(k-1))

# 	objf = sum_util+sum_div
# 	timeafter = time.time()    
# 	procesing_time = str(timeafter - timebefore)
# 	print("pGreedyPruning,{0},{1}".format(k,procesing_time), file=open(output, "a"))

# def SwapDPruning(df, k, output): 
# 	timebefore =  time.time()
# 	df_greedy = Greedy_Return_df(df,k)
# 	SortedRecItems = fc.swap_get_highest_utility(df).reset_index(drop=True)
# 	#SortedRecItems = SortedRecItems.drop('Utility', axis=1)
# 	Retlist = df_greedy.values.tolist()

# 	X = SortedRecItems.values.tolist()

	
# 	#get the original X = X -S
# 	Retlist_X = Retlist.copy()

# 	for i in range(0,len(Retlist_X)):
# 	    X.remove(Retlist_X[i])
# 	#print(X)
# 	S = Retlist.copy()
# 	for i in range(0,len(X)):
# 	    S_ = S.copy()
# 	    for j in range(0,len(S)):
# 	        if fc.objf_func_d(S_) < fc.objf_func_new_set_d(S, S[j], X[i]):
# 	            new_S = fc.create_S_d(S, S[j], X[i])
# 	            S_ = new_S.copy()
# 	            #print(S_)
# 	    if fc.objf_func_d(S_) > fc.objf_func_d(S):
# 	        S = S_.copy()

# 	df_swapDPrun = pd.DataFrame(S, columns=['Attributes', 'Meassure', 'Function','Utility'])

# 	#print("SwapD Algorithm ------ k = {}".format(k), file=open(output, "a"))

# 	sum_util = sum(df_swapDPrun['Utility'])/k
# 	#print(df_swapD, file=open(output, "a"))
# 	df_swapDPrun = df_swapDPrun.drop(['Utility'],axis=1)
# 	series_set = df_swapDPrun.apply(lambda row: set(row), axis=1)
# 	new_df = series_set.apply(lambda a: series_set.apply(lambda b: fc.diversity(a,b)))
# 	# Adding new column for the sum value by rows
# 	new_df['tot'] = new_df.sum(axis=1)
# 	sum_div = (sum(new_df['tot'])/2)/(k*(k-1))

# 	objf = sum_util+sum_div
# 	timeafter = time.time()    
# 	procesing_time = str(timeafter - timebefore)
# 	print("SwapDPruning,{0},{1}".format(k,procesing_time), file=open(output, "a"))




### Running the application.

xl = pd.ExcelFile("results_carrier_US_norm.xlsx")
df = xl.parse("Sheet1", header=0)

number_of_k = [5,15,25,35] #
output = "output_time_flights.csv"
n = len(df)

for k in number_of_k:
	random_selection(df,k, output)
	seedb(df, k, output)
	Greedy_Heuristic(df, k, output)
	SBDI(df, k, output)
	SwapU(df, k, output)
	SwapD(df, k, output)
	# pGreedyPruning(df, k, output)
	# SwapDPruning(df, k, output)
