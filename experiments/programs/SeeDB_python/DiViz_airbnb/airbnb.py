# -*- coding: utf-8 -*-
import pandas as pd

def data():
    db_name = 'seedb_data'
    table = "airbnb"

    data_set = {
          'neighbourhood'        : [('sum','beds'),('sum','number_of_reviews'),('sum','price'),('avg','beds'),('avg','number_of_reviews'),('avg','price'),('max','beds'),('max','number_of_reviews'),('max','price')],
          'property_type'         : [('sum','beds'),('sum','number_of_reviews'),('sum','price'),('avg','beds'),('avg','number_of_reviews'),('avg','price'),('max','beds'),('max','number_of_reviews'),('max','price')],
          'room_type'        : [('sum','beds'),('sum','number_of_reviews'),('sum','price'),('avg','beds'),('avg','number_of_reviews'),('avg','price'),('max','beds'),('max','number_of_reviews'),('max','price')],
          'zipcode'         : [('sum','beds'),('sum','number_of_reviews'),('sum','price'),('avg','beds'),('avg','number_of_reviews'),('avg','price'),('max','beds'),('max','number_of_reviews'),('max','price')]
      }
      
    return db_name,table,data_set

if __name__ == '__main__':
    print(00)

