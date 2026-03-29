from django.shortcuts import render

# Create your views here.
from app.models import Student
from django.shortcuts import get_object_or_404
from app.serliazier import Stu_serializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class studentViewSet(viewsets.ViewSet):

   
    def list(self, request):
        snippets = Student.objects.all()
        serializer = Stu_serializer(snippets, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = Stu_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def get_object(self, pk):
    #     try:
    #         return Student.objects.get(pk=pk)
    #     except Student.DoesNotExist:
    #         raise Http404
        

    def retrieve(self, request, pk=None):
        # snippet = self.get_object(pk)
        snippet = Student.objects.filter(id=pk)
        serializer = Stu_serializer(snippet)
        return Response(serializer.data)

    def update(self, request, pk=None):
        snippet = self.get_object(pk)
        serializer = Stu_serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        snippet = self.get_object(pk)
        serializer = Stu_serializer(snippet, data=request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



    