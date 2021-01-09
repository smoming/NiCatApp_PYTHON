from django.views.decorators.http import require_http_methods
from django.http.response import JsonResponse
from util.db_module import DbUtil
import json

# Create your views here.


@require_http_methods(["GET"])
def list(self):
    db = DbUtil()
    return JsonResponse(toJSON(db.fetch("SP_NATION_LIST")), safe=False, json_dumps_params={'ensure_ascii': False})


def toJSON(list=[]):
    if list is None:
        list = []
    dict = []
    for x in list:
        dict.append({"ID": x[0], "Name": x[1]})

    return dict
