# from django.db import models

# Create your models here.


def toJson(list=[]):
    if list is None:
        list = []
    dict = []
    for x in list:
        dict.append(
            {"TransNo": x[0], "TradeDate": x[1], "Buyer": x[2], "CommodityID": x[3], "TradeQuantity": x[4], "TradeAmount": x[5], "ShipperNo": x[6], "Remark": x[7]})

    return dict
