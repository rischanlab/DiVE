# -*- coding: utf-8 -*-
import pandas as pd

def data():
    db_name = 'seedb_data'
    table = "kickstarter"

    data_set = {
          'main_category'   : [('sum','backers'),('sum','usd_pledged_real'),('sum','usd_goal_real'),('avg','backers'),('avg','usd_pledged_real'),('avg','usd_goal_real'),('max','backers'),('max','usd_pledged_real'),('max','usd_goal_real')],
          #'state'           : [('sum','backers'),('sum','usd_pledged_real'),('sum','usd_goal_real'),('avg','backers'),('avg','usd_pledged_real'),('avg','usd_goal_real'),('max','backers'),('max','usd_pledged_real'),('max','usd_goal_real')],
          'country'         : [('sum','backers'),('sum','usd_pledged_real'),('sum','usd_goal_real'),('avg','backers'),('avg','usd_pledged_real'),('avg','usd_goal_real'),('max','backers'),('max','usd_pledged_real'),('max','usd_goal_real')]
      }
      
    return db_name,table,data_set

if __name__ == '__main__':
    print(00)
