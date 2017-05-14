from abc import abstractmethod

from django.core import serializers
from django.http.response import HttpResponse


class Abstract_serializer(object):
    def __init__(self):
        self.format = None

    @abstractmethod
    def serialize_all(self,clazz):
        objects = clazz.objects.all()
        data = serializers.serialize('json', objects)
        return HttpResponse(data,
                            content_type='application/{0}'.format(self.format))
