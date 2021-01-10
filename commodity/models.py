# from django.db import models

# Create your models here.


def toJson(list=[]):
    print(list)
    if list is None:
        list = []
    dict = []
    for x in list:
        dict.append(
            {"ID": x[0], "Name": x[1], "Style": x[2], "NationID": x[3], "SupplierID": x[4], "SupplierProductNo": x[5], "WholesalePrice": x[6], "RetailPrice": x[7], "Remark": x[8]})

    return dict
