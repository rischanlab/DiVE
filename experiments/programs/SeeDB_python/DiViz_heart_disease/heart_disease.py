# -*- coding: utf-8 -*-
import pandas as pd

def data():
    db_name = 'seedb_data'
    table = "heart_disease"

    data_set = {
        'sex'        : [('sum','age'),('sum','restbp'),('sum','chol'),('sum','thalach'),('sum','oldpeak'),('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak'),('variance','age'),('variance','restbp'),('variance','chol'),('variance','thalach'),('variance','oldpeak'),('stddev','age'),('stddev','restbp'),('stddev','chol'),('stddev','thalach'),('stddev','oldpeak')],
        'cp'         : [('sum','age'),('sum','restbp'),('sum','chol'),('sum','thalach'),('sum','oldpeak'),('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak'),('variance','age'),('variance','restbp'),('variance','chol'),('variance','thalach'),('variance','oldpeak'),('stddev','age'),('stddev','restbp'),('stddev','chol'),('stddev','thalach'),('stddev','oldpeak')],
        'fbs'        : [('sum','age'),('sum','restbp'),('sum','chol'),('sum','thalach'),('sum','oldpeak'),('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak'),('variance','age'),('variance','restbp'),('variance','chol'),('variance','thalach'),('variance','oldpeak'),('stddev','age'),('stddev','restbp'),('stddev','chol'),('stddev','thalach'),('stddev','oldpeak')],
        'restecg'    : [('sum','age'),('sum','restbp'),('sum','chol'),('sum','thalach'),('sum','oldpeak'),('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak'),('variance','age'),('variance','restbp'),('variance','chol'),('variance','thalach'),('variance','oldpeak'),('stddev','age'),('stddev','restbp'),('stddev','chol'),('stddev','thalach'),('stddev','oldpeak')],
        'exang'      : [('sum','age'),('sum','restbp'),('sum','chol'),('sum','thalach'),('sum','oldpeak'),('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak'),('variance','age'),('variance','restbp'),('variance','chol'),('variance','thalach'),('variance','oldpeak'),('stddev','age'),('stddev','restbp'),('stddev','chol'),('stddev','thalach'),('stddev','oldpeak')],
        'slope'      : [('sum','age'),('sum','restbp'),('sum','chol'),('sum','thalach'),('sum','oldpeak'),('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak'),('variance','age'),('variance','restbp'),('variance','chol'),('variance','thalach'),('variance','oldpeak'),('stddev','age'),('stddev','restbp'),('stddev','chol'),('stddev','thalach'),('stddev','oldpeak')],
        'num'        : [('sum','age'),('sum','restbp'),('sum','chol'),('sum','thalach'),('sum','oldpeak'),('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak'),('variance','age'),('variance','restbp'),('variance','chol'),('variance','thalach'),('variance','oldpeak'),('stddev','age'),('stddev','restbp'),('stddev','chol'),('stddev','thalach'),('stddev','oldpeak')],
        'thal'       : [('sum','age'),('sum','restbp'),('sum','chol'),('sum','thalach'),('sum','oldpeak'),('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak'),('variance','age'),('variance','restbp'),('variance','chol'),('variance','thalach'),('variance','oldpeak'),('stddev','age'),('stddev','restbp'),('stddev','chol'),('stddev','thalach'),('stddev','oldpeak')]
    }
    
    return db_name,table,data_set

if __name__ == '__main__':
    print(00)

# A = 7
# M = 4
# F = 3
# 84 

# data_set = {
#         'sex'        : [('sum','age'),('sum','restbp'),('sum','chol'),('sum','thalach'),('sum','oldpeak'),('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak')],
#         'cp'         : [('sum','age'),('sum','restbp'),('sum','chol'),('sum','thalach'),('sum','oldpeak'),('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak')],
#         'fbs'        : [('sum','age'),('sum','restbp'),('sum','chol'),('sum','thalach'),('sum','oldpeak'),('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak')],
#         'restecg'    : [('sum','age'),('sum','restbp'),('sum','chol'),('sum','thalach'),('sum','oldpeak'),('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak')],
#         'exang'      : [('sum','age'),('sum','restbp'),('sum','chol'),('sum','thalach'),('sum','oldpeak'),('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak')],
#         'slope'      : [('sum','age'),('sum','restbp'),('sum','chol'),('sum','thalach'),('sum','oldpeak'),('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak')],
#         'num'        : [('sum','age'),('sum','restbp'),('sum','chol'),('sum','thalach'),('sum','oldpeak'),('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak')],
#         'thal'       : [('sum','age'),('sum','restbp'),('sum','chol'),('sum','thalach'),('sum','oldpeak'),('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak')]
#     }

    # data_set = {
    #     'sex'        : [('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak')],
    #     'cp'         : [('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak')],
    #     'fbs'        : [('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak')],
    #     'restecg'    : [('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak')],
    #     'exang'      : [('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak')],
    #     'slope'      : [('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak')],
    #     'num'        : [('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak')],
    #     'thal'       : [('avg','age'),('avg','restbp'),('avg','chol'),('avg','thalach'),('avg','oldpeak'),('max','age'),('max','restbp'),('max','chol'),('max','thalach'),('max','oldpeak')]
    # }