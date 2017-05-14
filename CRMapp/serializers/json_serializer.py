from CRMapp.serializers import Abstract_serializer


class JSON_serializer(Abstract_serializer):
    def __init__(self):
        super(JSON_serializer, self).__init__()
        self.format = 'json'

    def serialize_all(self, clazz):
        super(JSON_serializer, self).serialize_all(clazz)
