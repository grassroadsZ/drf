from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import SerizlizerApp
from .serizlizers import SerizlizerSerizlers


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content-type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def serizlizerapp_list(request):
    """列出所有的 serlizliza app 返回新的serlizliza"""
    if request.method == "GET":
        ser_app = SerizlizerApp.objects.all()
        serializer = SerizlizerSerizlers(initial=ser_app, many=True)
        return JSONResponse(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SerizlizerSerizlers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=200)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def serizlizerapp_detail(request, pk):
    """更新或删除一个 serlizliza app"""
    try:
        ser_app = SerizlizerApp.objects.get(pk)
    except SerizlizerApp.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = SerizlizerSerizlers(ser_app)
        return JSONResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SerizlizerSerizlers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ser_app.delete()
        return HttpResponse(status=204)
