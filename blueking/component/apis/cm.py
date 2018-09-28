# -*- coding: utf-8 -*-
from ..base import ComponentAPI


class CollectionsCM(object):
    """Collections of CM APIS"""

    def __init__(self, client):
        self.client = client

        self.get_capacity = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi/cm/get_capacity/',
            description=u'磁盘容量查询'
        )
        
