from django.shortcuts import render
from .models import Partner
from .serializer import PartnerSerializer
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
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, serializers,renderers
from rest_framework_simplejwt.tokens import RefreshToken

class PartnerAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [renderers.JSONRenderer]
    
    def get(self, request,*args, **kwargs):
        try:
            stu=Partner.objects.all()
            serializer=PartnerSerializer(stu,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request,*args,**kwargs):
        json_data=request.data
        serializer=PartnerSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
            res={}
            res['status'] = status.HTTP_201_CREATED
            res['msg']="Data Created Successfully......"
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request,*args, **kwargs):
        json_data=request.data #json data
        id=json_data.get('id')
        stu=Partner.objects.get(id=id)
        serializer=PartnerSerializer(stu,data=json_data)
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
        stu=Partner.objects.get(id=id)
        serializer=PartnerSerializer(stu,data=json_data,partial=True)#complex data
        if serializer.is_valid():
            serializer.save()
            res={}
            res['status'] = status.HTTP_201_CREATED
            res['msg']="Data Updated Successfully......"
            return Response(res)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PartnerDelete(APIView):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        renderer_classes = [renderers.JSONRenderer]
        def delete(self, request,*args, **kwargs):
            res={} 
            record=Partner.objects.filter(id=kwargs['pk']).first()
            if record is not None:
                record.delete()
                res["msg"]="data deleted"
                res["status"]=status.HTTP_204_NO_CONTENT
                return Response(res,status.HTTP_204_NO_CONTENT)
            res={}
            res['msg']="Something Went wrong"    
            return Response(res,status=status.HTTP_400_BAD_REQUEST) 

class Partnergetspecificdetails(APIView):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        renderer_classes = [renderers.JSONRenderer]
        def get(self, request,*args, **kwargs):
            resp={}
            try:
                record=Partner.objects.filter(id=kwargs["pk"]).first()
                if record is not None:
                    serializer=PartnerSerializer(record)
                    return Response(serializer.data,status=status.HTTP_200_OK)
                else:
                    resp['error']='Something Went wrong'
                    return Response(resp,status=status.HTTP_400_BAD_REQUEST)
            except:
                resp['error']='Something Went wrong'
                return Response(resp,status=status.HTTP_400_BAD_REQUEST) 
            
class PartnerDeleteAll(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [renderers.JSONRenderer]
    def delete(self, request,*args, **kwargs):
        resp={}
        try:
            par = Partner.objects.all()
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
                
class PartnerLogin(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [renderers.JSONRenderer]
    
    def post(self, request):
        email=request.data['email_id']
        password=request.data['password']
        result=Partner.objects.filter(email_id=email).first()
        try:
            if result.email_id==email and result.password==password:
                resp={}
                resp['success']='Login Successfull..'
                resp['email']=email
                return Response(resp,status=status.HTTP_200_OK)
        except:
            return Response("Invalid Username and Password please check it.")