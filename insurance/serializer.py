from rest_framework import serializers
from .models import Insurance
from rest_framework import validators

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = "__all__"
        # read_only_fields =["name","roll"]
        
    def validate(self,data): #object leve validation
        if 'email_id' in data:
            if "@gmail.com" not in data['email_id']:
                raise serializers.ValidationError("Please Enter valid email address")
        if 'mobile_no' in data:
            if len(str(data['mobile_no'])) >= 11:
                raise serializers.ValidationError("Please enter a valid mobile number") 
            elif len(str(data['mobile_no'])) < 10:
                raise serializers.ValidationError("Please enter a valid mobile number") 
            
        if 'alternate_mobile_no' in data:
            if len(str(data['alternate_mobile_no'])) >= 11:
                raise serializers.ValidationError("Please enter a valid alternate mobile number") 
            elif len(str(data['alternate_mobile_no'])) < 10:
                raise serializers.ValidationError("Please enter a valid alternate mobile number") 
            
        if  'product_type' in data:
            if data['product_type'] =='ARTH_Sanjeevni' or  data['product_type'] =='ARTH_Swasth': 
                if   'no_of_policy' in data:
                    if data['no_of_policy'] != 1:
                        raise serializers.ValidationError("For ARTH Sanjeevni and ARTH Swasth Fixed value is 1")
                    
        if 'product_type' in data:
            if data['product_type'] =='ARTH_Jeevan':
                if 'no_of_policy' in data:
                    result=Insurance.objects.first()
                    if data['no_of_policy'] >= 6:
                        raise serializers.ValidationError("For ARTH Jeevan policy value between 1 to 5 Allowed...")
                    
        # if 'no_of_policy' in data: # for PATCH request only
        #     if 'id' in data:
        #         result=Insurance.objects.filter(id=data['id']).first()
        #         print(result.product_type,"<<<<<<<<<<<<<<<<<<<")
        #         if result.product_type == 'ARTH_Sanjeevni' or result.product_type == 'ARTH_Swasth':
        #             if data['no_of_policy'] !=1:
        #                 raise serializers.ValidationError("For ARTH Sanjeevni and ARTH Swasth Fixed value is 1")
                    
        # if 'no_of_policy' in data: # for PATCH request only
        #     if 'id' in data:
        #         result=Insurance.objects.filter(id=data['id']).first()
        #         print(result.product_type,"<<<<<<<<<<<<<<<<<<<")
        #         if result.product_type == 'ARTH_Jeevan':
        #             if data['no_of_policy'] >=6:
        #                 raise serializers.ValidationError("For ARTH Jeevan policy value between 1 to 5 Allowed...")
        #     else:
        #         print("id not found",data['no_of_policy'])
        return data