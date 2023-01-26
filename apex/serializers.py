from rest_framework import serializers

from .models import PatProfile, OpdRecord

class PatProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatProfile
        fields = ['uid', 'f_name', 'l_name', 'dob', 'parent_name', 'phone', 'sex', 'address', 'referred_by', 'created_at']

class OpdRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpdRecord
        fields = ['date', 'weight', 'height', 'temp', 'ref', 'id', 'charge']