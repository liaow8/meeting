# -*- coding: utf-8 -*-
import json

from django.test import TestCase

from blueking.component.shortcuts import ComponentClient


class TestAPI(TestCase):

    def setUp(self):
        self.client = ComponentClient(
            bk_app_code='test',
            bk_app_secret='xxx',
            common_args={
                'bk_username': 'admin',
            }
        )
        self.client.set_bk_api_ver('v2')

    def test_api(self):
        params = {
            'bk_biz_id': 1,
        }
        result = self.client.job.get_job_list(params)
        print json.dumps(result)
