#Users views

# Django REST FRAMEWORK
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

#serializer
from proyectos.serializers.signup import *
from proyectos.serializers.user import *

class UserSignUpAPIView(APIView):
    #user sign up API view
    def post(self, request, *args, **kwargs):
        #Hadlle HTTP POST    request.
        serializer =  UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data,
        return Response(data, status=status.HTTP_201_CREATED)
