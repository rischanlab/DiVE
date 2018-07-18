import datetime
import pandas as pd 
import math
import numpy as np
from itertools import product
from itertools import combinations
import mei_functions_collection_div_weight as fc 

# def Greedy_Return_df(df, k):
#     df_greedy = df.drop(['Utility'],axis=1)
#     dataset = df_greedy.reset_index(drop=True)
#     data = dataset.values.tolist()
#     X = data.copy()
#     S = fc.most_distant_two_views(data)
#     X.remove(S[0])
#     X.remove(S[1])
#     i = len(S)


#     while i < k:    
#         item = fc.dist(X, S)
#         #print(item)
#         if item not in S:
#             S.append(item)
#             X.remove(item)
#         else:
#             pass

#         i = i + 1  

#     df_gh = pd.DataFrame(S, columns=['Attributes', 'Meassure', 'Function'])
#     df_maxdiv = df_gh.merge(df, how='left')

#     return df_maxdiv



k= 5

xl = pd.ExcelFile("disease.xlsx")
df = xl.parse("Sheet1", header=0)

tradeoff_list = [0.0, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8, 0.82,0.84,0.86,0.88,0.9,0.92,0.94,0.96,0.98,1.0]
#number_of_k = [5,15,25,35] #
#tradeoff_list =[0.5]
output = "MaxMin_MaxMin_disease.csv"
#df_greedy = Greedy_Return_df(df,k)

def greedy_util_func(S_list, df):
    max_I = math.sqrt(2)
    df_pg = pd.DataFrame(S_list, columns=['Attributes', 'Meassure', 'Function'])
    df_pg_result = df_pg.merge(df, how='left')
    util = (sum(df_pg_result['Utility'])/k)/max_I
    return util

def greedy_div_func_maxmin(S_list):
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

def greedy_objf_func(S, tradeoff, df):
    util = greedy_util_func(S, df)
    div = greedy_div_func_maxmin(S)
    objf = ((1-tradeoff)*util)+(tradeoff*div)
    return objf

def div_compute(item, S_list):
    min_distance = 100
    for i in range(0, len(S_list)):
        d = fc.diversity(item,S_list[i])
        if d < min_distance:
            min_distance = d
    return min_distance

def max_compute(div, i_curr=math.sqrt(2), tradeoff=0.5):
    objf = ((1-tradeoff)*i_curr)+(tradeoff*div)
    return objf

def min_compute(div, i_0=0, tradeoff=0.5):
    objf = ((1-tradeoff)*i_0)+(tradeoff*div)
    return objf

def get_importance_score(df, view):
    new_df = df[(df['Attributes'] == view[0]) & (df['Meassure'] == view[1]) & (df['Function'] == view[2])]
    importance_score = new_df['Utility'].reset_index(drop=True)
    return importance_score.iloc[0]

def Greedy_Pruning(df, k, tradeoff, output):
    timebefore =  datetime.datetime.now()
    df_greedy = df.drop(['Utility'],axis=1)
    dataset = df_greedy.reset_index(drop=True)
    data = dataset.values.tolist()
    X = data.copy()
    S = fc.most_distant_two_views(data)
    X.remove(S[0])
    X.remove(S[1])
    i = len(S)

    total_pruned_views = []
    while i < k:
        print(i)
        #Creating dataframe of X 
        x_df = pd.DataFrame(X, columns=['Attributes', 'Meassure', 'Function']) 
        # Calculate diversity value of each X to current set S
        x_df['div'] = x_df[['Attributes', 'Meassure', 'Function']].apply(lambda row: div_compute(row,S), axis=1)
        # Calculate max and min values of each X
        x_df = x_df.sort_values(by=['div'],ascending=False)
        x_df = x_df.reset_index(drop=True)
        actual_importance = math.sqrt(2)
        i_0=0
        tradeoff = tradeoff
        x_df['Umax'] = x_df['div'].apply(max_compute, i_curr=actual_importance,tradeoff=tradeoff)
        x_df['Umin'] = x_df['div'].apply(min_compute, i_0=i_0, tradeoff=tradeoff)

        # Maximum value of Min
        bound = max(x_df['Umin'])
        new_df = x_df[x_df['Umax'] < bound]

        FS = 0
        #topview = []
        pruned_views = []
        for j in range(0,len(x_df)):
            S_ = S.copy()
            view = [x_df.iloc[j]['Attributes'], x_df.iloc[j]['Meassure'], x_df.iloc[j]['Function']]
            S_.append(view)
            div_view = greedy_div_func_maxmin(S_)
            i_score = get_importance_score(df, view)
            Uview = ((1-tradeoff)*i_score)+(tradeoff*div_view)

            if Uview > bound:
                bound = Uview
            new_df = x_df[x_df['Umax'] < bound]
            pruned_list = new_df[['Attributes','Meassure','Function']].values.tolist()
            for m in range(0, len(pruned_list)):
                if pruned_list[m] not in pruned_views:
                    pruned_views.append(pruned_list[m])
            #pruned = pruned + len(new_df)
            # if len(new_df) == len(x_df):
            #     #print("Total executed views = {0}".format(i+1))
            #     break
            #print(i,bound,len(new_df))
            objf = greedy_objf_func(S_, tradeoff, df)
            if objf > FS:
                FS = objf
                topview = view
            #print(FS, topview)


        S.append(topview)
        print(topview)
        X.remove(topview)
        for n in range(0, len(pruned_views)):
            if pruned_views[n] not in total_pruned_views:
                total_pruned_views.append(pruned_views[n])
        i = i + 1  

    print(S)
    df_pg = pd.DataFrame(S, columns=['Attributes', 'Meassure', 'Function'])
    df_pg_result = df_pg.merge(df, how='left')
    sum_util = (sum(df_pg_result['Utility'])/k)/math.sqrt(2)
    #print(df_maxdiv, file=open(output, "a"))

    df_pg_result = df_pg_result.drop(['Utility'],axis=1)
    series_set2 = df_pg_result.apply(lambda row: set(row), axis=1)
    new_df2 = series_set2.apply(lambda a: series_set2.apply(lambda b: fc.diversity(a,b)))
    # Adding new column for the sum value by rows
    new_df2['tot'] = new_df2.sum(axis=1)
    sum_div = (sum(new_df2['tot'])/2)/(k*(k-1))

    objf = sum_util+sum_div
    num_pruning = len(total_pruned_views)
    timeafter = datetime.datetime.now()    
    procesing_time = str(timeafter - timebefore)
    #print("Greedy-Pruning,{0},{1},{2},{3},{4}".format(k,sum_util,sum_div,objf,procesing_time), file=open(output, "a"))
    print("Greedy-Pruning,{0},{1},{2},{3},{4}".format(tradeoff,sum_util,sum_div,objf,num_pruning), file=open(output, "a"))


for tradeoff in tradeoff_list:
	Greedy_Pruning(df,k,tradeoff,output)

