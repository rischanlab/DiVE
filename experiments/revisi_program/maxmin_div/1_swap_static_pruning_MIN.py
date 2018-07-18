import datetime
import pandas as pd 
import math
import numpy as np
from itertools import product
from itertools import combinations
import mei_functions_collection_div_weight as fc 

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



def util_func_d(S_list):
    max_I = math.sqrt(2)
    new_df = pd.DataFrame(S_list)
    utility = (sum(new_df[3])/len(new_df))/max_I
    return utility

def div_func_d_maxmin(S_list):
    if len(set(map(tuple,S_list))) == len(S_list):
        k = len(S_list)
        new_df = pd.DataFrame(S_list)
        S_list_now = new_df.values.tolist()
        new_series = pd.Series(S_list_now)
        series_set = new_series.apply(lambda row: set(row))
        new_df = series_set.apply(lambda a: series_set.apply(lambda b: fc.diversity(a,b)))
        xx = new_df.replace(0, np.nan)
        return np.nanmin(xx.iloc[:, :].values)
    else:
        return 0

def objf_func_d(S, tradeoff):
    util = util_func_d(S)
    div = div_func_d_maxmin(S)
    objf = ((1-tradeoff)*util)+(tradeoff*div)
    return objf

def objf_func_new_set_d(S, X, Y, tradeoff):
    new_S = S.copy()
    new_S.remove(X)
    new_S.append(Y)
    util = util_func_d(new_S)
    div = div_func_d_maxmin(new_S)
    objf = ((1-tradeoff)*util)+(tradeoff*div)
    return objf

def checkpruning(S, X, Y, tradeoff):
    max_I = math.sqrt(2)
    new_S = S.copy()
    new_S.remove(X)
    
    temp_S = new_S.copy()
    temp_Y = Y.copy()
    temp_Y[3] = max_I
    temp_S.append(temp_Y)
    temp_util = util_func_d(temp_S)
    temp_div = div_func_d_maxmin(temp_S)
    temp_objf = ((1-tradeoff)*temp_util)+(tradeoff*temp_div)
    objf = temp_objf
    return objf

def create_S_d(S, X, Y):
    new_S = S.copy()
    new_S.remove(X)
    new_S.append(Y)
    return new_S



def pruning_calculation(df,k,tradeoff,output):
    df_greedy = Greedy_Return_df(df, k)
    Xdf = df.reset_index(drop=True)
    Retlist = df_greedy.values.tolist()

    X = Xdf.values.tolist()
    #get the original X = X -S
    Retlist_X = Retlist.copy()

    for i in range(0,len(Retlist_X)):
        X.remove(Retlist_X[i])

    S = Retlist.copy()
    print(S)
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

    print(S)
    df_swapD = pd.DataFrame(S, columns=['Attributes', 'Meassure', 'Function','Utility'])
    num_x = len(X)
    num_not_pruned = len(item_list)
    num_pruned = num_x - num_not_pruned
    print("{0},{1},{2}".format(tradeoff,num_not_pruned,num_pruned), file=open(output, "a"))


k=5

xl = pd.ExcelFile("results_carrier_US.xlsx")
df = xl.parse("Sheet1", header=0)

tradeoff_list = [0.0, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8, 0.82,0.84,0.86,0.88,0.9,0.92,0.94,0.96,0.98,1.0]
#number_of_k = [5,15,25,35] #
output = "swap_static_results_carrier_US_MIN.csv"


for tradeoff in tradeoff_list:
	pruning_calculation(df,k,tradeoff,output)

