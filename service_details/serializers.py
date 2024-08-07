from rest_framework import serializers
from .models import ServiceDetail, Worker

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'name', 'surname','job', 'email', 'image']

    def get_qr_code_link(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/qrcode/{obj.name}')

class ServiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDetail
        fields = ['id', 'LittleHeadName', 'LittleTextInfo', 'LargeHeadName', 'Image', 'DetailHead', 'DetailText']

