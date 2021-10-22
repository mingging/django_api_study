from django.shortcuts import render
from api_user.serializers import UserSerializer

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from rest_framework import status

class UserView(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'success':'true', 'data':user_serializer.data}, status=200)
        else:
            return Response({'success':'false', 'error':user_serializer.errors}, status=400)
    
    def get(self, request, **kwargs):
        if kwargs.get('uid') is None:
            user_queryset = User.objects.all()
            user_serializer = UserSerializer(user_queryset, many=True)
            return Response({'count':user_queryset.count(),'data':user_serializer.data}, status=200)
        else:
            uid = kwargs.get('uid')
            user_queryset = User.objects.get(id=uid)
            user_serializer = UserSerializer(user_queryset)
            return Response(user_serializer.data, status=200)


        

    def put(self, request, **kwargs):
        if kwargs.get('uid') is None:
            return Response({'success':'false', 'message':"Invalid request"}, status=400)
        else:
            uid = kwargs.get('uid')
            user_object = User.objects.get(id=uid)
            update_serializer = UserSerializer(user_object, data=request.data)
            if update_serializer.is_valid():
                update_serializer.save()
                return Response({'success':'true', 'update_data':update_serializer.data}, status=200)
            else:
                return Response({'success':'false', 'message':"Invalid request"}, status=400)

        

    def delete(self, request, **kwargs):
        if kwargs.get('uid') is None:
            return Response({'sucess':'false', 'message':"Invalid request"}, status=400)
        else:
            uid = kwargs.get('uid')
            user_object = User.objects.get(id=uid)
            user_object.delete()
            return Response({"success":"true"}, status=200)