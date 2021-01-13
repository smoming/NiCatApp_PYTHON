from django.http.response import JsonResponse
from rest_framework.decorators import api_view
import shipper.models as m
from util.db_module import DbUtil
import util.dict_module as d
import util.app_setting as app

# Create your views here.


@api_view([app.HTTP_GET, app.HTTP_POST])
def list_add(request):
    db = DbUtil()
    if app.isHTTP_GET(request.method):
        return JsonResponse(m.toJson(db.fetch("SP_SHIPPER_LIST", d.dictToList(request.query_params, 'StartDate', 'EndDate', 'Buyer'))), safe=False)
    else:
        return JsonResponse(db.execute("SP_SHIPPER_ADD", [','.join(request.data)]), safe=False)


@ api_view([app.HTTP_GET, app.HTTP_PUT, app.HTTP_DELETE])
def get_update_delete(request, TransNo):
    if(app.isHTTP_GET(request.method)):
        sp = "SP_SHIPPER_GET"
        pa = [TransNo]
    elif (app.isHTTP_PUT(request.method)):
        sp = "SP_SHIPPER_UPDATE"
        pa = d.dictToList(request.data, 'TransNo',
                          'TradeDate', 'Buyer', 'TradeAmount', 'Fee', 'Delivery', 'Remark')
    else:
        sp = "SP_SHIPPER_DELETE"
        pa = [TransNo]

    db = DbUtil()
    if app.isHTTP_GET(request.method):
        return JsonResponse(m.toJson(db.fetch(sp, pa)), safe=False)
    else:
        return JsonResponse(db.execute(sp, pa), safe=False)
