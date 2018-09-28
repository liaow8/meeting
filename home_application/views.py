# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""
import json
import pdb
from django.http import HttpResponse
from blueking.component.shortcuts import get_client_by_request
from common.mymako import render_mako_context
# from home_application.celery_tasks import async_task


def home(request):
    """
    首页
    """
    # async_task.delay(1, 2)  # async_task函数将异步执行
    # async_task(1, 2)  # async_task作为普通函数执行
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')


def esb(request):
    client = get_client_by_request(request)
    data = client.cc.search_business()
    result = json.dumps(data)
    return HttpResponse(result)