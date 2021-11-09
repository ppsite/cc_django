from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict


class CommonPageNumberPagination(PageNumberPagination):
    """ 通用分页设置 """
    page_size = 15
    page_query_param = 'current'
    page_size_query_param = 'pageSize'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('total', self.page.paginator.count),
            ('current', self.page.number),
            ('pageSize', self.get_page_size(request=self.request) or self.page_size),
            ('data', data)
        ]))
