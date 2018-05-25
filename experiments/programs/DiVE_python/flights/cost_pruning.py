import datetime
import pandas as pd 
from itertools import product
from itertools import combinations
import functions_collection as fc 

def Greedy_Return_df(df, k):
    df_greedy = df.drop(['Utility'],axis=1)
    dataset = df_greedy.reset_index(drop=True)
    data = dataset.values.tolist()
    X = data.copy()
    S = most_distant_two_views(data)
    X.remove(S[0])
    X.remove(S[1])
    i = len(S)


    while i < k:    
        item = dist(X, S)
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

def pruning_calculation(df,k,tradeoff,output)
	df_greedy = Greedy_Return_df(df,k)
	Xdf = df.reset_index(drop=True)
	Retlist = df_greedy.values.tolist()

	X = Xdf.values.tolist()
	#get the original X = X -S
	Retlist_X = Retlist.copy()

	for i in range(0,len(Retlist_X)):
	    X.remove(Retlist_X[i])

	S = Retlist.copy()
	item_list = []
	for i in range(0,len(X)):
	    S_ = S.copy()
	    for j in range(0,len(S)):
	        if objf_func_d(S_, tradeoff) < checkpruning(S, S[j], X[i], tradeoff):
	            if X[i] not in item_list:
	                item_list.append(X[i])
	            #print("pruning condition = {} ".format(X[i]))
	            if objf_func_d(S_, tradeoff) < objf_func_new_set_d(S, S[j], X[i], tradeoff):
	                #print("objf condition = {}".format(X[i]))
	                new_S = create_S_d(S, S[j], X[i])
	                S_ = new_S.copy()
	            #print(S_)
	    if objf_func_d(S_,tradeoff) > objf_func_d(S,tradeoff):
	        S = S_.copy()

	df_swapD = pd.DataFrame(S, columns=['Attributes', 'Meassure', 'Function','Utility'])
	num_x = len(X)
	num_not_pruned = len(item_list)
	num_pruned = num_x - num_not_pruned
	print("{0},{1},{2},{3},{4}".format(tradeoff,num_x,num_pruned), file=open(output, "a"))



k=5

xl = pd.ExcelFile("results_carrier_US_norm.xlsx")
df = xl.parse("Sheet1", header=0)

tradeoff_list = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
#number_of_k = [5,15,25,35] #
output = "pruning_all_output_carrier_US.csv"

for tradeoff in tradeoff_list:
	pruning_calculation(df,k,tradeoff,output)

