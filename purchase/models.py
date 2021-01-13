# from django.db import models

# Create your models here.


def toJson(list=[]):
    if list is None:
        list = []
    dict = []
    for x in list:
        dict.append(
            {"TransNo": x[0], "TradeDate": x[1], "Fee": x[2], "Remark": x[3]})

    return dict
