from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json

# 请求http://127.0.0.1:8000/test/helloworld
def hello(request):
    return HttpResponse("Hello world ! ")

#http://127.0.0.1:8000/test/rtjson
def rtjson(request):
    data={
        'patient_name': '张三',
        'age': '25',
        'patient_id': '19000347',
        '诊断': '上呼吸道感染',
         }
    return HttpResponse(json.dumps(data),content_type='application/json')

##http://127.0.0.1:8000/test/get?username='zhaocuixia'

def get(request):
    result = {}
    if request.method == 'GET':
        username = request.GET.get('username')
        result['user'] = username
        result = json.dumps(result)
        return HttpResponse(result,content_type='application/json')


    pass
#contentType:application/x-www-form-urlencoded
#http://127.0.0.1:8000/test/login
# def post(request):
#     if request.method == 'POST':
#        username = request.POST.get('username')
#        print(username)
#        print(type(username))
#        return HttpResponse("hello," +username)
#     else:
#
#  contentType:"application/json"
def post(request):
    if request.method == 'POST':
       received_json_data = json.loads(request.body)
       print(received_json_data)
       username = received_json_data['username']
       return HttpResponse("hello," +username)
    else:
       return render(request,'login.html',locals())