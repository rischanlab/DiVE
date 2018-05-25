import pandas as pd 
from itertools import product
from itertools import combinations
# Diversity functions
def check_attribute(attr):
    time_att = ['year','quarter','month','week','day']
    loc_att = ['country','state','region','city']
    product_att = ['category','subcategory','product_name']
    
    if attr in time_att:
        return 1
    elif attr in loc_att:
        return 2
    elif attr in product_att:
        return 3
    else:
        return 0

def time_hierarchy(at1, at2):
    time_att = ['year','quarter','month','week','day']
    val = [1,2,3,4,5]
    dict_time = dict(zip(time_att,val))
    d = abs(dict_time[at1] - dict_time[at2])
    return float(d)/len(time_att)
    
def loc_hierarchy(at1, at2):
    loc_att = ['country','state','region','city']
    val = [1,2,3,4]
    dict_loc = dict(zip(loc_att,val))
    d = abs(dict_loc[at1] - dict_loc[at2])
    return float(d)/len(loc_att)

def product_hierarchy(at1, at2):
    product_att = ['category','subcategory','product_name']
    val = [1,2,3]
    dict_prod = dict(zip(product_att,val))
    d = abs(dict_prod[at1] - dict_prod[at2])
    return float(d)/len(product_att)

def diversity(a,b):
    la = list(a)
    lb = list(b)
    v1 = get_value_d(la[0],lb[0])
    v2 = get_value_d(la[1],lb[1])
    v3 = get_value_d(la[2],lb[2])
    res = float((v1+v2+v3))/3
    return res
    
def get_value_d(attr1, attr2):
    d = None 
    if check_attribute(attr1) != 0:
        if check_attribute(attr1) == check_attribute(attr2):
            if check_attribute(attr1) == 1:
                d = time_hierarchy(attr1, attr2)
            elif check_attribute(attr1) == 2:
                d = loc_hierarchy(attr1, attr2)
            elif check_attribute(attr1) == 3:
                d = product_hierarchy(attr1, attr2)
            else:
                pass
        else:
            if (attr1) == (attr2):
                d = 0.0
            else:
                d = 1.0
    else:
        if (attr1) == (attr2):
                d = 0.0
        else:
            d = 1.0
    return d

# def diversity_bruteforce(a,b):
#     c = set(a).intersection(b)
#     d = float(len(c)) / (len(a) + len(b) - len(c))
#     return 1 - d

def distance_one_to_many(item, list_data):
    tot_dis = 0
    for i in range(0,len(list_data)):
        tot_dis += diversity(item, list_data[i])
    return tot_dis

def swap_get_highest_utility(df):
    return df.sort_values(by=['Utility'], ascending=[False])     

def swap_get_random(df, n):
    return df.sample(n)

def list_to_set_swap(Retlist):
    # input [11, 'carrier', 'weatherdelay', 'AVG', 0.88055483076477],..
    # output {'AVG', 'carrier', 'weatherdelay'}
    list_set = []
    for i in Retlist:
        setku = set([i[1],i[2],i[3]])
        list_set.append(setku)
    return list_set
def set_swap_one_item(item):
    return set([item[0],item[1],item[2]])

def list_heap(Retlist):
    # input [11, 'carrier', 'weatherdelay', 'AVG', 0.88055483076477],..
    # output {'AVG', 'carrier', 'weatherdelay',0.88055483076477}
    mylist = []
    for i in Retlist:
        listku= [i[1],i[2],i[3],i[4]]
        mylist.append(listku)
    return mylist


### greedy 
def get_the_farthest(x_max, X):
    listku = []
    max_distance = 0
    for a in range(0,len(X)):
        d = diversity(x_max, X[a])
        if d > max_distance:
            max_distance = d
            listku.append((X[a],d))

    max(listku)
    maxlist = max(listku)
    return maxlist[0]

def dist(X, S):
    # max_distance = []
    # for i in range(0,len(X)):
    #     d = 0
    #     for j in range(0,len(S)):
    #         d += (diversity(X[i],S[j]))/len(S)
    #     max_distance.append((d, tuple([X[i],S[j]])))
    # max_distance.sort(key=lambda x: x[0], reverse=True)
    # data = max_distance[:1]
    # return data[0][1][0]
    max_distance = 0
    result = []
    for i in range(0,len(X)):
        d = 0
        for j in range(0,len(S)):
            d += diversity(set(X[i]),set(S[j]))
            if d > max_distance:
                max_distance = d
                result = X[i]
    return result

def objf_dist(df, X, S):
    max_distance = 0
    result = []
    d = 0
    for i in range(0,len(X)):
        d = calculate_set_objf(df, X[i], S)
        if d > max_distance:
            max_distance = d
            result = X[i]
    return result


def calculate_set_utility(df,item,S_list):
    S_new = S_list.copy()
    S_new.append(item)
    k = len(S_new)
    new_df = pd.DataFrame(S_new, columns=['Attributes', 'Meassure', 'Function'])
    df_util = new_df.merge(df, how='left')
    utility = sum(df_util['Utility'])/k
    return utility

def calculate_set_diversity(item,S_list):
    S_new = S_list.copy()
    S_new.append(item)
    k = len(S_new)
    new_series = pd.Series(S_new)
    series_set = new_series.apply(lambda row: set(row))
    new_df = series_set.apply(lambda a: series_set.apply(lambda b: diversity(a,b)))
    new_df['tot'] = new_df.sum(axis=1)
    div = (sum(new_df['tot'])/2)/(k*(k-1))
    return div

def calculate_set_objf(df,item,S_list):
    util = calculate_set_utility(df,item,S_list)
    div = calculate_set_diversity(item,S_list)
    objf = util+div
    return objf

def three_values(mylist):
    # input [11, 'carrier', 'weatherdelay', 'AVG', 0.88055483076477],..
    # output {'AVG', 'carrier', 'weatherdelay'}
    list_three = []
    for i in mylist:
        listku = [i[1],i[2],i[3]]
        list_three.append(listku)
    return list_three

def swap_one_item(item):
    return [item[1],item[2],item[3]]

def min_list(mylist):
    return min(mylist, key=lambda x: x[-1])

def push_list(mylist, item):
    return mylist.append(item)

def set_swap_one_item(item):
    return set([item[1],item[2],item[3]])

def utility_one_to_many(item, list_data):
    list_data.append(item)
    return sum(i[4] for i in list_data)

#SWAP BARU

def util_func(S_list):
    new_df = pd.DataFrame(S_list)
    utility = sum(new_df[4])/len(new_df)
    return utility

def div_func(S_list):
    k = len(S_list)
    new_df = pd.DataFrame(S_list)
    df_now = new_df.drop([0, 4], axis=1)
    S_list_now = df_now.values.tolist()
    new_series = pd.Series(S_list_now)
    series_set = new_series.apply(lambda row: set(row))
    new_df = series_set.apply(lambda a: series_set.apply(lambda b: diversity(a,b)))
    new_df['tot'] = new_df.sum(axis=1)
    div = (sum(new_df['tot'])/2)/(k*(k-1))
    return div

def objf_func(S):
    util = util_func(S)
    div = div_func(S)
    objf = (util+div)
    return objf

def objf_func_new_set(S, X, Y):
    new_S = S.copy()
    new_S.remove(X)
    new_S.append(Y)
    util = util_func(new_S)
    div = div_func(new_S)
    objf = (util+div)
    return objf

def create_S(S, X, Y):
    new_S = S.copy()
    new_S.remove(X)
    new_S.append(Y)
    return new_S

def most_distant_two_views(data):
    max_distance = 0
    result = []
    for i in range(0,len(data)):
        for j in range(0,len(data)):
            d = diversity(data[i],data[j])
            if d > max_distance:
                max_distance = d
                result = [data[i],data[j]]
    return result

# SwapD

def util_func_d(S_list):
    new_df = pd.DataFrame(S_list)
    utility = sum(new_df[3])/len(new_df)
    return utility

def div_func_d(S_list):
    k = len(S_list)
    new_df = pd.DataFrame(S_list)
    df_now = new_df.drop([3], axis=1)
    S_list_now = df_now.values.tolist()
    new_series = pd.Series(S_list_now)
    series_set = new_series.apply(lambda row: set(row))
    new_df = series_set.apply(lambda a: series_set.apply(lambda b: diversity(a,b)))
    new_df['tot'] = new_df.sum(axis=1)
    div = (sum(new_df['tot'])/2)/(k*(k-1))
    return div

def objf_func_d(S):
    util = util_func_d(S)
    div = div_func_d(S)
    objf = (util+div)
    return objf

def objf_func_new_set_d(S, X, Y):
    new_S = S.copy()
    new_S.remove(X)
    new_S.append(Y)
    util = util_func_d(new_S)
    div = div_func_d(new_S)
    objf = (util+div)
    return objf

def create_S_d(S, X, Y):
    new_S = S.copy()
    new_S.remove(X)
    new_S.append(Y)
    return new_S

# Pruning Functions 
# Ini memang sengaja di set 0.5 tradeoff ya. karena ini hanya peduli pada result tp tidak pada cost

def div_compute(item, S_list):
    S_new = S_list.copy()
    S_new.append(item)
    k = len(S_new)
    new_series = pd.Series(S_new)
    series_set = new_series.apply(lambda row: set(row))
    new_df = series_set.apply(lambda a: series_set.apply(lambda b: diversity(a,b)))
    new_df['tot'] = new_df.sum(axis=1)
    div = (sum(new_df['tot'])/2)/(k*(k-1))
    return div

def max_compute(div, tradeoff=0.5):
    util = 0.5
    objf = ((1-tradeoff)*util)+(tradeoff*div)
    return objf

def min_compute(div, tradeoff=0.5):
    util = 0.0
    objf = ((1-tradeoff)*util)+(tradeoff*div)
    return objf