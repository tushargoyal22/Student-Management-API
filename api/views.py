# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import(
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    DestroyAPIView
)
from api import models,serializers
# Create your views here.


class StudentListView(ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentDetailsView(RetrieveAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer