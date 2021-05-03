from rest_framework import serializers
from .models import CovidReference

class CovidReferenceUpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidReference
        fields = ('user', 'verified')
