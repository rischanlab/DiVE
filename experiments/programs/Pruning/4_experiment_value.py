import datetime
import os
import pandas as pd 
import math
from itertools import product
from itertools import combinations
from operator import itemgetter
import mei_functions_collection_div_weight as fc 


def util_func_d(S_list):
    max_I = math.sqrt(2)
    new_df = pd.DataFrame(S_list)
    utility = (sum(new_df[3])/len(new_df))/max_I
    return utility

def div_func_d(S_list):
    k = len(S_list)
    new_df = pd.DataFrame(S_list)
    df_now = new_df.drop([3], axis=1)
    S_list_now = df_now.values.tolist()
    new_series = pd.Series(S_list_now)
    series_set = new_series.apply(lambda row: set(row))
    new_df = series_set.apply(lambda a: series_set.apply(lambda b: fc.diversity(a,b)))
    new_df['tot'] = new_df.sum(axis=1)
    div = (sum(new_df['tot'])/2)/(k*(k-1))
    return div

def objf_func_d(S, tradeoff):
    util = util_func_d(S)
    div = div_func_d(S)
    objf = ((1-tradeoff)*util)+(tradeoff*div)
    return objf

# def objf_func_new_set_d(S, X, Y, tradeoff, max_bound):
#     new_S = S.copy()
#     new_S.remove(X)
#     new_S.append(Y)
#     util = util_func_d(new_S)
#     div = div_func_d(new_S)
#     objf = ((1-tradeoff)*util)+(tradeoff*div)
#     return objf

def objf_func_new_set_d(S, X, Y, tradeoff, max_bound):
    new_S = S.copy()
    new_S.remove(X)
    
    temp_S = new_S.copy()
    temp_Y = Y.copy()
    temp_Y[3] = max_bound
    temp_S.append(temp_Y)
    temp_util = util_func_d(temp_S)
    temp_div = div_func_d(temp_S)
    temp_objf = ((1-tradeoff)*temp_util)+(tradeoff*temp_div)
    objf = temp_objf
    return objf

def create_S_d(S, X, Y):
    new_S = S.copy()
    new_S.remove(X)
    new_S.append(Y)
    return new_S

def div_new_set_d(S, X, Y):
    new_S = S.copy()
    new_S.remove(X)
    new_S.append(Y)
    #util = util_func_d(new_S)
    div = fc.div_func_d(new_S)
    #objf = (util+div)
    return div

def get_maxI_score(S):
    max_I = 0
    for i in range(0,len(S)):
        if S[i][3] > max_I:
            max_I = S[i][3]
    return max_I

def get_importance_score(v):
    return v[3]

def Only_Interestingness(df, k, output):
	# set time before running the function
	
	timebefore =  datetime.datetime.now()
	df_seedb = df.sort_values(by=['Utility'], ascending=[False]).head(k)
	sum_util = ((sum(df_seedb['Utility'])/k)/2)/max_i_score
	#print(df_seedb, file=open(output, "a"))

	df_seedb = df_seedb.drop(['Utility'],axis=1)
	series_set = df_seedb.apply(lambda row: set(row), axis=1)
	new_df = series_set.apply(lambda a: series_set.apply(lambda b: fc.diversity(a,b)))

	# Adding new column for the sum value by rows
	new_df['tot'] = new_df.sum(axis=1)
	sum_div = ((sum(new_df['tot'])/2)/(k*(k-1)))/2
	objf = sum_util+sum_div
	timeafter = datetime.datetime.now()    
	procesing_time = str(timeafter - timebefore)
	print("Only Interestingness,{0},{1},{2},{3},{4}".format(k,sum_util,sum_div,objf,procesing_time), file=open(output, "a"))

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


def Only_Diversity(df, k, output):
	
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

	sum_util = (sum(df_maxdiv['Utility'])/k)/2/max_i_score
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
	print("Only Diversity,{0},{1},{2},{3},{4}".format(k,sum_util,sum_div,objf,procesing_time), file=open(output, "a"))

def iDiVE_Greedy(df, k, output):
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
	# while i < k:
	# 	x_df = pd.DataFrame(X, columns=['Attributes', 'Meassure', 'Function']) 
	# 	x_df['div'] = x_df[['Attributes', 'Meassure', 'Function']].apply(lambda row: fc.div_compute(row,S), axis=1)
	# 	x_df = x_df.merge(df, how='left')
	# 	x_df['objf'] = x_df['div'] + x_df['Utility']
	# 	x_df = x_df.sort_values(by=['objf'], ascending=[False])   
	# 	top = x_df.head(1).values.tolist()
	# 	top_item = list([top[0][0],top[0][1],top[0][2]])
	# 	item = top_item
	# 	#print(item)
	# 	if item not in S:
	# 		S.append(item)
	# 		X.remove(item)
	# 	else:
	# 		pass

	# 	i = i + 1  

	df_pg = pd.DataFrame(S, columns=['Attributes', 'Meassure', 'Function'])
	df_pg_result = df_pg.merge(df, how='left')
	sum_util = (sum(df_pg_result['Utility'])/k)/2/max_i_score
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
	print("i-DiVE Greedy,{0},{1},{2},{3},{4}".format(k,sum_util,sum_div,objf,procesing_time), file=open(output, "a"))

def iDiVE_SwapI(df, k, output):
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

	sum_util = (sum(df_swapU['Utility'])/k)/2/max_i_score
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
	print("i-DiVE-SwapI,{0},{1},{2},{3},{4}".format(k,sum_util,sum_div,objf,procesing_time), file=open(output, "a"))



def iDiVE_SwapD(df, k, output):
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

	sum_util = (sum(df_swapD['Utility'])/k)/2/max_i_score
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
	print("i-DiVE-SwapD,{0},{1},{2},{3},{4}".format(k,sum_util,sum_div,objf,procesing_time), file=open(output, "a"))

def div_new_set_d(S, X, Y):
    new_S = S.copy()
    new_S.remove(X)
    new_S.append(Y)
    #util = util_func_d(new_S)
    div = fc.div_func_d(new_S)
    #objf = (util+div)
    return div


def iDiVE_SwapD_Pruning(df, k, output):
	tradeoff = 0.5
	timebefore =  datetime.datetime.now()
	df_greedy = Greedy_Return_df(df,k)

	Xdf = df.sample(len(df)).reset_index(drop=True)
	Retlist = df_greedy.values.tolist()
	X = Xdf.values.tolist()
	#get the original X = X -S
	Retlist_X = Retlist.copy()
	for i in range(0,len(Retlist_X)):
	    X.remove(Retlist_X[i])

	S = Retlist.copy()

	max_bound = math.sqrt(2)
	X_not_pruned_hypothetical = []
	X_not_pruned_max_actual = []
	maxI_q = 0
	count_q = 0
	pi_sample = 9

	improve = True
	objf_current_S = 0.0
	while (improve == True):
		X_sorted = []
		X_data = []
		d = 0
		for i in range(0,len(X)):
		    for j in range(0,len(S)):
		        d = div_new_set_d(S, S[j], X[i])
		        X_data = [S[j], X[i], d]
		        X_sorted.append(X_data)
		X_sorted.sort(key=itemgetter(2), reverse=True)

		S_ = S.copy()
		if max_bound == math.sqrt(2):
		    for a in range(0, len(X_sorted)):
		        if objf_func_d(S_, tradeoff) < objf_func_new_set_d(S, X_sorted[a][0], X_sorted[a][1], tradeoff, max_bound):
		            if X_sorted[a][1] not in X_not_pruned_hypothetical:
		                X_not_pruned_hypothetical.append(X_sorted[a][1])

		    numb_samples = pi_sample-len(S)
		    X_samples = X_not_pruned_hypothetical[0:numb_samples]            
		    maxI_S = get_maxI_score(S)
		    maxI_samples = get_maxI_score(X_samples)
		    if maxI_S > maxI_q:
		        maxI_q = maxI_S
		    if maxI_samples > maxI_q:
		        maxI_q = maxI_samples
		    max_bound = maxI_q

		    print("max_bound before X_not_pruned_hypothetical loop = {0}".format(max_bound))
		    for b in range(0, len(X_not_pruned_hypothetical)):
		        for c in range(0, len(S)):
		            if objf_func_d(S_, tradeoff) < objf_func_new_set_d(S, S[c], X_not_pruned_hypothetical[b], tradeoff, max_bound):
		                if X_not_pruned_hypothetical[b] not in X_not_pruned_max_actual:
		                    X_not_pruned_max_actual.append(X_not_pruned_hypothetical[b])

		                i_score = get_importance_score(X_not_pruned_hypothetical[b])
		                if objf_func_d(S_, tradeoff) < objf_func_new_set_d(S, S[c], X_not_pruned_hypothetical[b], tradeoff, i_score):
		                    new_S = create_S_d(S, S[c], X_not_pruned_hypothetical[b])
		                    S_ = new_S.copy()
		                if i_score > max_bound:
		                    max_bound = i_score

	    
		# While max_bound not sqrt 2                  
		else:
		    for y in range(0, len(X_sorted)):
		        print("max_bound else = {0}".format(max_bound))
		        if objf_func_d(S_, tradeoff) < objf_func_new_set_d(S, X_sorted[y][0], X_sorted[y][1], tradeoff, max_bound):
		            if X_sorted[y][1] not in X_not_pruned_max_actual:
		                X_not_pruned_max_actual.append(X_sorted[y][1])

		            i_score = get_importance_score(X_sorted[y][1])
		            if objf_func_d(S_, tradeoff) < objf_func_new_set_d(S, X_sorted[y][0], X_sorted[y][1], tradeoff, i_score):
		                new_S = create_S_d(S, X_sorted[y][0], X_sorted[y][1])
		                S_ = new_S.copy()
		            if i_score > max_bound:
		                max_bound = i_score

		if objf_func_d(S_,tradeoff) > objf_func_d(S,tradeoff):
		    S = S_.copy()

		objf = objf_func_d(S,tradeoff)
		if objf > objf_current_S:
		    objf_current_S = objf
		    improve = True 
		    print("need improve")
		else:
		    improve = False
		    print("no improve")

	df_swapD_Pruning = pd.DataFrame(S, columns=['Attributes', 'Meassure', 'Function','Utility'])
	sum_util = (sum(df_swapD_Pruning['Utility'])/k)/2/max_i_score
	#print(df_swapD, file=open(output, "a"))
	df_swapD_Pruning = df_swapD_Pruning.drop(['Utility'],axis=1)
	series_set = df_swapD_Pruning.apply(lambda row: set(row), axis=1)
	new_df = series_set.apply(lambda a: series_set.apply(lambda b: fc.diversity(a,b)))
	new_df['tot'] = new_df.sum(axis=1)
	sum_div = (sum(new_df['tot'])/2)/(k*(k-1))/2
	objf = sum_util+sum_div
	timeafter = datetime.datetime.now()    
	procesing_time = str(timeafter - timebefore)
	print("i-DiVE-SwapD-Pruning,{0},{1},{2},{3},{4}".format(k,sum_util,sum_div,objf,procesing_time), file=open(output, "a"))


### Running the application.

xl = pd.ExcelFile("200.xlsx")
df = xl.parse("Sheet1", header=0)
#os.remove("pruned_objf_flights1.csv")

number_of_k = [5] #
output = "mei_objf_200_9.csv"
n = len(df)
max_i_score = math.sqrt(2)

for k in number_of_k:
	Only_Interestingness(df, k, output)
	Only_Diversity(df, k, output)
	iDiVE_Greedy(df, k, output)
	iDiVE_SwapI(df, k, output)
	iDiVE_SwapD(df, k, output)
	iDiVE_SwapD_Pruning(df, k, output)

	#iDiVE_SwapD_top1(df, k, output)



