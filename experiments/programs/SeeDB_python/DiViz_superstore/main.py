# -*- coding: utf-8 -*-
from seedb import SeeDB
from superstore import data

if __name__ == "__main__":
    db,table,data_set = data()

    top_k = 35


    framework = SeeDB(db,data_set,table,top_k)
    framework.main()