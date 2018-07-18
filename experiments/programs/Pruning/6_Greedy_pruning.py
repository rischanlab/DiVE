import datetime
import pandas as pd 
import math
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



k=5

xl = pd.ExcelFile("cp_asymtomatic.xlsx")
df = xl.parse("Sheet1", header=0)

tradeoff_list = [0.0, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8, 0.82,0.84,0.86,0.88,0.9,0.92,0.94,0.96,0.98,1.0]
#number_of_k = [5,15,25,35] #
output = "static_greedy_pruning.csv"
#df_greedy = Greedy_Return_df(df,k)

def greedy_util_func(S_list, df):
    max_I = math.sqrt(2)
    df_pg = pd.DataFrame(S_list, columns=['Attributes', 'Meassure', 'Function'])
    df_pg_result = df_pg.merge(df, how='left')
    util = (sum(df_pg_result['Utility'])/k)/max_I
    return util

def greedy_div_func(S_list):
    k = len(S_list)
    new_df = pd.DataFrame(S_list)
    S_list_now = new_df.values.tolist()
    new_series = pd.Series(S_list_now)
    series_set = new_series.apply(lambda row: set(row))
    new_df = series_set.apply(lambda a: series_set.apply(lambda b: fc.diversity(a,b)))
    new_df['tot'] = new_df.sum(axis=1)
    div = (sum(new_df['tot'])/2)/(k*(k-1))
    return div

def greedy_objf_func(S, tradeoff, df):
    util = greedy_util_func(S, df)
    div = greedy_div_func(S)
    objf = ((1-tradeoff)*util)+(tradeoff*div)
    return objf

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
    initialization = list([get_importance_score(df,S[0]),get_importance_score(df,S[1])])
    i_curr = math.sqrt(2)
    i_0 = max(initialization)
    num_prune0 = 0
    num_prune1 = 0
    num_prune2 = 0
    item = []


    while i < k:
        x_df = pd.DataFrame(X, columns=['Attributes', 'Meassure', 'Function']) 
        x_df['div'] = x_df[['Attributes', 'Meassure', 'Function']].apply(lambda row: fc.div_compute(row,S), axis=1)
        #x_df = x_df.merge(df, how='left')
        x_df['Umax'] = x_df['div'].apply(lambda row: max_compute(row, i_curr=i_curr, tradeoff=tradeoff))
        x_df['Umin'] = x_df['div'].apply(lambda row: min_compute(row, i_0=i_0, tradeoff=tradeoff))
        x_df = x_df.sort_values(by=['div'],ascending=False)
        x_df = x_df.reset_index(drop=True)
        max_Umin = max(x_df['Umin'])
        # Pruning 0 step
        prune0_df = x_df[x_df['Umax'] < max_Umin]
        num_prune0 = num_prune0 + len(prune0_df)

        x_df = x_df[x_df['Umax'] > max_Umin]

        objf = 0
        for i in range(0,len(x_df)):
            S_new = S.copy()
            view = [x_df.iloc[i]['Attributes'], x_df.iloc[i]['Meassure'], x_df.iloc[i]['Function']]
            S_new.append(view)
            new_objf = greedy_objf_func(S_new, tradeoff, df)
            if new_objf > objf:
                x= get_importance_score(df, view)
                if x > i_0:
                    i_0 = x
                    x_df['Umax'] = x_df['div'].apply(lambda row: max_compute(row, i_curr=i_curr, tradeoff=tradeoff))
                    x_df['Umin'] = x_df['div'].apply(lambda row: min_compute(row, i_0=i_0, tradeoff=tradeoff))
                    x_df = x_df.sort_values(by=['div'],ascending=False)
                    x_df = x_df.reset_index(drop=True)
                    max_Umin = max(x_df['Umin'])
                    prune1_df = x_df[x_df['Umax'] < max_Umin]
                    num_prune1 = len(prune1_df)
                objf = new_objf
                item = view
            else:
                num_prune2 = num_prune2 + 1
        #print(item)
        if item not in S:
          S.append(item)
          X.remove(item)
        else:
          pass

        i = i + 1  

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
    num_pruning = num_prune0 + num_prune1 + num_prune2
    timeafter = datetime.datetime.now()    
    procesing_time = str(timeafter - timebefore)
    #print("Greedy-Pruning,{0},{1},{2},{3},{4}".format(k,sum_util,sum_div,objf,procesing_time), file=open(output, "a"))
    print("Greedy-Pruning,{0},{1},{2},{3},{4}".format(k,sum_util,sum_div,objf,procesing_time,num_pruning), file=open(output, "a"))


for tradeoff in tradeoff_list:
	Greedy_Pruning(df,k,tradeoff,output)

