from api import models
from rest_framework import serializers

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Institute
        fields = "__all__"

        
class StudentSerializer(serializers.ModelSerializer):
    institute = InstituteSerializer(read_only=True)
    class Meta:
        model = models.Student
        fields = "__all__"