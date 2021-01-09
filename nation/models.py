# from django.db import models

# Create your models here.


def toJson(list=[]):
    if list is None:
        list = []
    dict = []
    for x in list:
        dict.append({"ID": x[0], "Name": x[1]})

    return dict
