#coding=utf8
from django.shortcuts import render

# Create your views here.
from blueking.component.shortcuts import get_client_by_request
from common.mymako import render_mako_context, render_json
# from home_application.celery_tasks import async_task


def home(request):
    client = get_client_by_request(request)
    bizs = client.cc.get_app_list()['data']

    app_id = 2
    hosts = client.cc.get_app_host_list(app_id=app_id)['data']
    print hosts
    return render_json(hosts)
    # return render_mako_context(request, '/homework/home.html', {'bizs': bizs, "hosts": hosts})

def show_host(request):
    return render_mako_context(request, '/homework/host.html')

def show_operation(request):
    return render_mako_context(request, '/homework/operation.html')