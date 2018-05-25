import datetime
import os
import pandas as pd 
from itertools import product
from itertools import combinations
import functions_collection_div_weight as fc 


def Only_Interestingness(df, tr, output):
	# set time before running the function
	timebefore =  datetime.datetime.now()
	df_seedb = df.sort_values(by=['Utility'], ascending=[False]).head(k)
	sum_util = (sum(df_seedb['Utility'])/k)/2
	#print(df_seedb, file=open(output, "a"))

	df_seedb = df_seedb.drop(['Utility'],axis=1)
	series_set = df_seedb.apply(lambda row: set(row), axis=1)
	new_df = series_set.apply(lambda a: series_set.apply(lambda b: fc.diversity(a,b)))

	# Adding new column for the sum value by rows
	new_df['tot'] = new_df.sum(axis=1)
	sum_div = ((sum(new_df['tot'])/2)/(k*(k-1)))/2
	objf = ( (1 - tr) * sum_util) + (tr *sum_div)
	timeafter = datetime.datetime.now()    
	procesing_time = str(timeafter - timebefore)
	print("Only Interestingness,{0},{1},{2},{3},{4}".format(tr,sum_util,sum_div,objf,procesing_time), file=open(output, "a"))

def Greedy_Return_df(df, tr):	
	
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


def Only_Diversity(df, tr, output):
	
	timebefore =  datetime.datetime.now()
	
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

	sum_util = (sum(df_maxdiv['Utility'])/k)/2
	#print(df_maxdiv, file=open(output, "a"))

	df_maxdiv = df_maxdiv.drop(['Utility'],axis=1)
	series_set2 = df_maxdiv.apply(lambda row: set(row), axis=1)
	new_df2 = series_set2.apply(lambda a: series_set2.apply(lambda b: fc.diversity(a,b)))
	# Adding new column for the sum value by rows
	new_df2['tot'] = new_df2.sum(axis=1)
	sum_div = (sum(new_df2['tot'])/2)/(k*(k-1))/2
	
	objf = sum_util+sum_div
	timeafter = datetime.datetime.now()    
	procesing_time = str(timeafter - timebefore)
	print("Only Diversity,{0},{1},{2},{3},{4}".format(tr,sum_util,sum_div,objf,procesing_time), file=open(output, "a"))

def iDiVE_Greedy(df, tr, output):
	timebefore =  datetime.datetime.now()
	df_greedy = df.drop(['Utility'],axis=1)
	dataset = df_greedy.reset_index(drop=True)
	data = dataset.values.tolist()
	X = data.copy()
	S = fc.most_distant_two_views(data)
	X.remove(S[0])
	X.remove(S[1])
	i = len(S)

	while i < k:    
	    item = fc.objf_dist(df, X, S)
	    #print(item)
	    if item not in S:
	        S.append(item)
	        X.remove(item)
	    else:
	        pass
	                
	    i = i + 1  

	df_pg = pd.DataFrame(S, columns=['Attributes', 'Meassure', 'Function'])
	df_pg_result = df_pg.merge(df, how='left')
	sum_util = (sum(df_pg_result['Utility'])/k)/2
	#print(df_maxdiv, file=open(output, "a"))

	df_pg_result = df_pg_result.drop(['Utility'],axis=1)
	series_set2 = df_pg_result.apply(lambda row: set(row), axis=1)
	new_df2 = series_set2.apply(lambda a: series_set2.apply(lambda b: fc.diversity(a,b)))
	# Adding new column for the sum value by rows
	new_df2['tot'] = new_df2.sum(axis=1)
	sum_div = (sum(new_df2['tot'])/2)/(k*(k-1))/2

	objf = sum_util+sum_div
	timeafter = datetime.datetime.now()    
	procesing_time = str(timeafter - timebefore)
	print("i-DiVE Greedy,{0},{1},{2},{3},{4}".format(tr,sum_util,sum_div,objf,procesing_time), file=open(output, "a"))

def iDiVE_SwapI(df, tr, output):
	timebefore =  datetime.datetime.now()
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
	improve = True
	objf_current_S = 0.0
	while (improve == True):
		for i in range(0,len(X)):
		    S_ = S.copy()
		    for j in range(0,len(S)):
		        if fc.objf_func(S_) < fc.objf_func_new_set(S, S[j], X[i]):
		            new_S = fc.create_S(S, S[j], X[i])
		            S_ = new_S.copy()
		            #print(S_)
		    if fc.objf_func(S_) > fc.objf_func(S):
		        S = S_.copy()
		    print("X ke {}".format(i))
		objf = fc.objf_func(S)
		if objf > objf_current_S:
			objf_current_S = objf
			improve = True 
			print("need improve")
		else:
			improve = False
			print("no improve")


	df_swapU = pd.DataFrame(S, columns=['index','Attributes', 'Meassure', 'Function','Utility'])

	#print("SwapU Algorithm ------ k = {}".format(k), file=open(output, "a"))

	sum_util = (sum(df_swapU['Utility'])/k)/2
	#print(df_swapU, file=open(output, "a"))
	df_swapU = df_swapU.drop(['Utility'],axis=1)
	series_set = df_swapU.apply(lambda row: set(row), axis=1)
	new_df = series_set.apply(lambda a: series_set.apply(lambda b: fc.diversity(a,b)))
	# Adding new column for the sum value by rows
	new_df['tot'] = new_df.sum(axis=1)
	sum_div = (sum(new_df['tot'])/2)/(k*(k-1))/2

	objf = sum_util+sum_div
	timeafter = datetime.datetime.now()    
	procesing_time = str(timeafter - timebefore)
	print("i-DiVE-SwapI,{0},{1},{2},{3},{4}".format(tr,sum_util,sum_div,objf,procesing_time), file=open(output, "a"))



def iDiVE_SwapD(df, tr, output):
	timebefore =  datetime.datetime.now()
	df_greedy = Greedy_Return_df(df,k)
	Xdf = df.reset_index(drop=True)
	Retlist = df_greedy.values.tolist()

	X = Xdf.values.tolist()


	
	#get the original X = X -S
	Retlist_X = Retlist.copy()

	for i in range(0,len(Retlist_X)):
	    X.remove(Retlist_X[i])

	S = Retlist.copy()
	improve = True
	objf_current_S = 0.0
	while (improve == True):
		for i in range(0,len(X)):
		    S_ = S.copy()
		    for j in range(0,len(S)):
		        if fc.objf_func_d(S_) < fc.objf_func_new_set_d(S, S[j], X[i]):
		            new_S = fc.create_S_d(S, S[j], X[i])
		            S_ = new_S.copy()
		            #print(S_)
		    if fc.objf_func_d(S_) > fc.objf_func_d(S):
		        S = S_.copy()
		    print("X ke {}".format(i))
		objf = fc.objf_func_d(S)
		if objf > objf_current_S:
			objf_current_S = objf
			improve = True 
			print("need improve")
		else:
			improve = False
			print("no improve")

	df_swapD = pd.DataFrame(S, columns=['Attributes', 'Meassure', 'Function','Utility'])

	#print("SwapD Algorithm ------ k = {}".format(k), file=open(output, "a"))

	sum_util = (sum(df_swapD['Utility'])/k)/2
	#print(df_swapD, file=open(output, "a"))
	df_swapD = df_swapD.drop(['Utility'],axis=1)
	series_set = df_swapD.apply(lambda row: set(row), axis=1)
	new_df = series_set.apply(lambda a: series_set.apply(lambda b: fc.diversity(a,b)))
	# Adding new column for the sum value by rows
	new_df['tot'] = new_df.sum(axis=1)
	sum_div = (sum(new_df['tot'])/2)/(k*(k-1))/2

	objf = sum_util+sum_div
	timeafter = datetime.datetime.now()    
	procesing_time = str(timeafter - timebefore)
	print("i-DiVE-SwapD,{0},{1},{2},{3},{4}".format(tr,sum_util,sum_div,objf,procesing_time), file=open(output, "a"))




### Running the application.

xl = pd.ExcelFile("flights_results3.xlsx")
df = xl.parse("Sheet1", header=0)
#os.remove("pruned_objf_flights1.csv")
k = 5
tradeoff_list = [0, 0.1, 0.2, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
#number_of_k = [5,15,25,35] #
output = "div_weight_objf_superstore.csv"
n = len(df)

for tr in tradeoff_list:
	Only_Interestingness(df, tr, output)
	Only_Diversity(df, tr, output)
	iDiVE_Greedy(df, tr, output)
	iDiVE_SwapI(df, tr, output)
	iDiVE_SwapD(df, tr, output)



