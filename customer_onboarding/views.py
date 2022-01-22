from django.shortcuts import render
from .models import Customer
from .serializer import CustomerSerializer
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
from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomerAPI(APIView):
    authentication_classes=[JWTAuthentication]
    def get(self, request,*args, **kwargs):
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        stu=Customer.objects.all()
        serializer=CustomerSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request,*args,**kwargs):
        json_data=request.data
        serializer=CustomerSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
            res={}
            res['status'] = status.HTTP_201_CREATED
            res['msg']="Data Created Successfully......"
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request,*args, **kwargs):
        json_data=request.data #json data
        print(type(json_data),"<<<<<<<<<<<<<<<<<<<<<<<")
        id=json_data.get('id')
        stu=Customer.objects.get(id=id)
        serializer=CustomerSerializer(stu,data=json_data)
        if serializer.is_valid():
            serializer.save()
            res={}
            res['status'] = status.HTTP_200_OK
            res['msg']="Data Updated Successfully......"
            return Response(res)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request,*args, **kwargs):
        json_data=request.data #json data
        id=json_data.get('id')
        stu=Customer.objects.get(id=id)
        serializer=CustomerSerializer(stu,data=json_data,partial=True)#complex data
        if serializer.is_valid():
            serializer.save()
            res={}
            res['status'] = status.HTTP_201_CREATED
            res['msg']="Data Updated Successfully......"
            return Response(res)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Customergetspecificdetails(APIView):
    def get(self, request,*args, **kwargs):
        resp={}
        try:
            cust=Customer.objects.filter(id=kwargs['pk']).first()
            if cust is not None:   
                serializer=CustomerSerializer(cust)
                return Response(serializer.data,status=status.HTTP_200_OK) 
            resp['errors']='Something Went Wrong'
            return Response(resp,status=status.HTTP_400_BAD_REQUEST)
        except:
            resp['errors']='Something Went Wrong'
            return Response(resp,status=status.HTTP_400_BAD_REQUEST)

class CustomerDelete(APIView):
    def delete(self, request,*args, **kwargs):
        res={} 
        try:
            cust=Customer.objects.filter(id=kwargs['pk']).first()
            if cust is not None:
                cust.delete()
                res["msg"]="data deleted"
                res["status"]=status.HTTP_204_NO_CONTENT
                return Response(res,status.HTTP_204_NO_CONTENT)
            res={}
            res['msg']="Something Went wrong"    
            return Response(res,status=status.HTTP_400_BAD_REQUEST)
        except:
            res={}
            res['msg']="Something Went wrong"    
            return Response(res,status=status.HTTP_400_BAD_REQUEST)
     
class CustomerDeleteAll(APIView):
    def delete(self, request,*args, **kwargs):
        resp={}
        try:
            customer = Customer.objects.all()
            if customer is not None:    
                for i in customer:
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