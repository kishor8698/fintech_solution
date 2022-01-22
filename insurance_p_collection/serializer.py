from rest_framework import serializers
from .models import Insurance_p_collection
from rest_framework import validators

class Insurance_p_collectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance_p_collection
        fields = "__all__"
        
    def validate(self,data): #object leve validation
        if 'ifsc_code' in data:
            if len(str(data['ifsc_code'])) >= 12:
                raise serializers.ValidationError("Please enter a valid Banck IFSC number")
            elif len(str(data['ifsc_code'])) < 11:
                raise serializers.ValidationError("Please enter a valid Banck IFSC number")
        if 'transaction_no' in data:
            if ' ' in data['transaction_no']:
                raise serializers.ValidationError("Whitespace is not allowed in transaction number")
        return data