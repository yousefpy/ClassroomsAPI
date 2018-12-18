from django.shortcuts import render
from rest_framework.generics import ListAPIView , RetrieveAPIView , CreateAPIView, RetrieveUpdateAPIView , DestroyAPIView
from classes.models import Classroom
from .serializers import ListSerializer, DetailSerializer , CreateSerializer

class ListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ListSerializer

class DetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class CreateView(CreateAPIView):
    serializer_class = CreateSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class UpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class DeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'