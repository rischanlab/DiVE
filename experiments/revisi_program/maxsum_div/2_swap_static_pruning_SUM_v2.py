import datetime
import pandas as pd 
import math
from itertools import product
from itertools import combinations
from operator import itemgetter
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

    X_sorted = []
    X_data = []
    d = 0
    X_not_pruned_hypothetical = []
    for i in range(0,len(X)):
        for j in range(0,len(S)):
            d = div_new_set_d(S, S[j], X[i])
            X_data = [S[j], X[i], d]
            X_sorted.append(X_data)
    X_sorted.sort(key=itemgetter(2), reverse=True)
    print(len(X))
    print("/n")
    print(len(X_sorted))
    
    # max_bound =math.sqrt(2)
    # for a in range(0, len(X_sorted)):
    #     S_ = S.copy()
    #     if objf_func_d(S_, tradeoff) < objf_func_new_set_d(S, X_sorted[a][0], X_sorted[a][1], tradeoff, max_bound):
    #         if X_sorted[a][1] not in X_not_pruned_hypothetical:
    #             X_not_pruned_hypothetical.append(X_sorted[a][1])
    #         new_S = create_S_d(S, X_sorted[a][0], X_sorted[a][1])
    #         S_ = new_S.copy()
    
    #         if objf_func_d(S_,tradeoff) > objf_func_d(S,tradeoff):
    #             S = S_.copy()

    # x_df = pd.DataFrame(X, columns=['Attributes', 'Meassure', 'Function']) 
    #     # Calculate diversity value of each X to current set S
    # x_df['div'] = x_df[['Attributes', 'Meassure', 'Function']].apply(lambda row: fc.div_compute(row,S), axis=1)
    # # Calculate max and min values of each X
    # x_df = x_df.sort_values(by=['div'],ascending=False)
    # x_df = x_df.reset_index(drop=True)
    # max_static_bound = math.sqrt(2)
    # tradeoff = tradeoff
    # x_df['Umax'] = x_df['div'].apply(max_compute, i_curr=max_static_bound,tradeoff=tradeoff)

    # objf_S =  objf_func_d(S, tradeoff, df)

    # new_df = x_df[x_df['Umax'] < objf_S]
    # pruned_list = new_df[['Attributes','Meassure','Function']].values.tolist()

    # FS = 0
    # #topview = []
    # for j in range(0,len(x_df)):
    #     S_ = S.copy()
    #     view = [x_df.iloc[j]['Attributes'], x_df.iloc[j]['Meassure'], x_df.iloc[j]['Function']]
    #     #S_.append(view)
    #     for m in range(0,len(S)):
    #         if objf_func_d(S_, tradeoff) < checkpruning(S, S[m], view, tradeoff):
    #             if view not in item_list:
    #                 item_list.append(view)
    #             #print("pruning condition = {} ".format(X[i]))
    #             if objf_func_d(S_, tradeoff) < objf_func_new_set_d(S, S[m], view, tradeoff):
    #                 #print("objf condition = {}".format(X[i]))
    #                 new_S = create_S_d(S, S[m], view)
    #                 S_ = new_S.copy()
    #             #print(S_)
    #     if objf_func_d(S_,tradeoff) > objf_func_d(S,tradeoff):
    #         S = S_.copy()

    #print(len(pruned_list))
    # df_swapD = pd.DataFrame(S)
    # num_x = len(X)
    # num_not_pruned = len(X_not_pruned_max_actual)
    # num_pruned = num_x - num_not_pruned

    # print("{0},{1},{2}".format(tradeoff,num_not_pruned,num_pruned), file=open(output, "a"))



k=5

xl = pd.ExcelFile("disease.xlsx")
df = xl.parse("Sheet1", header=0)

tradeoff_list = [0.7]
#tradeoff_list = [0.0, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8, 0.82,0.84,0.86,0.88,0.9,0.92,0.94,0.96,0.98,1.0]
#number_of_k = [5,15,25,35] #
output = "swap_static_disease_SUM_2.csv"


for tradeoff in tradeoff_list:
	pruning_calculation(df,k,tradeoff,output)

