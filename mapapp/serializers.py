from mapapp.models import Cctv
from rest_framework import serializers


class CctvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cctv
        fields = '__all__'
