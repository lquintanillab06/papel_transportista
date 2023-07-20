from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication



# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        # Add extra responses here
        data['username'] = self.user.username
        data['groups'] = self.user.groups.values_list('name', flat=True)
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def get_user(request):
    print(request)
    ''' print(request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1])
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    authentication = JWTAuthentication()
    token_validated = authentication.get_validated_token(token)
    print(token_validated) '''
    #user, _ = authentication.get_user(token_validated)
    #print(user)
    authentication = JWTAuthentication()
    header = authentication.get_header(request)
    print(header)
    raw_token = authentication.get_raw_token(header) 
    print(raw_token)
    validated_token = authentication.get_validated_token(raw_token)
    print(validated_token)
    user = authentication.get_user(validated_token)
    print(user.__dict__)
    print(type(user))
   
    return Response({"username": user.username,"sucursal":user.sucursal.nombre})
