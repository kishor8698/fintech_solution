from rest_framework import serializers
from .models import Partner
from rest_framework import validators

class PartnerSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Partner
        fields = "__all__"
        # read_only_fields =["partner_ucic"]
        
    def validate(self,data): #object leve validation
        if 'email_id' in data:
            if "@gmail.com" not in data['email_id']:
                raise serializers.ValidationError("Please Enter valid email address")
            
        if 'mobile' in data:
            if len(str(data['mobile'])) >= 11:
                raise serializers.ValidationError("Please enter a valid mobile number") 
            elif len(str(data['mobile'])) < 10:
                raise serializers.ValidationError("Please enter a valid mobile number") 
            
        if 'alternate_mo_no' in data:
            if len(str(data['alternate_mo_no'])) >= 11:
                raise serializers.ValidationError("Please enter a valid mobile number") 
            elif len(str(data['alternate_mo_no'])) < 10:
                raise serializers.ValidationError("Please enter a valid mobile number") 
            
        if 'bank_ifsc' in data:
            if len(str(data['bank_ifsc'])) >= 12:
                raise serializers.ValidationError("Please enter a valid Banck IFSC number") 
            elif len(str(data['bank_ifsc'])) < 11:
                raise serializers.ValidationError("Please enter a valid Banck IFSC number")
        return data
    #kishor patil comment
        
