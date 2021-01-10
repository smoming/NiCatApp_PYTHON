from django.http.response import JsonResponse
from rest_framework.decorators import api_view
import nation.models as m
from util.db_module import DbUtil
import util.dict_module as d
import util.app_setting as app

# Create your views here.


@api_view([app.HTTP_GET, app.HTTP_POST])
def list_add(request):
    db = DbUtil()
    if app.isHTTP_GET(request.method):
        return JsonResponse(m.toJson(db.fetch("SP_NATION_LIST")), safe=False)
    else:
        return JsonResponse(db.execute("SP_NATION_ADD", d.dictToList(request.data, 'ID', 'Name')), safe=False)


@ api_view([app.HTTP_GET, app.HTTP_PUT, app.HTTP_DELETE])
def get_update_delete(request, id):
    if(app.isHTTP_GET(request.method)):
        sp = "SP_NATION_GET"
        pa = [id]
    elif (app.isHTTP_PUT(request.method)):
        sp = "SP_NATION_UPDATE"
        pa = d.dictToList(request.data, 'ID', 'Name')
    else:
        sp = "SP_NATION_DELETE"
        pa = [id]

    db = DbUtil()
    if app.isHTTP_GET(request.method):
        return JsonResponse(m.toJson(db.fetch(sp, pa)), safe=False)
    else:
        return JsonResponse(db.execute(sp, pa), safe=False)
