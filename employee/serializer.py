from rest_framework import serializers
from .models import Employee
from rest_framework import validators

class EmployeeSerializer(serializers.ModelSerializer): # ModelSerializer:
    # user_name_employee_ucic = serializers.CharField(read_only=True)
    class Meta:
        model = Employee
        fields = "__all__"
        # read_only_fields =["user_name_employee_ucic"]
        
    def validate(self,data): #object leve validation
        if 'personal_email_id' in data:
            if "@gmail.com" not in data['personal_email_id']:
                raise serializers.ValidationError("Please Enter valid email address")
            
        if 'office_email_id' in data:
            if "@gmail.com" not in data['office_email_id']:
                raise serializers.ValidationError("Please Enter valid email address")
            
        if 'guargian_mo_number' in data:
            if len(str(data['guargian_mo_number'])) >= 11:
                raise serializers.ValidationError("Please enter a valid mobile number") 
            elif len(str(data['guargian_mo_number'])) < 10:
                raise serializers.ValidationError("Please enter a valid mobile number") 
            
        if 'ifsc' in data:
            if len(str(data['ifsc'])) >= 12:
                raise serializers.ValidationError("Please enter a valid Banck IFSC number") 
            elif len(str(data['ifsc'])) < 11:
                raise serializers.ValidationError("Please enter a valid Banck IFSC number")
        return data       
        