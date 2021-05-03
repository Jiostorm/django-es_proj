from rest_framework import serializers
from .models import User

class UserVerifyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'middle_name', 'last_name')
