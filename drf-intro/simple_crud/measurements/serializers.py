from rest_framework import serializers
from .models import Project, Measurement


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "latitude", "longitude", "created_at", "updated_at"]


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ["id", "value", "project", "created_at", "updated_at"]
