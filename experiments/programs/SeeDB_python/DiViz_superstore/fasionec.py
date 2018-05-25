# -*- coding: utf-8 -*-
import pandas as pd

def data():
    db_name = 'FasionEC'

    table = "[Order] "
    table += "left outer join OrderDetail on [Order].注文番号 = [OrderDetail].注文番号 " + "left outer join Member2 on [Order].顧客番号 = [Member2].顧客番号 "
    table += "inner join Item on [OrderDetail].商品番号 = [Item].商品番号 AND [OrderDetail].商品詳細番号 = [Item].商品詳細番号 " + "left outer join Enquete on [Order].顧客番号 = [Enquete].顧客番号"

    data_set = {
        '[Member2].アンケートフラグ'        : [('count','*'),('sum','[OrderDetail].数量'),('sum','[OrderDetail].注文金額'),('sum','[Order].注文時追加料金'),('avg','[OrderDetail].数量'),('avg','[OrderDetail].注文金額'),('avg','[Order].注文時追加料金')],
        '[Member2].性別'                    : [('count','*'),('sum','[OrderDetail].数量'),('sum','[OrderDetail].注文金額'),('sum','[Order].注文時追加料金'),('avg','[OrderDetail].数量'),('avg','[OrderDetail].注文金額'),('avg','[Order].注文時追加料金')],
        '[Member2].都道府県'                : [('count','*'),('sum','[OrderDetail].数量'),('sum','[OrderDetail].注文金額'),('sum','[Order].注文時追加料金'),('avg','[OrderDetail].数量'),('avg','[OrderDetail].注文金額'),('avg','[Order].注文時追加料金')],
        '[Member2].年代'                    : [('count','*'),('sum','[OrderDetail].数量'),('sum','[OrderDetail].注文金額'),('sum','[Order].注文時追加料金'),('avg','[OrderDetail].数量'),('avg','[OrderDetail].注文金額'),('avg','[Order].注文時追加料金')],
        '[Item].カラーカテゴリ'             : [('count','*'),('sum','[OrderDetail].数量'),('sum','[OrderDetail].注文金額'),('sum','[Order].注文時追加料金'),('avg','[OrderDetail].数量'),('avg','[OrderDetail].注文金額'),('avg','[Order].注文時追加料金')],
        '[Item].サイズ'                     : [('count','*'),('sum','[OrderDetail].数量'),('sum','[OrderDetail].注文金額'),('sum','[Order].注文時追加料金'),('avg','[OrderDetail].数量'),('avg','[OrderDetail].注文金額'),('avg','[Order].注文時追加料金')],
        '[Item].ショップ番号'               : [('count','*'),('sum','[OrderDetail].数量'),('sum','[OrderDetail].注文金額'),('sum','[Order].注文時追加料金'),('avg','[OrderDetail].数量'),('avg','[OrderDetail].注文金額'),('avg','[Order].注文時追加料金')],
        '[Item].ブランド番号'               : [('count','*'),('sum','[OrderDetail].数量'),('sum','[OrderDetail].注文金額'),('sum','[Order].注文時追加料金'),('avg','[OrderDetail].数量'),('avg','[OrderDetail].注文金額'),('avg','[Order].注文時追加料金')],
        '[Item].商品カテゴリ大'             : [('count','*'),('sum','[OrderDetail].数量'),('sum','[OrderDetail].注文金額'),('sum','[Order].注文時追加料金'),('avg','[OrderDetail].数量'),('avg','[OrderDetail].注文金額'),('avg','[Order].注文時追加料金')],
        '[Item].商品カテゴリ小'             : [('count', '*'), ('sum', '[OrderDetail].数量'), ('sum', '[OrderDetail].注文金額'),('sum', '[Order].注文時追加料金'), ('avg', '[OrderDetail].数量'), ('avg', '[OrderDetail].注文金額'),('avg', '[Order].注文時追加料金')],
        '[Item].商品詳細番号'               : [('count','*'),('sum','[OrderDetail].数量'),('sum','[OrderDetail].注文金額'),('sum','[Order].注文時追加料金'),('avg','[OrderDetail].数量'),('avg','[OrderDetail].注文金額'),('avg','[Order].注文時追加料金')],
        #'[Item].商品番号'                   : [('count','*'),('sum','[OrderDetail].数量'),('sum','[OrderDetail].注文金額'),('sum','[Order].注文時追加料金'),('avg','[OrderDetail].数量'),('avg','[OrderDetail].注文金額'),('avg','[Order].注文時追加料金')],
        '[OrderDetail].セール商品FLG'    : [('count','*'),('sum','[OrderDetail].数量'),('sum','[OrderDetail].注文金額'),('sum','[Order].注文時追加料金'),('avg','[OrderDetail].数量'),('avg','[OrderDetail].注文金額'),('avg','[Order].注文時追加料金')],
        '[Order].購入時デバイス'            : [('count','*'),('sum','[OrderDetail].数量'),('sum','[OrderDetail].注文金額'),('sum','[Order].注文時追加料金'),('avg','[OrderDetail].数量'),('avg','[OrderDetail].注文金額'),('avg','[Order].注文時追加料金')],
        'SUBSTRING(CONVERT(VARCHAR, [Order].注文日, 111), 1, 7)'                    : [('count','*'),('sum','[OrderDetail].数量'),('sum','[OrderDetail].注文金額'),('sum','[Order].注文時追加料金'),('avg','[OrderDetail].数量'),('avg','[OrderDetail].注文金額'),('avg','[Order].注文時追加料金')],
        '[Order].予約FLG'                   : [('count','*'),('sum','[OrderDetail].数量'),('sum','[OrderDetail].注文金額'),('sum','[Order].注文時追加料金'),('avg','[OrderDetail].数量'),('avg','[OrderDetail].注文金額'),('avg','[Order].注文時追加料金')]
    }




    return db_name,table,data_set

if __name__ == '__main__':
    print(00)


def data():
    db_name = 'FasionEC'

    table = "[Order] "
    table += "left outer join OrderDetail on [Order].order_id= [OrderDetail].order_id " + "left outer join Member2 on [Order].customer_id = [Member2].customer_id "
    table += "inner join Item on [OrderDetail].item_id = [Item].item_id AND [OrderDetail].product_detail_id = [Item].product_detail_id " + "left outer join Enquete on [Order].customer_id = [Enquete].customer_id"

    data_set = {
        '[Member2].QuestionnaireFLG'        : [('count','*'),('sum','[OrderDetail].quantity'),('sum','[OrderDetail].order_amount'),('sum','[Order].additional_charge'),('avg','[OrderDetail].quantity'),('avg','[OrderDetail].order_amount'),('avg','[Order].additional_charge')],
        '[Member2].Sex'                    : [('count','*'),('sum','[OrderDetail].quantity'),('sum','[OrderDetail].order_amount'),('sum','[Order].additional_charge'),('avg','[OrderDetail].quantity'),('avg','[OrderDetail].order_amount'),('avg','[Order].additional_charge')],
        '[Member2].province'                : [('count','*'),('sum','[OrderDetail].quantity'),('sum','[OrderDetail].order_amount'),('sum','[Order].additional_charge'),('avg','[OrderDetail].quantity'),('avg','[OrderDetail].order_amount'),('avg','[Order].additional_charge')],
        '[Member2].Age'                    : [('count','*'),('sum','[OrderDetail].quantity'),('sum','[OrderDetail].order_amount'),('sum','[Order].additional_charge'),('avg','[OrderDetail].quantity'),('avg','[OrderDetail].order_amount'),('avg','[Order].additional_charge')],
        '[Item].color'             :  [('count','*'),('sum','[OrderDetail].quantity'),('sum','[OrderDetail].order_amount'),('sum','[Order].additional_charge'),('avg','[OrderDetail].quantity'),('avg','[OrderDetail].order_amount'),('avg','[Order].additional_charge')],
        '[Item].size'                     : [('count','*'),('sum','[OrderDetail].quantity'),('sum','[OrderDetail].order_amount'),('sum','[Order].additional_charge'),('avg','[OrderDetail].quantity'),('avg','[OrderDetail].order_amount'),('avg','[Order].additional_charge')],
        '[Item].shop_id'               : [('count','*'),('sum','[OrderDetail].quantity'),('sum','[OrderDetail].order_amount'),('sum','[Order].additional_charge'),('avg','[OrderDetail].quantity'),('avg','[OrderDetail].order_amount'),('avg','[Order].additional_charge')],
        '[Item].brand_id'               : [('count','*'),('sum','[OrderDetail].quantity'),('sum','[OrderDetail].order_amount'),('sum','[Order].additional_charge'),('avg','[OrderDetail].quantity'),('avg','[OrderDetail].order_amount'),('avg','[Order].additional_charge')],
        '[Item].big_brand'             : [('count','*'),('sum','[OrderDetail].quantity'),('sum','[OrderDetail].order_amount'),('sum','[Order].additional_charge'),('avg','[OrderDetail].quantity'),('avg','[OrderDetail].order_amount'),('avg','[Order].additional_charge')],
        '[Item].small_brand'             : [('count','*'),('sum','[OrderDetail].quantity'),('sum','[OrderDetail].order_amount'),('sum','[Order].additional_charge'),('avg','[OrderDetail].quantity'),('avg','[OrderDetail].order_amount'),('avg','[Order].additional_charge')],
        '[Item].product_detail_id'               : [('count','*'),('sum','[OrderDetail].quantity'),('sum','[OrderDetail].order_amount'),('sum','[Order].additional_charge'),('avg','[OrderDetail].quantity'),('avg','[OrderDetail].order_amount'),('avg','[Order].additional_charge')],
        #'[Item].item_id'                   : [('count','*'),('sum','[OrderDetail].quantity'),('sum','[OrderDetail].order_amount'),('sum','[Order].additional_charge'),('avg','[OrderDetail].quantity'),('avg','[OrderDetail].order_amount'),('avg','[Order].additional_charge')],
        '[OrderDetail].item_sold_FLG'    : [('count','*'),('sum','[OrderDetail].quantity'),('sum','[OrderDetail].order_amount'),('sum','[Order].additional_charge'),('avg','[OrderDetail].quantity'),('avg','[OrderDetail].order_amount'),('avg','[Order].additional_charge')],
        '[Order].deviced'            : [('count','*'),('sum','[OrderDetail].quantity'),('sum','[OrderDetail].order_amount'),('sum','[Order].additional_charge'),('avg','[OrderDetail].quantity'),('avg','[OrderDetail].order_amount'),('avg','[Order].additional_charge')],
        'SUBSTRING(CONVERT(VARCHAR, [Order].order_data, 111), 1, 7)'                    : [('count','*'),('sum','[OrderDetail].quantity'),('sum','[OrderDetail].order_amount'),('sum','[Order].additional_charge'),('avg','[OrderDetail].quantity'),('avg','[OrderDetail].order_amount'),('avg','[Order].additional_charge')],
        '[Order].researvationFLG'                   : [('count','*'),('sum','[OrderDetail].quantity'),('sum','[OrderDetail].order_amount'),('sum','[Order].additional_charge'),('avg','[OrderDetail].quantity'),('avg','[OrderDetail].order_amount'),('avg','[Order].additional_charge')]
    }




    