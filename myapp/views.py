from rest_framework import serializers, viewsets
from . import models

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestModel.history.model
        fields = '__all__'

class TestViewSet(viewsets.ModelViewSet):
    queryset = models.TestModel.history.all()
    serializer_class = TestSerializer
