from CRMapp.serializers import Abstract_serializer


class XML_serializer(Abstract_serializer):
    def __init__(self):
        super(XML_serializer, self).__init__()
        self.format = 'xml'

    def serialize_all(self, clazz):
        super(XML_serializer, self).serialize_all(clazz)
