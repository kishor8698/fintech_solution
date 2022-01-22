from django.shortcuts import render
from .models import Insurance
from .serializer import InsuranceSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt # for function based view
from rest_framework.response import Response
from rest_framework import exceptions, status
import json
# from django.utils.decorators import method_decorator 
from django.utils.decorators import method_decorator#for class based view
from django.views import View # for class based view
from rest_framework.views import APIView
from rest_framework.decorators import api_view #for function based view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework import permissions

class InsuranceAPI(APIView):
    def get(self, request,*args, **kwargs):
        stu=Insurance.objects.all()
        serializer=InsuranceSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request,*args,**kwargs):
        json_data=request.data
        serializer=InsuranceSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
            res={}
            res['status'] = status.HTTP_201_CREATED
            res['msg']="Data Created Successfully......"
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request,*args, **kwargs):
        res={}
        json_data=request.data #json data
        if json_data:
            id=json_data.get('id')
            stu=Insurance.objects.get(id=id)
            serializer=InsuranceSerializer(stu,data=json_data)
            if serializer.is_valid():
                serializer.save()
                res['status'] = status.HTTP_201_CREATED
                res['msg']="Data Updated Successfully......"
                return Response(res,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            res["error"]="All fields are required"
            res["status"]=status.HTTP_400_BAD_REQUEST
            return Response(res,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request,*args, **kwargs):
        json_data=request.data #json data
        id=json_data.get('id')
        result=Insurance.objects.get(id=id)
        # if json_data['no_of_policy'] is not None:
        #     if result.product_type == 'ARTH_Sanjeevni' or result.product_type == 'ARTH_Swasth':
        #         if json_data['no_of_policy'] !=1:
        #             resp={}
        #             resp['policy_error']="For ARTH Sanjeevni and ARTH Swasth Fixed value is 1"
        #             return Response(resp,status=status.HTTP_400_BAD_REQUEST)
        #     elif result.product_type == 'ARTH_Jeevan':
        #         if json_data['no_of_policy'] >=6:
        #             resp={}
        #             resp['policy_error']="For ARTH Jeevan policy value between 1 to 5 Allowed..."
        #             return Response(resp,status=status.HTTP_400_BAD_REQUEST)
        serializer=InsuranceSerializer(result,data=json_data,partial=True)#complex data
        if serializer.is_valid():
            serializer.save()
            res={}
            res['status'] = status.HTTP_201_CREATED
            res['msg']="Data Updated Successfully......"
            return Response(res)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class InsuranceDelete(APIView):
        def delete(self, request,*args, **kwargs):
            res={}
            try:
                record=Insurance.objects.filter(id=kwargs['pk']).first()
                if record is not None:
                    record.delete()
                    res["msg"]="data deleted"
                    res["status"]=status.HTTP_204_NO_CONTENT
                    return Response(res,status.HTTP_204_NO_CONTENT)
                res['msg']="Something Went wrong"    
                return Response(res,status=status.HTTP_400_BAD_REQUEST)
            except:
                res['msg']="Something Went wrong"    
                return Response(res,status=status.HTTP_400_BAD_REQUEST)

class Insurancegetspecificdetails(APIView):
        def get(self, request,*args, **kwargs):
            resp={}
            try:
                record=Insurance.objects.filter(id=kwargs["pk"]).first()
                if record is not None:
                    serializer=InsuranceSerializer(record)
                    return Response(serializer.data,status=status.HTTP_200_OK)
                else:
                    resp['error']='Something Went wrong'
                    return Response(resp,status=status.HTTP_400_BAD_REQUEST)
            except:
                resp['error']='Something Went wrong'
                return Response(resp,status=status.HTTP_400_BAD_REQUEST) 
            
class InsuranceDeleteAll(APIView):
    def delete(self, request,*args, **kwargs):
        resp={}
        try:
            par = Insurance.objects.all()
            if par is not None:    
                for i in par:
                    # pass
                    i.delete()
                resp["msg"]="data deleted"
                resp["status"]=status.HTTP_204_NO_CONTENT
                return Response(resp,status.HTTP_204_NO_CONTENT)    
            else:
                resp['msg']="Something Went wrong"    
                return Response(resp,status=status.HTTP_400_BAD_REQUEST)    
        except:
            resp['msg']="Something Went wrong"    
            return Response(resp,status=status.HTTP_400_BAD_REQUEST) 