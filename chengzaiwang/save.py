from users.models import UserProfile
from .models import chengzaiwang
from django.http import JsonResponse
from operation.models import operation
def sh_Save(request):
    fin_res = []
    id = request.GET.get("id")
    res = chengzaiwang.objects.get(id=id)
    res.status = "未出库"
    res.save()
    print("入库成功")
    return JsonResponse(fin_res, safe=False)

