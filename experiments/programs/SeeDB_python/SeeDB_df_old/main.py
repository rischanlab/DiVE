# -*- coding: utf-8 -*-
from seedb import SeeDB
from flights import data

if __name__ == "__main__":
    db,table,groupby,aggregate = data()

    top_k = 9
    #print(db,groupby,table,top_k,aggregate)
    framework = SeeDB(db,groupby,table,top_k,aggregate)
    framework.main()
