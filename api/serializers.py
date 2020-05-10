from api import models
from rest_framework import serializers

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Institute
        fields = "__all__"

        
class StudentSerializer(serializers.ModelSerializer):
    institute = InstituteSerializer(read_only=True)
    class Meta:
        models = models.Student
        fields = "__all__"