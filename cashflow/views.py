from django.http.response import JsonResponse
from rest_framework.decorators import api_view
import cashflow.models as m
from util.db_module import DbUtil
import util.dict_module as d
import util.app_setting as app

# Create your views here.


@api_view([app.HTTP_POST])
def account(request):
    db = DbUtil()
    return JsonResponse(db.execute("SP_ACCOUND_ADD", d.dictToList(request.query_params, 'xExeDate')), safe=False)


@api_view([app.HTTP_POST])
def unaccount(request):
    db = DbUtil()
    return JsonResponse(db.execute("SP_ACCOUND_DELETE", d.dictToList(request.query_params, 'xExeDate')), safe=False)
