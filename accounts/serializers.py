
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['id']         = str(user.id)
        token['username']   = user.username
        token['full_name']  = user.full_name
        if user.role:
            token['role']   = user.role.name
        

        return token