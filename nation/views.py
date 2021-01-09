from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from util.db_module import DbUtil
import util.dict_module as d
import json

# Create your views here.


@api_view(["GET", "POST"])
def list_add(request):
    db = DbUtil()
    if request.method == 'GET':
        return JsonResponse(toJson(db.fetch("SP_NATION_LIST")), safe=False)
    else:
        return JsonResponse(db.execute("SP_NATION_ADD", d.dictToList(request.data)), safe=False)


@api_view(["GET", "PUT", "DELETE"])
def get_update_delete(request, id):
    if(request.method == 'GET'):
        sp = "SP_NATION_GET"
        pa = [id]
    elif (request.method == 'PUT'):
        sp = "SP_NATION_UPDATE"
        pa = d.dictToList(request.data)
    else:
        sp = "SP_NATION_DELETE"
        pa = [id]

    db = DbUtil()
    if request.method == 'GET':
        return JsonResponse(toJson(db.fetch(sp, pa)), safe=False)
    else:
        return JsonResponse(db.execute(sp, pa), safe=False)


def toJson(list=[]):
    if list is None:
        list = []
    dict = []
    for x in list:
        dict.append({"ID": x[0], "Name": x[1]})

    return dict
