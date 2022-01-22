from rest_framework import serializers
from .models import Customer
from rest_framework import validators

def mobile_validator(value):
    if len(value) > 10:
        raise serializers.ValidationError("Mobile number must be 10 digits")
    elif len(value) < 10:
        raise serializers.ValidationError("Mobile number must be 10 digits")
    else:
        return value

class CustomerSerializer(serializers.ModelSerializer): # ModelSerializer:
    mobile_no=serializers.CharField(max_length=200,validators=[mobile_validator])
    class Meta:
        model = Customer
        fields = "__all__"
        # read_only_fields =["name","roll"]
        
    def validate(self,data): #object leve validation
        if 'mobile_no' in data:
            if len(str(data['mobile_no'])) >= 11:
                raise serializers.ValidationError("Please enter a valid mobile number") 
            elif len(str(data['mobile_no'])) < 10:
                raise serializers.ValidationError("Please enter a valid mobile number")
        if 'customer_photo' in data:
            image=data['customer_photo']
            print(image.size,"this is image size") 
        return data
                 
        