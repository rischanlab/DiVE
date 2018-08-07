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



k=20

xl = pd.ExcelFile("cp_asymtomatic.xlsx")
df = xl.parse("Sheet1", header=0)

tradeoff_list = [0.0, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8, 0.82,0.84,0.86,0.88,0.9,0.92,0.94,0.96,0.98,1.0]
#tradeoff_list =[0.5]
#number_of_k = [5,15,25,35] #
output = "3_sampling_top1_cp_asymtomatic_k20.csv"
df_greedy = Greedy_Return_df(df,k)

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


def pruning_calculation(df, df_greedy,k,tradeoff,output):
    df_greedy = df_greedy
    Xdf = df.reset_index(drop=True)
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

            #print("max_bound before X_not_pruned_hypothetical loop = {0}".format(max_bound))
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
                #print("max_bound else = {0}".format(max_bound))
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


    df_swapD = pd.DataFrame(S)
    num_x = len(X)
    num_not_pruned = len(X_not_pruned_max_actual)
    num_pruned = num_x - num_not_pruned

    print("{0},{1},{2}".format(tradeoff,num_not_pruned,num_pruned), file=open(output, "a"))





for tradeoff in tradeoff_list:
    pruning_calculation(df,df_greedy,k,tradeoff,output)

