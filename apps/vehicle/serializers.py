from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['licence_plate', 'comment', 'person']

    def to_representation(self, instance):
        return instance

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['created_date', 'licence_plate', 'comment']
