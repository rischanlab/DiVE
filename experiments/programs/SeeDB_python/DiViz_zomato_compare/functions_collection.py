import pandas as pd 
from itertools import product
from itertools import combinations
# Diversity functions
def jaccard(a, b):
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

def diversity(a,b):
    return 1 - jaccard(a,b)

def distance_one_to_many(item, list_data):
    tot_dis = 0
    for i in range(0,len(list_data)):
        tot_dis += diversity(item, list_data[i])
    return tot_dis

def diversity_bruteforce(a,b):
    c = set(a).intersection(b)
    d = float(len(c)) / (len(a) + len(b) - len(c))
    return 1 - d
# Swap functions 

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
        d = diversity_bruteforce(x_max, X[a])
        if d > max_distance:
            max_distance = d
            listku.append((X[a],d))

    max(listku)
    maxlist = max(listku)
    return maxlist[0]

def dist(X, S):
    max_distance = []
    for i in range(0,len(X)):
        d = 0
        for j in range(0,len(S)):
            d += (diversity_bruteforce(X[i],S[j]))/len(S)
        max_distance.append((d, tuple([X[i],S[j]])))
    max_distance.sort(key=lambda x: x[0], reverse=True)
    data = max_distance[:1]
    return data[0][1][0]


def calculate_set_utility(df,item,S_list):
    S_list.append(item)
    k = len(S_list)
    new_df = pd.DataFrame(S_list, columns=['Attributes', 'Meassure', 'Function'])
    df_util = new_df.merge(df, how='left')
    utility = sum(df_util['Utility'])/k
    return utility

def calculate_set_diversity(item,S_list):
    S_list.append(item)
    k = len(S_list)
    new_series = pd.Series(S_list)
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