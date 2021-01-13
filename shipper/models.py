# from django.db import models

# Create your models here.


def toJson(list=[]):
    if list is None:
        list = []
    dict = []
    for x in list:
        dict.append(
            {"TransNo": x[0], "TradeDate": x[1], "Buyer": x[2], "TradeAmount": x[3], "Fee": x[4], "Delivery": x[5], "Remark": x[6]})

    return dict
