from django.shortcuts import render
from rest_framework import response
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from rent_book.models import Book, Student

from rent_book.serializers import BookSerializer, StudentSerializer

class StudentView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":"True", "data":serializer.data}, status = status.HTTP_200_OK)
        else:
            return Response({"success":"False", "error":"Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, **kwargs):
        if kwargs.get('id') is None:
            serializer = StudentSerializer(Student.objects.all(), many=True)
            return Response({"data":serializer.data, "count":Student.objects.all().count()}, status=status.HTTP_200_OK)
        else:
            no = kwargs.get('id')
            serializer = StudentSerializer(Student.objects.get(no=no))
            return Response({"data":serializer.data}, status=status.HTTP_200_OK)
        
    def put(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response({'success':'false', 'message':"Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            no = kwargs.get('id')
            serializers = StudentSerializer(Student.objects.get(no=no), data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response({'success':'true', 'data':serializers.data}, status=status.HTTP_200_OK)
            else:
                return Response({'success':'false', 'message':"Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response({'success':'false', 'message':"Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
        else: 
            no = kwargs.get('id')
            studnet_object = Student.objects.get(no=no)
            studnet_object.delete()
            return Response({"success":"true"}, status=status.HTTP_200_OK)

class BookView(APIView):
    def post(self, request):
        serializers = BookSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"success":"True", "data":serializers.data}, status=status.HTTP_200_OK)
        else:
            return Response({"success":"False", "error":"Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, **kwargs):
        if kwargs.get('id') is None:
            serializers = BookSerializer(Book.objects.all(), many=True)
            return Response({"success":"true", "data":serializers.data}, status=status.HTTP_200_OK)
        else:
            no = kwargs.get('id')
            serializers = BookSerializer(Book.objects.get(isbn=no))
            return Response({"success":"true", "data":serializers.data}, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response({'success':'false', 'message':"Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            no = kwargs.get('id')
            serializers = BookSerializer(Book.objects.get(isbn=no), data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response({'success':'true', 'data':serializers.data}, status=status.HTTP_200_OK)
            else:
                return Response({'success':'false', 'message':"Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response({'success':'false', 'message':"Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            no = kwargs.get('id')
            book_object = Book.objects.get(isbn=no)
            book_object.delete()
            return Response({"success":"true"}, status=status.HTTP_200_OK)
 

class RentView(APIView):
    pass
