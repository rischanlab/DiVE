# -*- coding: utf-8 -*-
import pandas as pd

# def data():
#     db_name = 'seedb_data'
#     table = "flights"

#     data_set = {
#         'year'        : [('sum','arrivaldelay'),('sum','departuredelay'),('sum','weatherdelay'),('sum','distance'),('avg','arrivaldelay'),('avg','departuredelay'),('avg','weatherdelay'),('avg','distance'),('max','arrivaldelay'),('max','departuredelay'),('max','weatherdelay'),('max','distance')],
#         'month'         : [('sum','arrivaldelay'),('sum','departuredelay'),('sum','weatherdelay'),('sum','distance'),('avg','arrivaldelay'),('avg','departuredelay'),('avg','weatherdelay'),('avg','distance'),('max','arrivaldelay'),('max','departuredelay'),('max','weatherdelay'),('max','distance')],
#         'week'        : [('sum','arrivaldelay'),('sum','departuredelay'),('sum','weatherdelay'),('sum','distance'),('avg','arrivaldelay'),('avg','departuredelay'),('avg','weatherdelay'),('avg','distance'),('max','arrivaldelay'),('max','departuredelay'),('max','weatherdelay'),('max','distance')],
#         'day'         : [('sum','arrivaldelay'),('sum','departuredelay'),('sum','weatherdelay'),('sum','distance'),('avg','arrivaldelay'),('avg','departuredelay'),('avg','weatherdelay'),('avg','distance'),('max','arrivaldelay'),('max','departuredelay'),('max','weatherdelay'),('max','distance')],
#         'carrier'        : [('sum','arrivaldelay'),('sum','departuredelay'),('sum','weatherdelay'),('sum','distance'),('avg','arrivaldelay'),('avg','departuredelay'),('avg','weatherdelay'),('avg','distance'),('max','arrivaldelay'),('max','departuredelay'),('max','weatherdelay'),('max','distance')],
#         'origin'         : [('sum','arrivaldelay'),('sum','departuredelay'),('sum','weatherdelay'),('sum','distance'),('avg','arrivaldelay'),('avg','departuredelay'),('avg','weatherdelay'),('avg','distance'),('max','arrivaldelay'),('max','departuredelay'),('max','weatherdelay'),('max','distance')],
#         'destination'    : [('sum','arrivaldelay'),('sum','departuredelay'),('sum','weatherdelay'),('sum','distance'),('avg','arrivaldelay'),('avg','departuredelay'),('avg','weatherdelay'),('avg','distance'),('max','arrivaldelay'),('max','departuredelay'),('max','weatherdelay'),('max','distance')]
#     }
    
#     return db_name,table,data_set

# if __name__ == '__main__':
#     print(00)

# A = 7
# M = 4
# F = 3
# 84 

def data():
    db_name = 'seedb_data'

    table = "flights"
    groupby = (['year','month','week','day','carrier','origin','destination'])

    aggregate = ('arrivaldelay','departuredelay','weatherdelay','distance','arrivaldelay', 'departuredelay')

    return db_name, table, groupby, aggregate

if __name__ == '__main__':
    print(0)
