# -*- coding: utf-8 -*-
import pandas as pd

def data():
    db_name = 'seedb_data'
    table = "zomato"

    data_set = {
          'city'                        : [('sum','average_cost_for_two'),('sum','price_range'),('sum','aggregate_rating'),('sum','votes'),('avg','average_cost_for_two'),('avg','price_range'),('avg','aggregate_rating'),('avg','votes'),('max','average_cost_for_two'),('max','price_range'),('max','aggregate_rating'),('max','votes')],
          'cuisines'                    : [('sum','average_cost_for_two'),('sum','price_range'),('sum','aggregate_rating'),('sum','votes'),('avg','average_cost_for_two'),('avg','price_range'),('avg','aggregate_rating'),('avg','votes'),('max','average_cost_for_two'),('max','price_range'),('max','aggregate_rating'),('max','votes')],
          'has_table_booking'           : [('sum','average_cost_for_two'),('sum','price_range'),('sum','aggregate_rating'),('sum','votes'),('avg','average_cost_for_two'),('avg','price_range'),('avg','aggregate_rating'),('avg','votes'),('max','average_cost_for_two'),('max','price_range'),('max','aggregate_rating'),('max','votes')],
          'has_online_delivery'         : [('sum','average_cost_for_two'),('sum','price_range'),('sum','aggregate_rating'),('sum','votes'),('avg','average_cost_for_two'),('avg','price_range'),('avg','aggregate_rating'),('avg','votes'),('max','average_cost_for_two'),('max','price_range'),('max','aggregate_rating'),('max','votes')],
          'rating_text'                 : [('sum','average_cost_for_two'),('sum','price_range'),('sum','aggregate_rating'),('sum','votes'),('avg','average_cost_for_two'),('avg','price_range'),('avg','aggregate_rating'),('avg','votes'),('max','average_cost_for_two'),('max','price_range'),('max','aggregate_rating'),('max','votes')]
      }
      
    return db_name,table,data_set

if __name__ == '__main__':
    print(00)
