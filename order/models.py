# from django.db import models

# Create your models here.


def toJson(list=[]):
    if list is None:
        list = []
    dict = []
    for x in list:
        dict.append(
            {"TransNo": x[0], "TradeDate": x[1], "CommodityID": x[2], "TradeQuantity": x[3], "TradeAmount": x[4], "ReceiptNo": x[5], "PurchaseNo": x[6], "Remark": x[7]})

    return dict
