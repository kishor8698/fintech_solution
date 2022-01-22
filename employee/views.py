from unittest import result
from django.shortcuts import render
from .models import Employee
from .serializer import EmployeeSerializer
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

class EmployeeAPI(APIView):
    def get(self, request,*args, **kwargs):
        resp={}
        try:
            emp=Employee.objects.all()
            serializer=EmployeeSerializer(emp,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            resp['error']='something went wrong'
            return Response(resp,status=status.HTTP_400_BAD_REQUEST)

    def post(self, request,*args,**kwargs):
        json_data=request.data
        try:
            serializer=EmployeeSerializer(data=json_data)
            if serializer.is_valid():
                serializer.save()
                res={}
                res['status'] = status.HTTP_201_CREATED
                res['msg']="Data Created Successfully......"
                return Response(res,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except:
            resp={}
            resp['error']="Something went wrong"
            return Response(resp,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request,*args, **kwargs):
        json_data=request.data #json data
        resp={}
        if json_data:
            id=json_data.get('id')
            emp=Employee.objects.get(id=id)
            serializer=EmployeeSerializer(emp,data=json_data)
            if serializer.is_valid():
                serializer.save()
                res={}
                res['status'] = status.HTTP_200_OK
                res['msg']="Data Updated Successfully......"
                return Response(res)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            resp["error"]="All fields are required"
            resp["status"]=status.HTTP_400_BAD_REQUEST
            return Response(resp,status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request,*args, **kwargs):
        json_data=request.data #json data
        id=json_data.get('id')
        try:
            emp=Employee.objects.get(id=id)
            serializer=EmployeeSerializer(emp,data=json_data,partial=True)#complex data
            if serializer.is_valid():
                serializer.save()
                res={}
                res['status'] = status.HTTP_201_CREATED
                res['msg']="Data Updated Successfully......"
                return Response(res,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except:
            resp={}
            resp['error']="Something went wrong"
            return Response(resp,status=status.HTTP_400_BAD_REQUEST)
        
class EmployeeDelete(APIView):            
    def delete(self, request,*args, **kwargs):
        res={}
        try:
            emp=Employee.objects.filter(id=kwargs['pk']).first()
            if emp is not None:
                emp.delete()
                res["msg"]="data deleted"
                res["status"]=status.HTTP_204_NO_CONTENT
                return Response(res,status.HTTP_204_NO_CONTENT)
            res={}
            res['msg']="Something Went wrong"    
            return Response(res,status=status.HTTP_400_BAD_REQUEST)
        except:
            resp={}
            resp['error']="Something went wrong"
            return Response(resp,status=status.HTTP_400_BAD_REQUEST)
        
class Employeegetspecificdetails(APIView):
    def get(self, request,*args, **kwargs):
        resp={}
        try:
            emp=Employee.objects.filter(id=kwargs['pk'])
            if emp is not None:
                serializer=EmployeeSerializer(emp,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                resp['error']='something went wrong'
                return Response(resp,status=status.HTTP_400_BAD_REQUEST)
        except:
            resp['error']='something went wrong'
            return Response(resp,status=status.HTTP_400_BAD_REQUEST)     
       
class EmployeeDeleteAll(APIView):
    def delete(self, request,*args, **kwargs):
        resp={}
        try:
            emp = Employee.objects.all()
            if emp is not None:    
                for i in emp:
                    print("one tiem")
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
       
class EmployeeLogin(APIView):
    def post(self, request, *args, **kwargs):
        user_name=request.data['employee_name']
        password=request.data['user_password']
        # role=request.data['role']
        result=Employee.objects.filter(employee_name=user_name).first()
        try:
            if result:
                if result.employee_name==user_name and result.user_password==password:
                    resp={}
                    resp['success']='Login Successfull..'
                    return Response(resp,status=status.HTTP_200_OK)
        except:
            return Response("Invalid Username and Password please check it.")
    