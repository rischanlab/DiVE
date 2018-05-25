# -*- coding: utf-8 -*-
import pandas as pd

def data():
    db_name = 'seedb_data'
    table = "orders"

    data_set = {
        'order_date'    : [('sum','sales'),('sum','quantity'),('sum','discount'),('sum','profit'),('avg','sales'),('avg','quantity'),('avg','discount'),('avg','profit'),('max','sales'),('max','quantity'),('max','discount'),('max','profit')],
        'ship_date'     : [('sum','sales'),('sum','quantity'),('sum','discount'),('sum','profit'),('avg','sales'),('avg','quantity'),('avg','discount'),('avg','profit'),('max','sales'),('max','quantity'),('max','discount'),('max','profit')],
        'ship_mode'     : [('sum','sales'),('sum','quantity'),('sum','discount'),('sum','profit'),('avg','sales'),('avg','quantity'),('avg','discount'),('avg','profit'),('max','sales'),('max','quantity'),('max','discount'),('max','profit')],
        'customer_name' : [('sum','sales'),('sum','quantity'),('sum','discount'),('sum','profit'),('avg','sales'),('avg','quantity'),('avg','discount'),('avg','profit'),('max','sales'),('max','quantity'),('max','discount'),('max','profit')],
        'segment'       : [('sum','sales'),('sum','quantity'),('sum','discount'),('sum','profit'),('avg','sales'),('avg','quantity'),('avg','discount'),('avg','profit'),('max','sales'),('max','quantity'),('max','discount'),('max','profit')],
        'country'       : [('sum','sales'),('sum','quantity'),('sum','discount'),('sum','profit'),('avg','sales'),('avg','quantity'),('avg','discount'),('avg','profit'),('max','sales'),('max','quantity'),('max','discount'),('max','profit')],
        'state'         : [('sum','sales'),('sum','quantity'),('sum','discount'),('sum','profit'),('avg','sales'),('avg','quantity'),('avg','discount'),('avg','profit'),('max','sales'),('max','quantity'),('max','discount'),('max','profit')],
        'region'        : [('sum','sales'),('sum','quantity'),('sum','discount'),('sum','profit'),('avg','sales'),('avg','quantity'),('avg','discount'),('avg','profit'),('max','sales'),('max','quantity'),('max','discount'),('max','profit')],
        'city'          : [('sum','sales'),('sum','quantity'),('sum','discount'),('sum','profit'),('avg','sales'),('avg','quantity'),('avg','discount'),('avg','profit'),('max','sales'),('max','quantity'),('max','discount'),('max','profit')],
        'postal_code'   : [('sum','sales'),('sum','quantity'),('sum','discount'),('sum','profit'),('avg','sales'),('avg','quantity'),('avg','discount'),('avg','profit'),('max','sales'),('max','quantity'),('max','discount'),('max','profit')],
        'category'      : [('sum','sales'),('sum','quantity'),('sum','discount'),('sum','profit'),('avg','sales'),('avg','quantity'),('avg','discount'),('avg','profit'),('max','sales'),('max','quantity'),('max','discount'),('max','profit')],
        'subcategory'   : [('sum','sales'),('sum','quantity'),('sum','discount'),('sum','profit'),('avg','sales'),('avg','quantity'),('avg','discount'),('avg','profit'),('max','sales'),('max','quantity'),('max','discount'),('max','profit')],
        'product_name'  : [('sum','sales'),('sum','quantity'),('sum','discount'),('sum','profit'),('avg','sales'),('avg','quantity'),('avg','discount'),('avg','profit'),('max','sales'),('max','quantity'),('max','discount'),('max','profit')]
    }
    
    return db_name,table,data_set

if __name__ == '__main__':
    print(00)


#A = 13
#M = 4
#F =3
#156


# where segment = 'Consumer'
# where ship_mode = 'First Class'

