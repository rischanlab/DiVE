# -*- coding:utf-8 -*-
import pandas as pd 
import time,math,numpy as np
from itertools import combinations
from config import config_data
import matplotlib.pyplot as plt
import functions_collection as fc 



class SeeDB:
    query_time,deviance_time,sort_time,div_time,visualization_time = 0,0,0,0,0
    def __init__(self, db,data_set,table,k):
        self.cursor = config_data(db)
        self.data_set, self.table,self.k = data_set, table, k
        self.terms()
        self.start = time.time()
        self.top_k = {}
        self.best_k = {}

    def terms(self):
        self.where1,self.where2 = input('enter WHERE clause for q1->'),input('enter WHERE clause for q2->')

    def query(self):
        # if self.func == 'sum' or 'order_amount' in self.attribute1: 
        #     query1 = 'select ' + self.attribute2 +',' + self.func + '(' + 'CAST(' + self.attribute1 + ' AS BIGINT' + '))' + ' from ' + self.table
        # else:
        query1 = 'select ' + self.attribute2 + ',' + self.func + '(' + self.attribute1 + ')' + ' from ' + self.table
        if self.where1 != '':
            query1 += ' where ' + self.where1
        query1 += ' group by ' + self.attribute2 + ' order by ' + self.attribute2

        # if self.func == 'sum' or 'order_amount' in self.attribute1:
        #     query2 = 'select ' + self.attribute2 + ',' + self.func + '(' + 'CAST(' + self.attribute1 + ' AS BIGINT' + ')) ' + ' from ' + self.table
        # else:
        query2 = 'select ' + self.attribute2 +',' + self.func + '(' + self.attribute1 + ')' + ' from ' + self.table
        if self.where2 != '':
            query2 += ' where ' + self.where2
        query2 += ' group by ' + self.attribute2 + ' order by ' + self.attribute2

        self.cursor.execute(query1)
        data1 = self.cursor.fetchall()
        self.cursor.execute(query2)
        data2 = self.cursor.fetchall()

        return data1,data2

    def nomalization(self,data):
        z,sum_x = tuple(),0
        for x,y in data:
            sum_x += y
        for x,y in data:
            z += ( (x , y/sum_x), )
        return z

    def distance(self):
        # make queries and execute these
        a = time.time()
        x,y = self.query()
        self.query_time += time.time() - a

        # calclate deviance
        deviance = 0
        a = time.time()
        x,y = self.nomalization(x),self.nomalization(y)
        dd = dict()
        for i, j in x:
            dd[i] = j
        for i, j in y:
            if i in dd:
                dd[i] = math.fabs(dd[i] - j)
            else:
                dd[i] = j
        for x, dis in dd.items():
            deviance += float(dis)
        self.deviance_time += time.time() - a

        return math.sqrt(deviance)

    def cheak_k(self,d):
        # preprocessing
        if self.attribute1 == '*':
            self.attribute1 = '.'+self.attribute1
        # cheak deviance and sort results
        if len(self.top_k) == 0:
            self.top_k[0] = (d,(self.func,self.attribute1,self.attribute2))
        elif len(self.top_k) < self.k:
            target = (d, (self.func,self.attribute1, self.attribute2))
            for i, j in self.top_k.items():
                if j[0] < target[0]:
                    self.top_k[i] = target
                    target = j
            self.top_k[len(self.top_k)] = target
        else:
            target = (d,(self.func,self.attribute1,self.attribute2))
            for i,j in self.top_k.items():
                if j[0] < target[0]:
                    self.top_k[i] = target
                    target = j

    def get_best_k(self,d):
        # preprocessing
        if self.attribute1 == '*':
            self.attribute1 = '.'+self.attribute1
        # cheak deviance and sort results
        if len(self.best_k) == 0:
            self.best_k[0] = (d,(self.func,self.attribute1,self.attribute2))
        # elif len(self.best_k) > self.k:
        #     target = (d, (self.func,self.attribute1, self.attribute2))
        #     for i, j in self.best_k.items():
        #         if j[0] < target[0]:
        #             self.best_k[i] = target
        #             target = j
        #     self.best_k[len(self.best_k)] = target
        else:
            target = (d,(self.func,self.attribute1,self.attribute2))
            for i,j in self.best_k.items():
                if j[0] < target[0]:
                    self.best_k[i] = target
                    target = j
            self.best_k[len(self.best_k)] = target

    def visualization(self):
        # setting n*m
        n = math.ceil(np.sqrt(self.k))
        m = math.ceil(self.k / n)
        fig, axes = plt.subplots(nrows=n, ncols=m, figsize=(10, 8))
        ii = 0
        for dis,dt in self.top_k.items():
            if '*' in dt[1][1]:
                self.attribute1, self.attribute2, self.func = dt[1][1].split('.')[1], dt[1][2], dt[1][0]
            else:
                self.attribute1, self.attribute2, self.func = dt[1][1], dt[1][2], dt[1][0]
            data1, data2 = self.query()
            data1, data2 = self.nomalization(data1), self.nomalization(data2)
            x_agre = list()
            for i, j in data1 + data2:
                if not i in x_agre:
                    x_agre.append(i)
            t1, t2 = dict(data1), dict(data2)
            x, y1, y2 = [i for i in range(0, len(x_agre))], list(), list()
            for i in x_agre:
                if i in t1:
                    y1.append(t1[i])
                else:
                    y1.append(0)
                if i in t2:
                    y2.append(t2[i])
                else:
                    y2.append(0)
            axes[int(ii/m), ii%m].plot(x, y1, linewidth=2)
            axes[int(ii/m), ii%m].plot(x, y2, linewidth=2)
            axes[int(ii/m), ii%m].set_xticks(x)
            axes[int(ii/m), ii%m].set_xticklabels(x_agre, rotation=30)
            axes[int(ii/m), ii%m].set_title(ii)
            axes[int(ii/m), ii%m].set_xlabel(self.attribute2)
            axes[int(ii/m), ii%m].grid(True)
            ii+=1
            if ii > self.k:
                break
        plt.savefig('sample.png')
        plt.show()

    def store_result(self):
        data_result = []
        for i,j in self.best_k.items():
            data_result.append([i+1,j[1][2],j[1][1],j[1][0],j[0]])
        writer = pd.ExcelWriter('results.xlsx')
        df = pd.DataFrame(data_result, columns=['ID','Attributes', 'Meassure', 'Function', 'Utility'])
        df.to_excel(writer,'Sheet1', index=0)
        writer.save()
        

    # def diversity(self):
    #     a = time.time()
    #     xl = pd.ExcelFile("results.xlsx")
    #     df = xl.parse("Sheet1", header=0)
    #     lower, upper = 0.25, 0.5
    #     df['Utility'] = df['Utility'].apply(lambda x: lower + (upper - lower) * x)
    #     SortedRecItems = fc.swap_get_highest_utility(df).reset_index(drop=False)
    #     # Get the topk from set X with the highest utility
    #     Retlist = SortedRecItems.head(self.k).values.tolist()
    #     X = SortedRecItems.head(len(df)).values.tolist()
    #     # get the original X = X -S
    #     Retlist_X = Retlist.copy()
    #     for i in range(0,len(Retlist_X)):
    #         X.remove(Retlist_X[i])
    #     S = Retlist.copy()
    #     S_ = S.copy()
    #     min_ = fc.min_list(S)
    #     S_.remove(min_)
    #     for i in range(0,len(X)):
    #         # d_i_Retlist : distance i to all member in Retlist
    #         # d_pos_Retlist : distance pos to all member in Retlist
    #         d_i_S_ = fc.distance_one_to_many(fc.set_swap_one_item(min_),
    #                            fc.list_to_set_swap(S_))
    #         d_pos_S_ = fc.distance_one_to_many(fc.set_swap_one_item(X[i]),fc.list_to_set_swap(S_))
    #         #print("This item which removed {}".format(min_))
    #         #print("This item which item in {} the value {}".format(i, X[i]))
    #         # If sum of distance min_ to S_ < sum of distance pos to S_ - 
    #         if d_i_S_ < d_pos_S_:
    #             try:
    #                 # If objective function with min_ < objective function with pos
    #                 objf_i = fc.calculate_set_objf(df, fc.swap_one_item(min_),fc.three_values(S_))
    #                 objf_pos = fc.calculate_set_objf(df, fc.swap_one_item(X[i]),fc.three_values(S_))
    #                 if objf_i < objf_pos:
    #                     S.remove(min_)
    #                     #print("Removing {} from S".format(min_))
    #                     S.append(X[i])
    #                     #print("Adding {} to S".format(X[i]))
    #                     S_ = S.copy()
    #                     #print("Copying S_ from S")
    #                 else:
    #                     S_ = S.copy()
    #                     #print("Objf is not better Copying S_ from S")
    #             except IndexError:
    #                 pass
    #         else:
    #             S_ = S.copy()
    #             #print("Distance is not better Copying S_ from S")
    #         try:
    #             if len(S_) > 0:
    #                 min_ = fc.min_list(S_)
    #                 S_.remove(min_)
    #             else:
    #                 pass
    #         except IndexError:
    #             pass
    #     self.div_time += time.time() - a
    #     for i in S:
    #         print(i[1], i[5], i[4], i[3], i[2])
    #     #print(Retlist)

    def diversity(self):
        a = time.time()
        xl = pd.ExcelFile("results.xlsx")
        df = xl.parse("Sheet1", header=0)
        df_greedy = df.drop(['Utility'],axis=1)
        series_set = df_greedy.apply(lambda row: tuple(row), axis=1)

        farthest = []
        for z in combinations(series_set, 2):
            dis = fc.diversity_bruteforce(*z)
            farthest.append((dis, list(z)))
            
        farthest.sort(key=lambda x: x[0], reverse=True)
        x_y_max = farthest[:1]
        S = x_y_max[0][1]
        S = [list(row) for row in S]
        X = df_greedy.values.tolist()
        X.remove(S[0])
        X.remove(S[1])
        i = len(S)

        while i < self.k:    
            item = fc.dist(X, S)
            #print(item)
            if item not in S:
                S.append(item)
                X.remove(item)
            else:
                pass
                        
            i = i + 1  
        self.div_time += time.time() - a
        # for i in S:
        #     print(i[1], i[5], i[4], i[3], i[2])
        xl = pd.ExcelFile("results.xlsx")
        df = xl.parse("Sheet1", header=0)
        lower, upper = 0.25, 0.5
        df['Utility'] = df['Utility'].apply(lambda x: lower + (upper - lower) * x)
        df_gh = pd.DataFrame(S, columns=['id','Attributes', 'Meassure', 'Function'])
        df_maxdiv = df_gh.merge(df, how='left')
        df_maxdiv = df_maxdiv[['Utility','Function','Meassure','Attributes']]
        df_maxdiv.rename(columns={'Utility': 'ObjectiveF'}, inplace=True)
        print('Diversity time:',self.div_time)
        print('Greedy only diversity')
        print('================================================================')
        print(df_maxdiv)

    def output(self):
        print('================================================================')
        print('Query time:',self.query_time)
        print('Utility time:',self.deviance_time+self.sort_time)
        print('Total view processing time:',time.time()-self.start)
        #print('Visualization time:',self.visualization_time)
        print('================================================================')
        print('Rank, Utility, (F, M, A)')
        print('================================================================')
        for i,j in self.top_k.items():
            print(i+1,j[0],j[1])
        print('================================================================')

    def visualize(self):
        print('================================================================')
        print('Visualization time:',self.visualization_time)

    def main(self):
        # roop
        for self.attribute2, ite in self.data_set.items():
            for self.func, self.attribute1 in ite:
                # calclate euclid distance
                d = self.distance()
                # sort results
                a = time.time()
                # if d != -1 and d<1:
                #self.store_result(d)
                self.cheak_k(d)
                self.get_best_k(d)
                self.sort_time += time.time() - a
            #print(time.time() - self.start)
        self.output()
        self.store_result()
        self.diversity()
        # a = time.time()
        # self.visualization()
        # self.visualization_time = time.time() - a
        # self.visualize()
        #         